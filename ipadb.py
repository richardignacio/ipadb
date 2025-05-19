'''Script to lookup IP address at AbuseIPDB using the API'''
import json
from os import environ
from requests import request
from sys import argv, exit

# Get IP address from the first command line argument
if len(argv) > 1:
    IP = argv[1]
else:
    print("Error: Requires an IP address as an argument")
    exit(1)

# Personal API Key from registering
api_key  = environ.get("API_KEY")

'''AbuseIPDB Endpoint Documentation
   https://docs.abuseipdb.com/?python#check-endpoint
'''  
base_url = 'https://api.abuseipdb.com/api/v2'
endpoint = '/check'
method   = 'GET'

headers  = {
    'Accept': 'application/json',
    'Key'   : api_key
}

query_string = {
    'ipAddress': IP,
    'maxAgeInDays': '90'
}

# Send request to AbuseIPDB
response = request(method, base_url + endpoint, params = query_string, headers = headers)

if response.content:
    # Import json as a python dict object
    _data = json.loads(response.content.decode())
    
    if response.status_code in [200]:
        # print(json.dumps(_data, indent=2))
        data = _data.get("data")
        score = int(data.get("abuseConfidenceScore", 0))
        
        if score > 90:
            print(f"{IP} is malicious")
        elif score == 0:
            print(f"{IP} has not been reported")
            
    else:
        print(f"Error ({response.status_code}): {json.dumps(_data, indent=2)}")

else:
    print(f"No response received")
