#!/usr/bin/env python3

import json
import requests
from requests.auth import HTTPBasicAuth

#Next addition is keeping the inputted values below temporarily until the user
# decides to input them again

vend_key = input("Vendor Key: ")
user_key = input("User Key: ")
metrc_license = input("Facility number: ")
state = input("State abbreviation: ")
base_url = 'https://sandbox-api-{}.metrc.com'.format(state)
api_endpoint = input("API Endpoint: ")
last_mod_start = input("Last modified start date in the format 2018, 1, 1: ")

#vend_key = ''
#user_key = ''
#metrc_license = ''
#api_endpoint = ''

a = HTTPBasicAuth(vend_key, user_key)


def get(path, date):
    url = '{}/{}/?licenseNumber={}&lastModifiedStart={}'.format(base_url, path, metrc_license, date, )
    print('URL:', url)
    r = requests.get(url, auth=a)
    print("The server response is: ", r.status_code)
    print('The script took {0} second !'.format(time.time() - startTime))

    if r.status_code == 200:
        return r.json()
    # Would like an elif that is r.status_code is 500 wait _ seconds and try again
    elif r.status_code == 500:
        print(r.status_code + ", try again.")
        time.sleep(10)
    else:
        print("Error")


import datetime
import time

startTime = time.time()

start_date = datetime.date(2020, 3, 1)

end_date = datetime.date.today()

delta = datetime.timedelta(days=1)

while start_date <= end_date:
    last_mod = start_date + delta

    print(get(api_endpoint, last_mod))

    start_date += delta


print ('The script took {0} second !'.format(time.time() - startTime))