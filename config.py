import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Notion API settings
NOTION_API_KEY = os.getenv('NOTION_API_KEY')
DATABASE_ID = os.getenv('NOTION_DATABASE_ID')

# Google Sheets settings
SPREADSHEET_ID = os.getenv('GOOGLE_SPREADSHEET_ID')
SHEET_NAME = os.getenv('GOOGLE_SHEET_NAME', 'notion-metrics-recorder')

# Google API settings
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# File paths
CREDENTIALS_FILE = os.getenv('GOOGLE_CREDENTIALS_FILE', 'credentials.json')
TOKEN_FILE = os.getenv('GOOGLE_TOKEN_FILE', 'token.json')
