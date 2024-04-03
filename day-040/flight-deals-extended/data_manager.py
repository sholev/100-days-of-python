import os, pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow


# https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets
class DataManager:

    def __init__(self, scopes, spreadsheet_id, name, cred_path):
        self.scopes = scopes
        self.spreadsheet_id = spreadsheet_id
        self.sheet_name = name
        self.service = self.build_service(cred_path)

    def build_service(self, cred_path):
        flow = InstalledAppFlow.from_client_secrets_file(
            cred_path,
            scopes=[self.scopes]
        )

        token_file = os.path.splitext(cred_path)[0] + '.pickle'
        if os.path.exists(token_file):
            credentials = pickle.load(open(token_file, "rb"))
        else:
            credentials = flow.run_local_server(port=0)
            pickle.dump(credentials, open(token_file, "wb"))

        return build('sheets', 'v4', credentials=credentials)

    def get(self):
        value_range = f'{self.sheet_name}'
        request = self.service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id,
            range=value_range,
        )
        return request.execute()

    def put_at_index(self, index: int, *data: str):
        value_range = f'{self.sheet_name}!A{index}'
        body = {
            'values': [data]
        }
        request = self.service.spreadsheets().values().update(
            spreadsheetId=self.spreadsheet_id,
            range=value_range,
            valueInputOption='RAW',
            body=body,
        )
        request.execute()

    def append(self, *values: str):
        value_range = f'{self.sheet_name}'
        body = {
            'values': [values]
        }

        request = self.service.spreadsheets().values().append(
            spreadsheetId=self.spreadsheet_id,
            range=value_range,
            valueInputOption='RAW',
            body=body,
        )
        request.execute()
