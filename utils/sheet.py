import httplib2
from googleapiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials

import os
from dotenv import load_dotenv
load_dotenv()

CREDENTIALS_FILE = os.getenv('CREDENTIALS_FILE')
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets ']
)
httpAuth = credentials.authorize(httplib2.Http())
service = discovery.build('sheets', 'v4', http=httpAuth)

sheet_metadata = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
sheet_id = sheet_metadata['sheets'][0]['properties']['sheetId']


def get_test_values():
    range = 'Лист1!B2:O2'
    result = service.spreadsheets().values().get(
        spreadsheetId = SPREADSHEET_ID,
        range=range
    ).execute()

    values = result.get('values', [])

    if not values or not values[0]:
        return []
    return values[0]


def get_expected_result():
    range = 'Лист1!B3:O3'
    result = service.spreadsheets().values().get(
        spreadsheetId = SPREADSHEET_ID,
        range=range
    ).execute()

    expected_result = result.get('values', [])

    if not expected_result or not expected_result[0]:
        return []
    return expected_result[0]


def write_and_format_cell(sheet_id, row, col, value):
    if value == "passed":
        bg = {"red": 53.0 / 255, "green": 148.0 / 255, "blue": 21.0 / 255}
    elif value == "failed":
        bg = {"red": 217.0 / 255, "green": 28.0 / 255, "blue": 28.0 / 255}
    elif value == "warning":
        bg = {"red": 222.0 / 255, "green": 200.0 / 255, "blue": 58.0 / 255}
    else:
        bg = {"red": 1.0, "green": 1.0, "blue": 1.0}

    fg = {"red": 1.0, "green": 1.0, "blue": 1.0}

    return [
        {
            "pasteData": {
                "data": value,
                "delimiter": ",",
                "coordinate": {
                    "sheetId": sheet_id,
                    "rowIndex": row,
                    "columnIndex": col
                },
                "type": "PASTE_NORMAL"
            }
        },
        {
            "repeatCell": {
                "range": {
                    "sheetId": sheet_id,
                    "startRowIndex": row,
                    "endRowIndex": row + 1,
                    "startColumnIndex": col,
                    "endColumnIndex": col + 1
                },
                "cell": {
                    "userEnteredFormat": {
                        "backgroundColor": bg,
                        "textFormat": {"foregroundColor": fg}
                    }
                },
                "fields": "userEnteredFormat(backgroundColor,textFormat)"
            }
        }
    ]



