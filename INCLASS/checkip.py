import json
from os import environ
from sys import argv
from requests import request
from pprint import pprint

BASE_URL = "https://api.abuseipdb.com/api/v2"
ENDPOINT = "/check"
API_KEY = environ.get("API_KEY")

HEADERS = {
    "Key": API_KEY,
    "Accept": "application/json"
}

METHOD = "GET"

IP = "222.68.155.105"

QUERY = {
    "ipAddress": IP,
    "maxAgeInDays": 90
}

IP_FILE_NAME =  argv[1]

ip_addresses = None
with open(IP_FILE_NAME, 'r') as ipfn:
    ip_addresses = ipfn.read()

for ip in ip_addresses.split():
    response = request(METHOD,BASE_URL + ENDPOINT, headers=HEADERS, params=QUERY)
    ip_response = json.loads(response.content.decode())
    if ip_response['data']['abuseConfidenceScore'] > 90:
        print(ip, "is malicious")
 


    








