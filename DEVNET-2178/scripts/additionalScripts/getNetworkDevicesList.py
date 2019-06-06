#!/usr/bin/env
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json
import sys
import os
import datetime
import getpass      # Import getpass module to hid the password input string
import tabulate     # We use this module to generate a table view
import requests     # We use Python "requests" module to do HTTP GET query
from requests.auth import HTTPBasicAuth  #DNAC uses basic Authentication to get a token
import json         # Import JSON encoder and decode module
import warnings     # Import warnings module to customized the warning messages output level
warnings.filterwarnings("ignore")
requests.packages.urllib3.disable_warnings() # Disable warnings

# Do a clear screen - for a fresh/clear start
os.system('clear')

# DNAC parameters - User Inputs
print("DNA Center - API Bootcamp (POC Script)")
print("--------------------------------------")
print
dnac_ip     = raw_input('IP Address: ')
username 	= raw_input('Username: ')
password 	= getpass.getpass('Password: ')

def getToken():
# POST token API URL
    post_url = "https://" + dnac_ip + "/api/system/v1/auth/token"
# All DNAC REST API request and response content type is JSON.
    headers = {'content-type': 'application/json'}
# Make request and get response - "response" is the response of this request
    response = requests.post(post_url, auth=HTTPBasicAuth(username=username,password=password), headers=headers,verify=False)
# Validation for successful API call (POST) request
    if response.status_code != 200:
# In case of faliure, script will abort
		print ("Verify Login \t\t\t\tFAIL")
		sys.exit()
    print
# In case of a successful login, script will proceed with the below printouts
    print ("Verify Login \t\t\t\tPASS")
    print ("Retrieve Token ID \t\t\tPASS")
# Get the json-encoded content (i.e. our Token) from response
    r_json=response.json()
    token = r_json["Token"]
# Usualy the Token would not be printed (need to mark the next line) - That was done for this demo only
#    print (token)
# Saving the Token as variable for future API calls
    return token

def getDeviceList(token):
# GET network devices API URL
	url = "https://" + dnac_ip + "/api/v1/network-device"
# All DNAC REST API request and response content type is JSON. Note the "X-Auth-Token" string - populated with the the "token" variable
	header = {"content-type": "application/json", "X-Auth-Token":token}
# Make request and get response - "response" is the response of this request
	response = requests.get(url, headers=header, verify=False)
# Validation for successful API call (GET) request
	if response.status_code != 200:
# In case of faliure, script will abort
		print ("Retrieve Device List \t\t\tFAIL")
		sys.exit()
# In case of a successful API query, script will proceed with the device list / printouts
	print ("Retrieve Device List \t\t\tPASS")
	r_json=response.json()
        devices = r_json["response"]
        device_list = []
# Now extract host name, ip and type to a list. Also add a sequential number in front
        i=0
        for item in devices:
            i+=1
            device_list.append([i,item["hostname"],item["managementIpAddress"],item["type"]])
# We use tabulate module here to print a nice table format. You should use "pip" tool to install in your local machine
        print (tabulate.tabulate(device_list, headers=['hostname','ip','type'],tablefmt="rst"))

theTicket = getToken()
thegetDeviceList = getDeviceList(theTicket)
