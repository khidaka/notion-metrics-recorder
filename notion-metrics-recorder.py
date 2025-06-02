import requests
import datetime
import os
import logging
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from config import *

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class NotionAPIError(Exception):
    """Custom exception for Notion API errors"""
    pass

class GoogleSheetsError(Exception):
    """Custom exception for Google Sheets API errors"""
    pass

def validate_config():
    """Validate that all required configuration values are present"""
    required_vars = {
        'NOTION_API_KEY': NOTION_API_KEY,
        'SPREADSHEET_ID': SPREADSHEET_ID
    }
    
    missing_vars = [var for var, value in required_vars.items() if not value]
    if missing_vars:
        raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

def count_notion_records(database_id):
    """Count records in Notion database with improved error handling"""
    if not database_id:
        logger.warning(f"Skipping undefined database ID")
        return None

    url = f"https://api.notion.com/v1/databases/{database_id}/query"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }

    has_more = True
    next_cursor = None
    total_records = 0

    try:
        while has_more:
            body = {}
            if next_cursor:
                body["start_cursor"] = next_cursor

            response = requests.post(url, headers=headers, json=body)
            response.raise_for_status()
            data = response.json()

            results = data.get("results", [])
            total_records += len(results)
            has_more = data.get("has_more", False)
            next_cursor = data.get("next_cursor", None)

        logger.info(f"Successfully counted {total_records} records in Notion database {database_id}")
        return total_records

    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to query Notion API: {str(e)}")
        raise NotionAPIError(f"Notion API request failed: {str(e)}")
    except ValueError as e:
        logger.error(f"Failed to parse Notion API response: {str(e)}")
        raise NotionAPIError(f"Invalid response from Notion API: {str(e)}")

def get_google_credentials():
    """Get Google API credentials with proper error handling"""
    creds = None
    
    try:
        if os.path.exists(TOKEN_FILE):
            creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
            
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not os.path.exists(CREDENTIALS_FILE):
                    raise FileNotFoundError(f"Credentials file not found: {CREDENTIALS_FILE}")
                flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
                creds = flow.run_local_server(port=0)
            
            with open(TOKEN_FILE, 'w') as token:
                token.write(creds.to_json())
                
        return creds
        
    except Exception as e:
        logger.error(f"Failed to get Google credentials: {str(e)}")
        raise GoogleSheetsError(f"Authentication failed: {str(e)}")

def append_to_google_sheet(counts):
    """Append data to Google Sheet with improved error handling"""
    try:
        creds = get_google_credentials()
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()

        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        values = [[now] + [str(count) if count is not None else "" for count in counts]]
        body = {'values': values}

        result = sheet.values().append(
            spreadsheetId=SPREADSHEET_ID,
            range=f"{SHEET_NAME}!A1",
            valueInputOption="USER_ENTERED",
            insertDataOption="INSERT_ROWS",
            body=body
        ).execute()

        logger.info(f"Successfully appended records to Google Sheet: {counts}")
        return result

    except HttpError as e:
        logger.error(f"Google Sheets API error: {str(e)}")
        raise GoogleSheetsError(f"Failed to update Google Sheet: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error while updating Google Sheet: {str(e)}")
        raise GoogleSheetsError(f"Failed to update Google Sheet: {str(e)}")

def main():
    """Main function with proper error handling"""
    try:
        validate_config()
        
        # Count records for all databases
        counts = []
        for db_id in [NOTION_DATABASE_ID1, NOTION_DATABASE_ID2, NOTION_DATABASE_ID3, 
                     NOTION_DATABASE_ID4, NOTION_DATABASE_ID5]:
            try:
                count = count_notion_records(db_id)
                counts.append(count)
            except NotionAPIError as e:
                logger.warning(f"Skipping database due to error: {str(e)}")
                counts.append(None)
        
        # Append all counts to Google Sheet
        append_to_google_sheet(counts)
        logger.info("Process completed successfully")
        
    except (NotionAPIError, GoogleSheetsError, ValueError) as e:
        logger.error(f"Process failed: {str(e)}")
        return 1
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return 1
    return 0

if __name__ == "__main__":
    exit(main())