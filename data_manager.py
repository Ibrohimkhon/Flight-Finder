import gspread
import os
import requests
import flight_data

# SERVICE_ACCOUNT_FILE = 'creds.json'
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# API_NAME = "sheets"
# API_VERSION = "v4"
# SPREADSHEET_ID = os.environ["SHEET_ID"]
# RANGE_NAME = 'Sheet1!A1:Z4999'
# gs = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)
# sh = gs.open_by_key(SPREADSHEET_ID)
# worksheet = sh.sheet1

SHEET_ENDPOINT = 'https://api.sheety.co/a25a2f7bc21f3af3ad7a0365d555e722/flightData/sheet1'
SHEETY_KEY = os.environ['SH_KEY']
SHEETY_AUTH = {"Authorization": f"Basic {SHEETY_KEY}"}

class DataManager:

    def __init__(self):
        self.destination_data = {}


    def get_destination_data(self):
        response = requests.get(url=SHEET_ENDPOINT, headers=SHEETY_AUTH)
        data = response.json()
        self.destination_data = data['sheet1']
        return(self.destination_data)


    def update_destination_codes(self):
        for city in self.destination_data:
            data = {
                'sheet1': {
                    "iataCode": city['iataCode']
                }
            }
            requests.put(url=f"{SHEET_ENDPOINT}/{city['id']}", headers=SHEETY_AUTH, json=data)
        print("Data updated")