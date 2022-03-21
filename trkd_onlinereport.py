'''
The RKD API sample code is provided for informational purposes only 
and without knowledge or assumptions of the end users development environment. 
We offer this code to provide developers practical and useful guidance while developing their own code. 
However, we do not offer support and troubleshooting of issues that are related to the use of this code 
in a particular environment; it is offered solely as sample code for guidance. 
Please see the Refinitiv Knowledge Direct (RKD) API (formerly known as TRKD API) product page at https://my.refinitiv.com 
for additional information regarding the RKD API.'''

import os
import sys
import requests
import json
import getpass
from dotenv import load_dotenv

# Send HTTP request for all services


def doSendRequest(url, requestMsg, headers):
    result = None
    try:
        # send request
        result = requests.post(
            url, data=json.dumps(requestMsg), headers=headers)
        # print('outgoing message is %s'%(json.dumps(requestMsg)))
        # handle error
        if result.status_code != 200:
            print('Request fail')
            print('response status %s' % (result.status_code))
            if result.status_code == 500:  # if username or password or appid is wrong
                #print('Error: %s' % (result.json()))
                print('Error: %s' % (json.dumps(result.json(),
                                                sort_keys=True, indent=2, separators=(',', ':'))))
            result.raise_for_status()
    except requests.exceptions.RequestException as e:
        print('Exception!!!')
        print(e)
        sys.exit(1)
    return result


# Perform authentication
def CreateAuthorization(username, password, appid):
    token = None
    # create authentication request URL, message and header
    authenMsg = {'CreateServiceToken_Request_1': {
        'ApplicationID': appid, 'Username': username, 'Password': password}}
    authenURL = 'https://api.rkd.refinitiv.com/api/TokenManagement/TokenManagement.svc/REST/Anonymous/TokenManagement_1/CreateServiceToken_1'
    headers = {'content-type': 'application/json;charset=utf-8'}
    print('############### Sending Authentication request message to RKD ###############')
    authenResult = doSendRequest(authenURL, authenMsg, headers)
    if authenResult and authenResult.status_code == 200:
        print('Authen success')
        print('response status %s' % (authenResult.status_code))
        # get Token
        token = authenResult.json()['CreateServiceToken_Response_1']['Token']

    return token

# Perform Online Report request


def RetrieveOnlineReport(token, appid):
    # construct Online Report URL and header
    onlinereportURL = 'http://api.rkd.refinitiv.com/api/OnlineReports/OnlineReports.svc/REST/OnlineReports_1/GetSummaryByTopic_1'
    headers = {'content-type': 'application/json;charset=utf-8',
               'X-Trkd-Auth-ApplicationID': appid, 'X-Trkd-Auth-Token': token}
    # construct a Online Report request message
    onelinereportRequestMsg = {'GetSummaryByTopic_Request_1': {
        'Topic': 'OLRUTOPNEWS',
        'MaxCount': 20,
        'ReturnPrivateNetworkURL': False
    }
    }
    print('############### Sending News - Online Report request message to RKD ###############')
    onlinereportResult = doSendRequest(
        onlinereportURL, onelinereportRequestMsg, headers)
    if onlinereportResult and onlinereportResult.status_code == 200:
        print('Online Report response message: ')
        # print(onlinereportResult.json())
        print(json.dumps(onlinereportResult.json(), sort_keys=True,
                         indent=2, separators=(',', ':')))


## ------------------------------------------ Main App ------------------------------------------ ##
if __name__ == '__main__':
    # Load Environment Variables
    load_dotenv()
    # Get username, password and application_id from Environment Variables or .env
    username = os.getenv('RKD_USERNAME')
    # use getpass.getpass to hide user inputted password
    password = os.getenv('RKD_PASSWORD')
    appid = os.getenv('RKD_APP_ID')

    #If not Environment Variables or .env
    if not (username and password and appid):
        ## Get username, password and applicationid
        username = input('Please input username: ')
        ## Use getpass.getpass to hide user inputted password
        password = getpass.getpass(prompt='Please input password: ')
        appid = input('Please input appid: ')   


    token = CreateAuthorization(username, password, appid)
    print('Token = %s' % (token))

    # if authentication success, continue subscribing Online Report
    if token:
        RetrieveOnlineReport(token, appid)
