from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials


from google.oauth2 import service_account


SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


SAMPLE_SPREADSHEET_ID = '1Vu_nLr6XL-L0KcTPBksmQEhdMJUws__faPvVZMFAGr0'



service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="sheet1!A1:B2").execute()
#values = result.get('values', [])

print(result)