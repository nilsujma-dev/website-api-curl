import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import sys
import json

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


for curl in range(2500):
    response = requests.get("https://juice-shop.cpdevsecops.net/#/index.html", verify=False)
    print("Count of Website Curl", curl)
    print(response.text[:100])