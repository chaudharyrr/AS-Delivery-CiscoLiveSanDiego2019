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
#from slackclient import SlackClient
import slack
from simplecrypt import encrypt, decrypt
from base64 import b64encode, b64decode

os.system('clear')

print("DNA Center - Discovery Using IP's Range (CiscoLive SanDiego 2019)")
print("---------------------------------------------------------------")
print
dnac_ip         = input('IP Address: 172.31.37.71')
username        = input('Username: ')
password        = getpass.getpass('Password: ')
range           = input ('IP Range: ')
slackUser       = input('Your First and Last Name: ')
SlackPassword   = getpass.getpass('Slack Password: ')
#Overwriting the input value with the DNAC Server IP for our testing env
dnac_ip 	= "172.31.37.71"

print (dnac_ip)

def getToken():
    post_url = "https://" + dnac_ip + "/api/system/v1/auth/token"
    headers = {'content-type': 'application/json'}
    response = requests.post(post_url, auth=HTTPBasicAuth(username=username,password=password), headers=headers,verify=False)
    if response.status_code != 200:
        print ("Verify Login \t\t\t\t \033[1;31;40m FAIL \033[0;0m")
        sys.exit()
    print
    print ("Verify Login \t\t\t\t \033[1;32;40m PASS \033[0;0m")
    print ("Retrieve Token ID \t\t\t \033[1;32;40m PASS \033[0;0m")
    r_json=response.json()
    token = r_json["Token"]
    return token

def getCliInstanceUUID(token):
    url = "https://" + dnac_ip + "/api/v1/global-credential?credentialSubType=CLI"
    header = {"content-type": "application/json", "X-Auth-Token":token}
    response = requests.get(url, headers=header, verify=False)
    if response.status_code != 200:
        print ("Retrieve CLI Instanceuuid \t\t \033[1;31;40m FAIL \033[0;0m")
        sys.exit()
    print ("Retrieve CLI Instanceuuid \t\t \033[1;32;40m PASS \033[0;0m")
    r_json=response.json()
    cliUUID = r_json["response"][0]["instanceUuid"]
    return cliUUID

def getSNMPv2InstanceUUID(token):
    url = "https://" + dnac_ip + "/api/v1/global-credential?credentialSubType=SNMPV2_READ_COMMUNITY"
    header = {"content-type": "application/json", "X-Auth-Token":token}
    response = requests.get(url, headers=header, verify=False)
    if response.status_code != 200:
        print ("Retrieve SNMPv2 Instanceuuid \t\t \033[1;31;40m FAIL \033[0;0m")
        sys.exit()
    print ("Retrieve SNMPv2 Instanceuuid \t\t \033[1;32;40m PASS \033[0;0m")
    r_json=response.json()
    snmpv2UUID = r_json["response"][0]["instanceUuid"]
    return snmpv2UUID

def postDiscovery(token, cliUUID, snmpv2UUID):
    url = "https://" + dnac_ip + "/api/v1/discovery"
    payload = {"discoveryType":"Range",
              "ipAddressList":"" + range + "",
              "ipFilterList":[],
              "protocolOrder":"ssh",
              "cdpLevel":"16",
              "timeout":"5",
              "retry":"3",
              "globalCredentialIdList":["" + cliUUID + "","" + snmpv2UUID + ""],
              "name":"" + slackUser + ""}
    header = {"content-type": "application/json", "X-Auth-Token":token}
    response = requests.post(url,data=json.dumps(payload), headers=header, verify=False)
    if response.status_code != 202:
        print ("Run Discovery \t\t\t\t \033[1;31;40m FAIL \033[0;0m")
        sys.exit()
    r_json=response.json()
    taskID = r_json["response"]["taskId"]
    print ("Run Discovery \t\t\t\t \033[1;32;40m PASS \033[0;0m")

def slackNotification():
    #encoded_cipher = "c2MAAo9SyHusC9Bgu3nMzSVS5qVHKnuDlyClO+BsyBUoLpWOzIH6bG3PCY7rhkJU187L/WjOWTWTR7zsC+hXqV2AKzGmELsaCml/88E9gEMzBffyQzrDYBj/HCC6Y5o8lsWqJKLvq/c3Uj2aqA/MiC4608baeCIG2y1hv7gsDDZMIwTmYbMUEqzATVdYnytR"
    #cipher = b64decode(encoded_cipher)
    #plaintext = decrypt(SlackPassword, cipher)
    #str_data = plaintext.decode('utf-8')
    #slack_token = str_data
    slack_token="xoxp-463078570673-463512828948-532319044546-2dee207d13024ca34e2b08e039c11b88"
    #sc = SlackClient(slack_token)
    sc = slack.WebClient(token=slack_token)
    sc.chat_postMessage(
      channel="CJ9AUU74M",
      text="DNA Center ...doing Discovery operation",
      username=slackUser,
      attachments= [
            {
                "fallback": "Required plain-text summary of the attachment.",
                "color": "#36a64f",
                "pretext": "[Auto-Generated Message]",
                "author_name": "DNA Center",
            	"author_icon": "https://pbs.twimg.com/profile_images/925717136281976832/UUA8Cz6q_400x400.jpg",
                "title": "Devices Discovery (Using IPs Range) Started Successfuly",
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

thetoken = getToken()
theCliUUID = getCliInstanceUUID(thetoken)
theSNMPv2UUID = getSNMPv2InstanceUUID(thetoken)
postDiscovery(thetoken, theCliUUID, theSNMPv2UUID)
theslackNotification = slackNotification()
