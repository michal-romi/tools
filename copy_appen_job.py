""" This programs copies an existing Appen job and loads data to it from a csv file """
import requests
import json
import os
import sys

API_KEY = "Nxthz9EEB_3oXHtWK3ES"
job_id = input("Please enter the job id you want to copy from: ")
copy_test_q = input("Copy test questions? yes/no: ")
file_path = input("Please enter the csv file you want to load to the new job (make sure there are headers) : ")

if copy_test_q == 'yes' or copy_test_q == 'Yes':
    gold_answer = 'true'
else:
    gold_answer = 'false'

# Check if the entered file exists
if os.path.exists(file_path):
    csv_file = open(file_path, 'rb')
else:
    print("File doesn't exist")
    sys.exit()

request_url = "https://api.appen.com/v1/jobs/{}/copy.json".format(job_id)
headers = {'content-type': 'text/csv'}
payload = {'key' : API_KEY, 'gold': gold_answer}
response = requests.get(request_url, params=payload, headers=headers)

status = response.status_code
content = response.json()
# in case the new job was created successfully - status code =200 then load the csv file to it
if status == 200:
    new_id = content['id']
    request_url = "https://api.appen.com/v1/jobs/{}/upload.json".format(new_id)
    headers = {'content-type': 'text/csv'}
    payload = {'key': API_KEY, 'force': 'true'}
    response = requests.put(request_url, data=csv_file, params=payload, headers=headers)

    status = response.status_code
    content = response.json()
    if status == 200:
        print("file was loaded successfully to job {}".format(new_id))
    else:
        print(status, content)
else:
    print(status, content)
