[<img align="right" src="DEVNET-2178/pics/discoveryAPICalls/discoveryAPI1.png" title="DNA Center">](https://www.cisco.com/c/en/us/products/cloud-systems-management/dna-center/index.html)

# DNA Center - API Scavenger Hunt
In this workshop, you’ll get hands-on with DNA Center API capabilities. You'll practice three different challenges: <br />
:heavy_check_mark: How to retrieve necessary data and how to integrate with a (non-cisco) cross-solution (Slack). <br />
:heavy_check_mark: How to obtain meaningful data for a customized report. <br />
:heavy_check_mark: How to discover undocumented API calls for basic/advanced automation. <br />

---
# Table of Content
* [Lab Setup](#lab-setup)
* [DNA Center Environment](#dna-center-environment)
* [Scenario #1 - API Operation with Cross Platform Integratioin](#scenario-1)
* [Scenario #2 - Retrieve Unique Data Using API](#scenario-2)
* [Scenario #3 - Discover & Leverage Undocumented API](#scenario-3)
* [Additional Resources](#additional-resources)
* [Dive Deeper](#dive-deeper)
* [Code Snippets](#code-snippets)
* [Maintainers & Contributors](#maintainers--contributors)

# Lab Setup
> This section is expected to be completed in advance of the actual lab by the instructor to complete time-consuming steps.
### VPN Connectivity
1.	Open **Cisco AnyConnect Client**, type in the IP address of **64.100.58.118** and click **"Connect"**.<br />
    <img src="https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/vpnConnectivity/vpnConnect1.png" width="40%" height="40%">

2.	If the following warning message appears, click on **"Change Setting..."**. Otherwise, move to step #5<br />
    <img src="https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/vpnConnectivity/vpnConnect2.png" width="50%" height="50%">

3.	Uncheck the  **“Block connections to untrusted servers”** option (it's the last one) and close the window. <br />
    <img src="https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/vpnConnectivity/vpnConnect3.png" width="40%" height="40%">

4.	Re-establish the VPN connection by clicking **"Connect** again. <br />
    <img src="https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/vpnConnectivity/vpnConnect1.png" width="40%" height="40%">

5.	A new warning message would appear, click **"Connect Anyway"**. <br />
    <img src="https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/vpnConnectivity/vpnConnect4.png" width="50%" height="50%">

6.	When the login prompt appears, type in the following **Username** and **Password**. Once done, click **OK**. <br />

    ```yaml
    Username: scmcdona
    Password: C1scoDNA!
    ```

    <img src="https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/vpnConnectivity/vpnConnect5.png" width="40%" height="40%">

### Repo Clone
7. Open a **Terminal** window (Press CMD + Space, type "Terminal" and hit return). <br />

8. Clone the lab code to your workstation (Copy & Paste the commands below). <br />

    ```concole
    cd /tmp
    git clone https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/
    cd CiscoLive-Cancun2018/DEVNET-2178/scripts
    ```

### Lab Initialization
9. From the terminal window, run **`./setup.sh`** to initialize the lab environment. This will create a Python virtual environment, activate it, and install prerequisites. <br />

:warning:**Note: This step may take 1 - 2 minutes.**

<details>
      <summary>Sample Setup Output"</summary>

  ```concole
  Setting up the workstation environment for the lab.

  Creating Python 3 Virtual Environment
  Collecting requests (from -r requirements.txt (line 1))
    Using cached https://files.pythonhosted.org/packages/ff/17/5cbb026005115301a8fb2f9b0e3e8d32313142fe8b617070e7baad20554f/requests-2.20.1-py2.py3-none-any.whl
  Collecting pyOpenSSL (from -r requirements.txt (line 2))
    Using cached https://files.pythonhosted.org/packages/96/af/9d29e6bd40823061aea2e0574ccb2fcf72bfd6130ce53d32773ec375458c/pyOpenSSL-18.0.0-py2.py3-none-any.whl
  Collecting ndg-httpsclient (from -r requirements.txt (line 3))
    Using cached https://files.pythonhosted.org/packages/fb/67/c2f508c00ed2a6911541494504b7cac16fe0b0473912568df65fd1801132/ndg_httpsclient-0.5.1-py3-none-any.whl
  Collecting pyasn1 (from -r requirements.txt (line 4))
    Using cached https://files.pythonhosted.org/packages/d1/a1/7790cc85db38daa874f6a2e6308131b9953feb1367f2ae2d1123bb93a9f5/pyasn1-0.4.4-py2.py3-none-any.whl
  Collecting tabulate (from -r requirements.txt (line 5))
    Using cached https://files.pythonhosted.org/packages/12/c2/11d6845db5edf1295bc08b2f488cf5937806586afe42936c3f34c097ebdc/tabulate-0.8.2.tar.gz
  Collecting six (from -r requirements.txt (line 6))
    Using cached https://files.pythonhosted.org/packages/67/4b/141a581104b1f6397bfa78ac9d43d8ad29a7ca43ea90a2d863fe3056e86a/six-1.11.0-py2.py3-none-any.whl
  Collecting slackclient (from -r requirements.txt (line 7))
    Using cached https://files.pythonhosted.org/packages/0d/2f/1378e64a843a5a8a83d73caa59ac88c36c67e2b41ac0fab3422080ff13bd/slackclient-1.3.0-py2.py3-none-any.whl
  Collecting simple-crypt (from -r requirements.txt (line 8))
    Using cached https://files.pythonhosted.org/packages/60/66/5bf6feb073f715a61492f8a6d444ad3d884ada71af317ce7a9c80bebee60/simple-crypt-4.1.7.tar.gz
  Collecting idna<2.8,>=2.5 (from requests->-r requirements.txt (line 1))
    Using cached https://files.pythonhosted.org/packages/4b/2a/0276479a4b3caeb8a8c1af2f8e4355746a97fab05a372e4a2c6a6b876165/idna-2.7-py2.py3-none-any.whl
  Collecting urllib3<1.25,>=1.21.1 (from requests->-r requirements.txt (line 1))
    Using cached https://files.pythonhosted.org/packages/62/00/ee1d7de624db8ba7090d1226aebefab96a2c71cd5cfa7629d6ad3f61b79e/urllib3-1.24.1-py2.py3-none-any.whl
  Collecting certifi>=2017.4.17 (from requests->-r requirements.txt (line 1))
    Using cached https://files.pythonhosted.org/packages/56/9d/1d02dd80bc4cd955f98980f28c5ee2200e1209292d5f9e9cc8d030d18655/certifi-2018.10.15-py2.py3-none-any.whl
  Collecting chardet<3.1.0,>=3.0.2 (from requests->-r requirements.txt (line 1))
    Using cached https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl
  Collecting cryptography>=2.2.1 (from pyOpenSSL->-r requirements.txt (line 2))
    Using cached https://files.pythonhosted.org/packages/18/d5/7f725ac9ff162c93f67087414961b8256019527093d31e4c1fa9c377170a/cryptography-2.4.2-cp34-abi3-macosx_10_6_intel.whl
  Collecting websocket-client<1.0a0,>=0.35 (from slackclient->-r requirements.txt (line 7))
    Using cached https://files.pythonhosted.org/packages/26/2d/f749a5c82f6192d77ed061a38e02001afcba55fe8477336d26a950ab17ce/websocket_client-0.54.0-py2.py3-none-any.whl
  Collecting pycrypto (from simple-crypt->-r requirements.txt (line 8))
    Using cached https://files.pythonhosted.org/packages/60/db/645aa9af249f059cc3a368b118de33889219e0362141e75d4eaf6f80f163/pycrypto-2.6.1.tar.gz
  Collecting cffi!=1.11.3,>=1.7 (from cryptography>=2.2.1->pyOpenSSL->-r requirements.txt (line 2))
    Using cached https://files.pythonhosted.org/packages/8e/be/40b1bc2c3221acdefeb9dab6773d43cda7543ed0d8c8df8768f05af2d01e/cffi-1.11.5-cp36-cp36m-macosx_10_6_intel.whl
  Collecting asn1crypto>=0.21.0 (from cryptography>=2.2.1->pyOpenSSL->-r requirements.txt (line 2))
    Using cached https://files.pythonhosted.org/packages/ea/cd/35485615f45f30a510576f1a56d1e0a7ad7bd8ab5ed7cdc600ef7cd06222/asn1crypto-0.24.0-py2.py3-none-any.whl
  Collecting pycparser (from cffi!=1.11.3,>=1.7->cryptography>=2.2.1->pyOpenSSL->-r requirements.txt (line 2))
    Using cached https://files.pythonhosted.org/packages/68/9e/49196946aee219aead1290e00d1e7fdeab8567783e83e1b9ab5585e6206a/pycparser-2.19.tar.gz
  Installing collected packages: idna, urllib3, certifi, chardet, requests, six, pycparser, cffi, asn1crypto, cryptography, pyOpenSSL, pyasn1, ndg-httpsclient, tabulate, websocket-client, slackclient, pycrypto, simple-crypt
    Running setup.py install for pycparser ... done
    Running setup.py install for tabulate ... done
    Running setup.py install for pycrypto ... done
    Running setup.py install for simple-crypt ... done
  Successfully installed asn1crypto-0.24.0 certifi-2018.10.15 cffi-1.11.5 chardet-3.0.4 cryptography-2.4.2 idna-2.7 ndg-httpsclient-0.5.1 pyOpenSSL-18.0.0 pyasn1-0.4.4 pycparser-2.19 pycrypto-2.6.1 requests-2.20.1 simple-crypt-4.1.7 six-1.11.0 slackclient-1.3.0 tabulate-0.8.2 urllib3-1.24.1 websocket-client-0.54.0
  You are using pip version 9.0.1, however version 18.1 is available.
  You should consider upgrading via the 'pip install --upgrade pip' command.

  Setup complete.  To begin the lab run:

   source start
 ```
</details>

### Lab Startup
10. Run **`source start`** to prepare the workstation and to activate the pre-created Python virtual environment. <br />

<details>
  <summary>Sample Start Output</summary>

 ```concole
  Preparing the Workstation to Run this lab

  Note: This command script should be run with 'source start'
  to prepare the active terminal session.

  Activating Python Virtual Environment
  Opening Incognito browser windows for lab
 ```
</details>

### DNA Center and Slack Login
11. From the Incognito web browser, sign in to **DNA Center** using your assigned **Username** and **Password** and to **Slack** (ciscolive-workspace) using your assigned **Email Address** and **Password** (please check the  **[table](#login-information)** below for your credentials). For example: <br />
    <img src="https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/general/slackLogin1.png" width="40%" height="40%">

12. In Slack portal, make sure that you see the welcome message in the **"# ciscolive-cancun-2018"** channel. <br />
    <img src="https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/general/slackLogin3.png" width="50%" height="50%">

--------------------------------------------------------------------------------------------------

# DNA Center Environment
<div align="right">
    <b><a href="#table-of-content">↥ back to top</a></b>
</div>

### Login Information

|User   |DNA Center IP|DNA Center Username|DNA Center Password     |Slack Username |Slack Password     |
|:-----:|:-------------:|:------:|:-----------:|:------------------------------:|:-----------:|
|**User1**|`172.31.37.61`|`admin1`|`ciscolive123!`|`admin.1@ciscolivecancun2018.com`|`ciscolive123!`|
|**User2**|`172.31.37.61`|`admin2`|`ciscolive123!`|`admin.2@ciscolivecancun2018.com`|`ciscolive123!`|
|**User3**|`172.31.37.61`|`admin3`|`ciscolive123!`|`admin.3@ciscolivecancun2018.com`|`ciscolive123!`|
|**User4**|`172.31.37.61`|`admin4`|`ciscolive123!`|`admin.4@ciscolivecancun2018.com`|`ciscolive123!`|
|**User5**|`172.31.37.61`|`admin5`|`ciscolive123!`|`admin.5@ciscolivecancun2018.com`|`ciscolive123!`|
|**User6**|`172.31.37.61`|`admin6`|`ciscolive123!`|`admin.6@ciscolivecancun2018.com`|`ciscolive123!`|
|**User7**|`172.31.37.61`|`admin7`|`ciscolive123!`|`admin.7@ciscolivecancun2018.com`|`ciscolive123!`|
|**User8**|`172.31.37.61`|`admin8`|`ciscolive123!`|`admin.8@ciscolivecancun2018.com`|`ciscolive123!`|
|**User9**|`172.31.37.61`|`admin9`|`ciscolive123!`|`admin.9@ciscolivecancun2018.com`|`ciscolive123!`|
|**User10**|`172.31.37.61`|`admin10`|`ciscolive123!`|`admin.10@ciscolivecancun2018.com`|`ciscolive123!`|
|**User11**|`172.31.37.61`|`admin11`|`ciscolive123!`|`admin.11@ciscolivecancun2018.com`|`ciscolive123!`|
|**User12**|`172.31.37.61`|`admin12`|`ciscolive123!`|`admin.12@ciscolivecancun2018.com`|`ciscolive123!`|

--------------------------------------------------------------------------------------------------

# Scenario #1
<div align="right">
    <b><a href="#table-of-content">↥ back to top</a></b>
</div>

![alt text](https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story1/story1.png)
### Lab Objectives & Flow
![alt text](https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story1/lab1Flow.png) <br />

13. Let us quickly review the DNA Center "Network Discovery" API calls in **[Cisco documentation](https://developer.cisco.com/site/dna-center-rest-api/)** (please right-click and open in a new tab).

<img src="https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/general/DidYouKnow.png" width="7%" height="7%">**In DNA Center 1.2.6, there are 146 documented API calls. Many of them, have additional sub-options/calls**. <br />

14. right-click (open in a new tab) on the following POST API call to get in-depth information about all the available data types. <br />
<p align="center">
    <a href="https://developer.cisco.com/site/dna-center-rest-api/"><img src="https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/discoveryAPICalls/discoveryAPI1.png" title="DNA Center API Calls" align="center" /></a>
</p>

15. In this lab, we will trigger an IP-range discovery from CLI, leveraging several DNA Center an Slack API calls, and Python scripting. Due to time constraint, the script was already created. <br />
To execute the script, copy and paste the following command in the terminal: **`python autoDiscovery_viaIPRange.py`**  <br />

16. Please enter the following information to start the device discovery: <br />

|Prompt   | Input |
|:-----|:-------------|
|IP Address | **`172.31.37.61`** |
|Username | For example: **`admin1`** |
|Password | **`ciscolive123!`** |
|IP Range | **`172.31.37.91-172.31.37.94`** |
|Your First and Last Name | For example: **`John Doe`** |
|Slack Password | **`ciscolive123!`** |

:warning:**Please check the [table](#login-information) above for your assigned credentials.** <br />
:warning:**In case of typos, please click on "control C" to stop the script execution. After that, copy and paste `python autoDiscovery_viaIPRange.py` to restart this exercise.**

An example of script execution: <br />
    ![alt text](https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story1/Discovery1.png) <br />

17. In DNA Center, click on the **"Find New Devices"** hyperlink (located under the **"Network Devices"** section) to reach the **Discovery** page and check the the following (Another option is to click on the **rubric cub** icon (upper right), and select **Discovery**): <br />
<img src="https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story1/Discovery0.png" width="30%" height="30%">

* **DNA Center Discovery Window** - On the left-hand side, look for your discovery job (Hint: Search for your first and last name). <br />

    <details>
      <summary>Example of Discovery Operation</summary>
      <img align="left" src="https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story1/Discovery2.png" title="Discovery Operation">
    </details>

* **Slack Web Client** - What just happened? :smiley: (Hint: Check the **"# ciscolive-cancun-2018"** channel).  <br />

    <details>
      <summary>Example of Slack Web Client Notification</summary>
      <img align="left" src="https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story1/Discovery3.png" title="Slack Web Client Notification"><br /><br />
    </details><br /><br /><br /><br />

## Section Summary and Key Points
<table>
<tr>
<td>
  By running the DNA Center Discovery script, DNA Center auto-started a discovery process based on a user-defined IP Address range. The script also notified the group Slack channel about the discovery operation. All these operations were done using (published) API calls wrapped in a python script. A similar Discovery script, using an input file,  was created as well. Please contact the instructors for additional information.
</td>
</tr>
</table>

--------------------------------------------------------------------------------------------------

# Scenario #2
<div align="right">
    <b><a href="#table-of-content">↥ back to top</a></b>
</div>

![alt text](https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story2/story2.png) <br />
### Lab Objectives and Flow
![alt text](https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story2/lab2Flow.png)

18. Let us review the available DNA Center "Interfaces" API calls in **[Cisco documentation](https://developer.cisco.com/site/dna-center-rest-api/)**. (Hint: Search for ***"Get all interfaces"*** ) <br />

19. right-click on the following GET API call to get in-depth information about all the available data types. <br />
<p align="center">
    <a href="https://developer.cisco.com/site/dna-center-rest-api/"><img src="https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story2/newReport1.png" title="DNA Center API Calls" align="center" /></a>
</p>

20. Review the available data (i.e., response) of this API call. <br /> Do you see any value that may help with?

    ```yaml
    {
      "response": [
        {
          "adminStatus": "string",
          "className": "string",
          "description": "string",
          "deviceId": "string",
          "duplex": "string",
          "id": "string",
          "ifIndex": "string",
          "instanceTenantId": "string",
          "instanceUuid": "string",
          "interfaceType": "string",
          "ipv4Address": "string",
          "ipv4Mask": "string",
          "isisSupport": "string",
          "lastUpdated": "string",
          "macAddress": "string",
          "mappedPhysicalInterfaceId": "string",
          "mappedPhysicalInterfaceName": "string",
          "mediaType": "string",
          "nativeVlanId": "string",
          "ospfSupport": "string",
          "pid": "string",
          "portMode": "string",
          "portName": "string",
          "portType": "string",
          "serialNo": "string",
          "series": "string",
     =>   "speed": "string",  <=
          "status": "string",
          "vlanId": "string",
          "voiceVlan": "string"
        }
      ],
      "version": "string"
    }
    ```

21. **Great Job, you have found it!** :thumbsup: <br /> In this exercise, we will trigger specific API calls, leveraging two DNA Center API calls and Python scripting. Due to time constraint, the python script was already created. <br /> To execute the script, copy and paste the following command in the terminal: **`python autoReport_IFSpeedConf.py`**  <br />

22. Please enter the following information to generate the report: <br />

|Prompt   | Input |
|:-----|:-------------|
|IP Address | **`172.31.37.61`** |
|Username | For example: **`admin1`** |
|Password | **`ciscolive123!`** |

:warning:**Please check the [table](#login-information) above for your assigned credentials.** <br />
:warning:**In case of typos, please click on "control C" to stop the script execution. After that, copy and paste `python autoReport_IFSpeedConf.py` to restart this exercise.** <br />
:warning:**It is recommended to expand the Terminal window to 160x70 for optimal view.** <br />

An example of script execution: <br />
    ![alt text](https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story2/newReport2.png)

23. For advance reports, please use the **Command Runner** API calls.

<details>
  <summary>Command Runner - API Implantation via Postman (High-Level Overview)</summary>
    <p>

##### The Command Runner API requires four API calls.
##### 1. POST - Retrieve the API key.
##### 2. POST - Send the Command Runner API call and the payload (per deviceUuid).
##### 3. GET - Find the taskID of the previous POST command.
##### 4. GET - Find the file which stores the API call result.
##### Please see (Postman) captures below (note that the API response is not JSON - Content-Type→text/html; charset=utf-8).
</p>
<img align="left" src="https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/general/apiCommandRunner1.png" title="API Command Runner call1 (POST)">

<img align="left" src="https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/general/apiCommandRunner2.png" title="API Command Runner call2 (POST)">

<img align="left" src="https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/general/apiCommandRunner3.png" title="API Command Runner call3 (GET)">

<img align="left" src="https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/general/apiCommandRunner4.png" title="API Command Runner call4 (GET)">

</details>

## Section Summary and Key Points
<table>
<tr>
<td>
  In this section, we saw how to leverage the "Get All Interfaces" API call do build a tailor-made report. The generated data can be uploaded/integrated with cross-solutions such as Spark, Qlik, SmartSheet, and others.
</td>
</tr>
</table>

--------------------------------------------------------------------------------------------------

# Scenario #3
<div align="right">
    <b><a href="#table-of-content">↥ back to top</a></b>
</div>

![alt text](https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story3/story3.png)
### Lab Objectives and Flow
![alt text](https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story3/lab3Flow.png) <br />

:warning:**For this exercise, it is recommended to line-up the windows for optimal view.** <br />

24.	In DNA Canter GUI, right-click (anywhere) and choose **“Inspect”**. <br />
    <img src="https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story3/newAPI3.png" width="15%" height="15%">

25.	A new **Developer Tools** section will appear. <br />
    <img src="https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story3/newAPI4.png" width="80%" height="80%">

26.	Click on the **“Network”** tab. <br />
    ![alt text](https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story3/newAPI5.png)  

27.	Click on the **“:”** icon (right-hand side) and then choose **“Undock into separate window”**. <br />
    <img src="https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story3/newAPI6.png" width="25%" height="25%">  

28.	Now go back to DNA Canter GUI window and click on the **"Setting"** icon and choose **“System Settings”**. <br />
    ![alt text](https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story3/newAPI11.png)  

29.	In the **"System Setting"** windows, click on the **“Users”** tab. <br />
    ![alt text](https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story3/newAPI13.png)

30.	A new **“Users – Change Password”** window will appear. <br />
    ![alt text](https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story3/newAPI14.png)  

31.	Click on **“User Management”**. <br />
    ![alt text](https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story3/newAPI15.png)  
 
32.	Click on the **Add** button on the right side. <br />
    ![alt text](https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story3/newAPI16.png)  
33. Create a new user (using the following information) :heavy_exclamation_mark:**DO NOT CLICK ON "Save"**:heavy_exclamation_mark::

```yaml
First Name: Your first name (e.g. John)
Last Name: Your last name (e.g. Doe)
Username: Your first character of your First name & your Last name (e.g. jdoe)
Password: ciscolive123!
Role: NETWORK-ADMIN-ROLE
```

<img src="https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story3/newAPI17.png" width="45%" height="45%">

34.	In the Developer Tools window, clear all printout by clicking on the following icon (note that all the tracked data got cleared). <br />
    ![alt text](https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story3/newAPI18.png)

35.	Click on **"Save"** to create the user. <br />

36.	Make sure that the user was successfully created. <br />
    ![alt text](https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story3/newAPI19.png)

37.	Check the Developer Tools window. A similar trace will appear: <br />
    ![alt text](https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story3/newAPI20.png)

38.	Click on the first session (<img src="https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story3/newAPI21.png" width="20%" height="20%">) and review the following API captured information (on the right-hand side): <br />
* **“Request URL”** (Top right-hand side -> Headers -> General) <br />
    ![alt text](https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story3/newAPI22.png) <br /><br />
* **"Request Payload”** (Loewer right-hand side -> Headers -> Request Payload) <br />
    ![alt text](https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story3/newAPI23.png)

<img src="https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story3/newAPI24.png" width="7%" height="7%">**WOW! that is AWESOME! Why?** <br />

:bulb: We just discovered an undocumented POST API call. <br />
:bulb: Along with that, we found the payload information. <br /> <br />
In this exercise, we will leverage this information to create new users. <br />

39. Now, let us build a script which will use the newly discovered API for a bulk users creation (via a CSV file). Due to time constraint, the python script was already created. <br /> To execute the script, copy and paste the following command in the terminal: **`python autoUserCreate_viaFileImport.py`** <br />

40. Please enter the following information to create the new users (Note that the **input file** is based on your **user ID**): <br />

|Prompt   | Input |
|:-----|:-------------|
|IP Address | **`172.31.37.61`** |
|Username | For example: **`admin1`** |
|Password | **`ciscolive123!`** |
|Input file (for user admin1) | **`/tmp/CiscoLive-Cancun2018/DEVNET-2178/scripts/inputFiles/userList1.csv`**  |
|Input file (for user admin2) | **`/tmp/CiscoLive-Cancun2018/DEVNET-2178/scripts/inputFiles/userList2.csv`**  |
|Input file (for user admin3) | **`/tmp/CiscoLive-Cancun2018/DEVNET-2178/scripts/inputFiles/userList3.csv`**  |
|Input file (for user admin4) | **`/tmp/CiscoLive-Cancun2018/DEVNET-2178/scripts/inputFiles/userList4.csv`**  |
|Input file (for user admin5) | **`/tmp/CiscoLive-Cancun2018/DEVNET-2178/scripts/inputFiles/userList5.csv`**  |
|Input file (for user admin6) | **`/tmp/CiscoLive-Cancun2018/DEVNET-2178/scripts/inputFiles/userList6.csv`**  |
|Input file (for user admin7) | **`/tmp/CiscoLive-Cancun2018/DEVNET-2178/scripts/inputFiles/userList7.csv`**  |
|Input file (for user admin8) | **`/tmp/CiscoLive-Cancun2018/DEVNET-2178/scripts/inputFiles/userList8.csv`**  |
|Input file (for user admin9) | **`/tmp/CiscoLive-Cancun2018/DEVNET-2178/scripts/inputFiles/userList9.csv`**  |
|Input file (for user admin10) | **`/tmp/CiscoLive-Cancun2018/DEVNET-2178/scripts/inputFiles/userList10.csv`**  |
|Input file (for user admin11) | **`/tmp/CiscoLive-Cancun2018/DEVNET-2178/scripts/inputFiles/userList11.csv`**  |
|Input file (for user admin12) | **`/tmp/CiscoLive-Cancun2018/DEVNET-2178/scripts/inputFiles/userList12.csv`**  |

:warning:**In case of typos, please click on "control C" to stop the script execution. After that, copy and paste `python autoUserCreate_viaFileImport.py` to restart this exercise.**

An example for script execution: <br />
    ![alt text](https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story3/newAPI25.png)

41.	Go back to your browser and look at DNA Center again, you should see that the users were created successfully (Note: That's an example)<br />
    ![alt text](https://wwwin-github.cisco.com/AS-Internal/AS-Delivery-CiscoLiveCancun2018/blob/master/DEVNET-2178/pics/storyStrip/story3/newAPI26.png)

## Section Summary and Key Points

<table>
<tr>
<td>
  By running the DNA Center Bulk Users Creation script, DNA Center auto-configured a list of users from a CSV file. That was done using (unpublished) API call wrapped in a python script (A similar script can be created for modifying or deleting a list of users).
</td>
</tr>
</table>

# Additional Resources
<div align="right">
    <b><a href="#table-of-content">↥ back to top</a></b>
</div>

- Use the provided DNA Center application documentation (e.g. https://dna_ip/dna/apidoc).
- In DNA Center, there is an API tester which can be used to test API calls (e.g., https://dna_ip/dna/apitester).
- Check [Cisco DevNet](https://developer.cisco.com/docs/dna-center/) for API examples and code re-use.

# Dive Deeper
<div align="right">
    <b><a href="#table-of-content">↥ back to top</a></b>
</div>

Learning API is a challenge and a journey. <br /> There are several ways how to learn, practice and master API: <br />
- Practice DNA Center [Command Runner](https://www.cisco.com/c/en/us/td/docs/cloud-systems-management/network-automation-and-management/dna-center/1-2-6/user_guide/b_dnac_ug_1_2_6/about_command_runner.html) UI and API calls (the Command Runner enables you to run read-only commands on a network device and to retrieve its real-time configuration). <br />
- Take advantage of the built-in browsers [Inspect Element](https://developers.google.com/web/tools/chrome-devtools/network-performance/) tools. <br />
- Get familiar with [WireShark](https://www.wireshark.org/) (Network protocol analyzer). <br />
- Learn about [Fiddler](https://www.telerik.com/fiddler) (A powerful web debugging tool which logs HTTP(S) traffic between your computer and the Internet). <br />
- Contact Cisco.

# Code Snippets
<div align="right">
    <b><a href="#table-of-content">↥ back to top</a></b>
</div>

<details>
      <summary>Scenario #1 - "Discovery-viaIPRange.py"</summary>


  ```python
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
        from slackclient import SlackClient
        from simplecrypt import encrypt, decrypt
        from base64 import b64encode, b64decode

        os.system('clear')

        print("DNA Center - Discovery Using IP's Range (CiscoLive Cancun 2018)")
        print("---------------------------------------------------------------")
        print
        dnac_ip         = input('IP Address: ')
        username        = input('Username: ')
        password        = getpass.getpass('Password: ')
        range           = input ('IP Range: ')
        slackUser       = input('Your First and Last Name: ')
        SlackPassword   = getpass.getpass('Slack Password: ')

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
            encoded_cipher = "c2MAAubr2Zix/EyX9+DFi0zCKMHeoSzeQESvOqEnlxoHynQAzOuuh7/YATb2aCNXq0JmiyENW4v87zFbK9HWkQpaD+CX4kNEsnZdcBWhUdYZ6kpbllGcOKiEnrUhz3lf6GwHp8VB4ZkgD5KoUQy6mz25wGBiyHgWK8Pxa6RoeosyyNryKQMQ4a0pFCdW69ki"
            cipher = b64decode(encoded_cipher)
            plaintext = decrypt(SlackPassword, cipher)
            str_data = plaintext.decode('utf-8')
            slack_token = str_data
            sc = SlackClient(slack_token)
            sc.api_call(
              "chat.postMessage",
              channel="CDMS29EKX",
              username=slackUser,
              icon_emoji=':thumbsup:',
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
  ```
</details> <br />

<details>
  <summary>Scenario #2 - "autoReport_IFSpeedConf.py"</summary>

  ```python
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
      requests.packages.urllib3.disable_warnings() # Disable warnings
      from slackclient import SlackClient

      os.system('clear')

      print("DNA Center - Interface Speed Configuration (CiscoLive Cancun 2018)")
      print("------------------------------------------------------------------")
      print
      dnac_ip     = raw_input('IP Address: ')
      username 	= raw_input('Username: ')
      password 	= getpass.getpass('Password: ')

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

      def getInterfaceStatus(token):
      	url = "https://" + dnac_ip + "/dna/intent/api/v1/interface"
      	header = {"content-type": "application/json", "X-Auth-Token":token}
      	response = requests.get(url, headers=header, verify=False)
      	if response.status_code != 200:
      		print ("Retrieve Interfaces Status \t\t \033[1;31;40m FAIL \033[0;0m")
      		sys.exit()
      	print ("Retrieve Interfaces Status \t\t \033[1;32;40m PASS \033[0;0m")
      	r_json=response.json()
              devices = r_json["response"]
              device_list = []
              i=0
              for item in devices:
                  i+=1
                  device_list.append([i,item["portName"],item["portMode"],item["interfaceType"],item["status"],item["adminStatus"],item["speed"],item["vlanId"],item["ipv4Address"]])
      # We use tabulate module here to print a nice table format. You should use "pip" tool to install in your local machine
              table = (tabulate.tabulate(device_list, headers=['Port Name','Port Mode','Interface Type','Oper Status', 'Admin Satus', 'Speed (Kbit/sec)', 'VLAN ID', 'IP Address'],tablefmt="fancy_grid", numalign="center"))
              return table

      def tableFormat(table):
          print ("Formelizing Data \t\t\t \033[1;32;40m DONE \033[0;0m")
          print
          print(table)

      theTicket = getToken()
      thegetInterfaceStatus = getInterfaceStatus(theTicket)
      thetableFormat = tableFormat(thegetInterfaceStatus)
  ```
</details> <br />

<details>
  <summary>Scenario #3 - "autoUserCreate_viaFileImport.py"</summary>

  ```python
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

      print("DNA Center - Bulk Users Creation (CiscoLive Cancun 2018)")
      print("--------------------------------------------------------")
      print
      dnac_ip     = input('IP Address: ')
      username 	= input('Username: ')
      password 	= getpass.getpass('Password: ')
      user_input 	= input("Input File Aabsolute Path: ")
      cnt = 0

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
            print("Some error occurred in user creation", sys.exc_info()[0])

      token = getToken()
      readFile(token)
  ```
</details>

# Maintainers & Contributors
<div align="right">
    <b><a href="#table-of-content">↥ back to top</a></b>
</div>

:email: [Yossi Meloch](mailto:ymeloch@cisco.com) <br />
:email: [Stanley Chan](mailto:stanchan@cisco.com) <br />
:email: [Scott McDonald](mailto:cmcdona@cisco.com) <br />
<p align="center">
    <a href="https://www.cisco.com/c/en/us/products/cloud-systems-management/dna-center/index.html"><img src="https://media.giphy.com/media/QOwEXFdrKY364AwYND/giphy.gif" title="DNA Center" align="center" /></a>
</p>
