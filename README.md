# ipadb
## Demo REST API Clients for AbuseIPDB

### Check Endpoint
https://docs.abuseipdb.com/?shell#check-endpoint

### Bulk Report Endpoint
https://docs.abuseipdb.com/?python#bulk-report-endpoint

**API Clients**
- ipadb.py  : Python Check endpoint client, accepts single IP address argument
- ipadb2.py : Python Check endpoint client, accepts multiple IP address arguements. Implements functions.
- ipadb.sh  : Bash Check endpoint client, accepts single IP address argument.

- ipadb_bulk_report.py: Python Bulk Report endpoint, accepts single file name argument.

- curl.cmd : Example curl commands for submitting to the Check and Bulk Report endpoints

**Test Data**
ip_list.txt: Multiple IP addresses, one per line.
report.csv : Multiple IP addresses, one per line. Meets the Bulk Report endpoint csv requirements.


