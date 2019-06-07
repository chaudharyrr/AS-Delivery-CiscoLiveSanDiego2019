#!/usr/bin/env
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json
import sys
import os
import datetime
import getpass
import tabulate
import requests
from requests.auth import HTTPBasicAuth
import warnings
warnings.filterwarnings("ignore")
requests.packages.urllib3.disable_warnings()
import csv

os.system('clear')

print("DNA Center - Bulk Users Creation (CiscoLive SanDiego 2019)")
print("--------------------------------------------------------")
print
dnac_ip     = input('IP Address: 172.31.37.71')
username 	= input('Username: ')
password 	= getpass.getpass('Password: ')
user_file 	= input("Input File Name: ")
cnt = 0
#We are just overwriting the DNAC server IP to the test server env
dnac_ip = "172.31.37.71"
user_input = "/tmp/AS-Delivery-CiscoLiveSanDiego2019/DEVNET-2178/scripts/inputFiles/" + user_file

assert os.path.exists(user_input), "Unable to find the file at, "+str(user_input)

print("--------------------")
print ("Verify Input File Location \t\t \033[1;32;40m PASS \033[0;0m")

def readFile(token):
   token=token
   try:
        with open(user_input) as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                try:
                     createUser(token, row)
                except:
                    print("Exception on %s!" % row)
   except:
        print("Unexpected error while reading config file:", sys.exc_info()[0])

def getToken():
    post_url = "https://" + dnac_ip + "/api/system/v1/auth/token"
    headers = {'content-type': 'application/json'}
    response = requests.post(post_url, auth=HTTPBasicAuth(username=username,password=password), headers=headers,verify=False)
    if response.status_code != 200:
      print ("Verify Login \t\t\t\t \033[1;31;40m FAIL \033[0;0m")
      sys.exit()
    print ("Verify Login \t\t\t\t \033[1;32;40m PASS \033[0;0m")
    print ("Retrieve Token ID \t\t\t \033[1;32;40m PASS \033[0;0m")
    print("--------------------")
    r_json=response.json()
    token = r_json["Token"]
    return token

def createUser(token, row):
   global cnt
   try:
      url = "https://" + dnac_ip + "/api/system/v1/identitymgmt/user"
      payload = {"firstName": row['firstName'],
               "lastName": row['lastName'],
               "username": row['userName'],
               "passphrase": row['password'],
               "roleList":[
               row['role']
               ]
            }
      header = {"content-type": "application/json", "X-Auth-Token":token}
      response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
#      print(response.content)
      if response.status_code != 200:
         print ("User Creation \t\t\t\t \033[1;31;40m FAIL \033[0;0m")
         sys.exit()
      r_json=response.json()
      taskID=r_json["response"]["userId"]
      cnt=cnt+1
      print ("User Creation " + str(cnt) + "\t\t\t\t \033[1;32;40m PASS \033[0;0m \tUsername:UserID", row['userName'] + ":" + taskID)
   except:
      print("\033[1;31;40m Permission Denied. Only Super-Admin is allowd to create users \033[0;0m", sys.exc_info()[0])

token = getToken()
readFile(token)
