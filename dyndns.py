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

while (True): 
    currentIp = getMyIp()
    