from requests import request, packages
from bs4 import BeautifulSoup

packages.urllib3.disable_warnings()
URL = "https://host-k1juquij-prod.prod.cywar.xyz:33114"

response = request("GET", URL, verify=False)
page = BeautifulSoup(response.text, "html.parser")
target = page.find("canvas").get("title")

params = target.split()
method = params[0]
value = params[1]
key = params[2]
params = {
    key: value
}

response = request(method, URL, verify=False, params=params)

while True:  
    page = BeautifulSoup(response.text, "html.parser")
    target = page.find("canvas").get("title")
    
    
    params = target.split()
    if len(params) < 3:
        print(target)
        break
    
    method = params[0]
    value = params[1]
    key = params[2]
    params = {
        key: value
    }
    print(f"Got {method} {key} {value}")
    
    if method == "POST":
        response = request(method, URL, verify=False, data=params)
    elif method == "GET":  
        response = request(method, URL, verify=False, params=params)
        
    
    # ask = input("Hit enter (q to quit)")
    # if ask.startswith("q"):
    #     break
    
    
    
    
    



