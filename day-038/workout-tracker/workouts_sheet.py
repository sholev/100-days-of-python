import os, pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

spreadsheet_id = '11hNaGfrU-nH8GNig8eoeN_eIJ00eqvMB5m6Ps2Zhe-o'
sheet_name = 'workouts'

flow = InstalledAppFlow.from_client_secrets_file(
    '../../google_api_cred.json',
    scopes=['https://www.googleapis.com/auth/spreadsheets']
)

token_file = "../../google_api_cred.pickle"
if os.path.exists(token_file):
    credentials = pickle.load(open(token_file, "rb"))
else:
    credentials = flow.run_local_server(port=0)
    pickle.dump(credentials, open(token_file, "wb"))

service = build('sheets', 'v4', credentials=credentials)


def insert(*values: str):
    value_range = f'{sheet_name}'
    body = {
        'values': [values]
    }

    request = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=value_range,
        valueInputOption='RAW',
        body=body
    ).execute()

    print(request)
