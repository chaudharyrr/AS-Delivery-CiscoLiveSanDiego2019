#!/usr/bin/env
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json			# Import JSON encoder and decode module
import sys
import os
import datetime
import getpass      # Import getpass module to hid the password input string
import tabulate     # We use this module to generate a table view
import requests     # We use Python "requests" module to do HTTP GET query
from requests.auth import HTTPBasicAuth  #DNAC uses basic Authentication to get a token  
import warnings     # Import warnings module to customized the warning messages output level
warnings.filterwarnings("ignore")
requests.packages.urllib3.disable_warnings() # Disable warnings
from slackclient import SlackClient

# Do a clear screen - for a fresh/clear start
os.system('clear')

# DNAC parameters - User Inputs
print("DNA Center - Import Device List (CiscoLive Cancun 2018)")
print("--------------------------------------------")
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
		print ("Verify Login \t\t\t\t \033[1;31;40m FAIL \033[0;0m")
		sys.exit()
    print
# In case of a successful login, script will proceed with the below printouts
    print ("Verify Login \t\t\t\t \033[1;32;40m PASS \033[0;0m")
    print ("Retrieve Token ID \t\t\t \033[1;32;40m PASS \033[0;0m")
# Get the json-encoded content (i.e. our Token) from response
    r_json=response.json()
    token = r_json["Token"]
# Usualy the Token would not be printed (need to mark the next line) - That was done for this demo only
#    print (token)
# Saving the Token as variable for future API calls
    return token

def importDeviceList(token):
# GET network devices API URL
	url = "https://" + dnac_ip + "/api/v1/network-device"
# All DNAC REST API request and response content type is JSON. Note the "X-Auth-Token" string - populated with the the "token" variable
	headers = {'X-Auth-Token':token, 'Accept': 'application/json'}
# Python files-import handler
	files = { 'file': (os.path.basename('/Users/ymeloch/Desktop/CiscoLive_Cancun/bulk-import-devices-template.csv'), open('/Users/ymeloch/Desktop/CiscoLive_Cancun/bulk-import-devices-template.csv', 'rb'), 'application/octet-stream')}
# Make request and get response - "response" is the response of this request
	response = requests.post(url, headers=headers, files=files, verify=False)

# Debug lines (Raise exception if 4xx or 5xx HTTP Error)
#	response.raise_for_status()
#	print("HTTP Code: %s" % response.status_code)
#	print("Content:\n%s" % response.content)
#	print("%s" % json.dumps(response.json(), sort_keys=True, indent=4, separators=(',', ': ')))

# Validation for successful API call (POST) request
	if response.status_code != 202:
# In case of faliure, script will abort
		print ("Import Device List \t\t\t \033[1;31;40m FAIL \033[0;0m")
		sys.exit()
# In case of a successful API query, script will proceed with the device list / printouts
	print ("Import Device List \t\t\t \033[1;32;40m PASS \033[0;0m")

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
		print ("Retrieve Device List \t\t\t \033[1;31;40m FAIL \033[0;0m")
		sys.exit()
# In case of a successful API query, script will proceed with the device list / printouts
	print ("Retrieve Device List \t\t\t \033[1;32;40m PASS \033[0;0m")
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

# pre-requisite: sudo pip install slackclient

def slackNotification():
	slack_token = "xoxp-463078570673-463512828948-464020819424-f402cb372d17eb965f3a961b6e93a4ff"
	sc = SlackClient(slack_token)

	sc.api_call(
	  "chat.postMessage",
	  channel="CDMS29EKX",
	#  text="[That is an automated message] Hey team, auto DNA Center discovery started",
	  username='Administrator',
	  icon_emoji=':robot_face:',
	  attachments= [
	        {
	            "fallback": "Required plain-text summary of the attachment.",
	            "color": "#36a64f",
	            "pretext": "[Auto-Generated Message]",
	            "author_name": "DNA Center (10.122.6.118)",
            	"author_icon": "https://pbs.twimg.com/profile_images/925717136281976832/UUA8Cz6q_400x400.jpg",
	            "title": "Devices Discovery (Using File Import) Started Successfuly",
	            "title_link": "https://api.slack.com/",
	            "fields": [
	                {
	                    "title": "Priority - High",
	                }
	            ],
	            "image_url": "http://my-website.com/path/to/image.jpg",
	            "thumb_url": "http://example.com/path/to/thumb.png",
	            "footer": "Slack API",
	            "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png",
	        }
	    ]
	)

theTicket = getToken()
theimportDeviceList = importDeviceList(theTicket)
thegetDeviceList = getDeviceList(theTicket)
theslackNotification = slackNotification()
