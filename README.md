## Syncing ZD to Google Sheets

Set up link to Google Sheets for write_to_spreadsheet.py:
* Using these two resources:
   * https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
   * http://gspread.readthedocs.io/en/latest/

Connect to ZenDesk API:
   * Store credentials in a local config.py file.
   * Use Views endpoint https://aweber.zendesk.com/api/v2/views/{view_id}/tickets.json to pull list of tickets in View.
