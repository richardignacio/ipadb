#!/bin/bash

curl -G "https://api.abuseipdb.com/api/v2/check" --data-urlencode "ipAddress=$1" -H "Key: $API_KEY" -H "Accept: application/json" -s