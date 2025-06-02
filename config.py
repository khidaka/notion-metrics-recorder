import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Notion API configuration
NOTION_API_KEY = os.getenv('NOTION_API_KEY')
NOTION_DATABASE_ID1 = os.getenv('NOTION_DATABASE_ID_1')
NOTION_DATABASE_ID2 = os.getenv('NOTION_DATABASE_ID_2')
NOTION_DATABASE_ID3 = os.getenv('NOTION_DATABASE_ID_3')
NOTION_DATABASE_ID4 = os.getenv('NOTION_DATABASE_ID_4')
NOTION_DATABASE_ID5 = os.getenv('NOTION_DATABASE_ID_5')

# Google Sheets settings
SPREADSHEET_ID = os.getenv('GOOGLE_SPREADSHEET_ID')
SHEET_NAME = os.getenv('GOOGLE_SHEET_NAME', 'notion-metrics-recorder')

# Google API configuration
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# File paths
CREDENTIALS_FILE = os.getenv('GOOGLE_CREDENTIALS_FILE', 'credentials.json')
TOKEN_FILE = os.getenv('GOOGLE_TOKEN_FILE', 'token.json')
