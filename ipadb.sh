#!/bin/bash
BASE_URL='https://api.abuseipdb.com/api/v2'
ENDPOINT='/check'
IP=$1

if [ -z "$IP"  ]; then
  echo "Got nothing";
  exit 1;
fi

echo "==================================================="
echo "Looking up $IP..."
RESPONSE=$(curl -G "$BASE_URL$ENDPOINT" \
  --data-urlencode "ipAddress=$IP" \
  -d maxAgeInDays=90 \
  -H "Key: $API_KEY" \
  -H "Accept: application/json" \
  -s)

# Use jq to filter JSON output to scores > 90
echo
echo "Using jq:"
echo $RESPONSE | jq '
    .data | {ipAddress, abuseConfidenceScore} | 
    select(.abuseConfidenceScore > 90)
'

# Use pipe through cut and awk showing lines with scores > 90
echo
echo "Using piping throught cut and awk:"
echo $RESPONSE | cut -d'{' -f3 | cut -d'}' -f1 | cut -d',' -f1,5 | awk -F ':' '{ if ($3 > 90) print $1":"$2":"$3}'









