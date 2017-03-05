import requests

import config

# Password setup in config.
pw = config.pw

# View ID for Feature Requests
view_id = '209090008'
views_url = f'https://aweber.zendesk.com/api/v2/views/{view_id}/tickets.json'
headers = {'Accept': 'application/json'}


def pull_ticket_list():
    r = requests.get(views_url, auth=('danp@aweber.com', pw), headers=headers)
    data = r.json()
    ticket_list = data['tickets']
    return ticket_list
