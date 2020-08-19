#!/usr/bin/env python3

import json
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import time


#vend_key = input("Vendor Key: ")
#user_key = input("User Key: ")
#state = input("State abbreviation: ")

state = 'ca'
base_url = 'https://sandbox-api-{}.metrc.com'.format(state)


vend_key = 'vlURDoJQFcmHqm0hrvM9sY7pBG5HKv9DM5tminVsQGiWF7Dq'
user_key = 'hFS1854W-VjEIZZ0Ale8GfkW5Uv8zWNP-e4YGo3unBnIcuHE'
metrc_license = ''
api_endpoint = '/facilities/v1'

api_keys = HTTPBasicAuth(vend_key, user_key)


def get(path):
    error_401 = 0
    error_200 = 0
    error_500 = 0
    url = '{}/{}/?licenseNumber={}'.format(base_url, path, metrc_license)
    print('URL:', url)
    r = requests.get(url, auth=api_keys)
    if r.status_code == 401:
        print('{} ERROR / THERE IS AN ISSUE WITH THE API KEYS'.format(r.status_code))
        error_401 += 1
        print(error_401 + 1)
    elif r.status_code == 200:
        print('{} OK'.format(r.status_code))
        error_200 += 1
        print(error_200 + 1)
    elif r.status_code == 500 or 503:
        print('{} ERROR'.format(r.status_code))
        print(error_500 + 1)
    else:
        print(datetime.now)
        print('The server response is {}'.format(r.status_code))


count = 1
begin_time = datetime.now()


while True:
    if count <= 1000:
        get(api_endpoint)
        print()
        print(count)
        print("Current Time =", datetime.now())
        print('_______________________________')
        count += 1
    else:
        print(" ")
        print("This GET has been run {} times".format(count - 1))
        print('and took {} to complete'.format(datetime.now() - begin_time))
        quit()
