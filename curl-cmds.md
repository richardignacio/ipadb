# Example Curl Commands for AbuseIPDB API Endpoints

## Check Endpoint
### Multi-line for readability ###
```
curl -G "https://api.abuseipdb.com/api/v2/check" \
  --data-urlencode "ipAddress=218.92.0.235" \
  -d maxAgeInDays=90 \
  -H "Key: $API_KEY" \
  -H "Accept: application/json"
```

### One-line ###

`curl -G "https://api.abuseipdb.com/api/v2/check" --data-urlencode "ipAddress=218.92.0.235" -d maxAgeInDays=90 -H "Key: $API_KEY" -H "Accept: application/json"`

## Bulk Report Endpoint ##

### Multi-line for readability ###
```
curl https://api.abuseipdb.com/api/v2/bulk-report \
  -F csv=@report.csv \
  -H "Key: $API_KEY" \
  -H "Accept: application/json" \
  > output.json
```



