import gspread
from oauth2client.service_account import ServiceAccountCredentials
import zd_api

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Feature Requests").sheet1

feature_requests = zd_api.pull_ticket_list()


# Update cell values for A, B column
def update_cells(x, val_1, val_2):
    sheet.update_cell(x, 1, val_1)
    sheet.update_cell(x, 2, val_2)


# Iterate through data list placing tickets number and subject line in sheet
def update_spreadsheet(the_list):
    i = 2
    for ticket in the_list:
        update_cells(i, ticket['id'], ticket['subject'])
        i += 1


update_spreadsheet(feature_requests)
