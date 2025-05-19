'''Script to lookup IP address at AbuseIPDB using the API'''
import json
from os import environ
from requests import request
from sys import argv, exit

# Get file name from the first command line argument
if len(argv) > 1:
    file_name = argv[1]
else:
    print("Error: Requires file name as an argument")
    exit(1)

# Personal API Key from registering
api_key  = environ.get("API_KEY")

base_url = 'https://api.abuseipdb.com/api/v2'
endpoint = '/bulk-report'
method   = 'POST'

headers  = {
    'Accept': 'application/json',
    'Key'   : api_key
}

files = {
    'csv': (file_name, open(file_name, 'rb'))
}

# Send request to AbuseIPDB
response = request(method, base_url + endpoint, files = files, headers = headers)

if response.content:
    # Import json as a python dict object
    _data = json.loads(response.content.decode())
    
    if response.status_code in [200]:
        print(json.dumps(_data, indent=2))
    else:
        print(f"Error ({response.status_code}): {json.dumps(_data, indent=2)}")

else:
    print(f"No response received")
