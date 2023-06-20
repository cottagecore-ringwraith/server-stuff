import json
import requests
import re
import sys
keyFile = open("keys.txt", "r")
content = keyFile.read()

apiKey = content.splitlines()[0] 
secretKey = content.splitlines()[1]
keyFile.close()

def getMyIp():
    #endpoint: https://porkbun.com/api/json/v3/ping
    #JSON Command Example
    # {
    # 	"secretapikey": "YOUR_SECRET_API_KEY",
    # 	"apikey": "YOUR_API_KEY"
    # }
    #JSON Response Example
    # {
    # 	"status": "SUCCESS",
    # 	"yourIp": "98.113.211.54"
    # }
    r = requests.post('https://porkbun.com/api/json/v3/ping', data={'secretapikey': secretKey, 'apikey': apiKey})

def raiseTheAlarm():
    print("aaaaaaaaa")
    #todo - make this actually work

def is_valid_ipv4_address(ip_address):
    parts = ip_address.split('.')
    
    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False

        value = int(part)
        if value < 0 or value > 255:
            return False

    return True

while (True): 
    currentIp = getMyIp()
    if (not (is_valid_ipv4_address(currentIp))):
        panic()
    else
        # so we got back a valid ip, lets check if the dns records need updating