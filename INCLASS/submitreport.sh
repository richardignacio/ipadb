#!/bin/bash

curl "https://api.abuseipdb.com/api/v2/bulk-report" -F "csv=@$1" -H "Key: $API_KEY" -H "Accept: application/json"


