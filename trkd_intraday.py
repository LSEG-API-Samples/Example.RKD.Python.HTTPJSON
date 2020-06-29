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

# Send HTTP request for all services


def doSendRequest(url, requestMsg, headers):
    result = None
    try:
        # send request
        result = requests.post(
            url, data=json.dumps(requestMsg), headers=headers)
        # print('outgoing message is %s'%(json.dumps(requestMsg)))
        # handle error
        if result.status_code is not 200:
            print('Request fail')
            print('response status %s' % (result.status_code))
            if result.status_code == 500:  # if username or password or appid is wrong
                # print('Error: %s' % (result.json()))
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

# Perform Intraday request


def RetrieveIntraday(token, appid):
     # construct Time Series Intraday request message
    ricName = input('Please input Symbol: ')
    intradayRequestMsg = None
    # change your fields (support these 'OPEN','HIGH','LOW','CLOSE','CLOSEYIELD','VOLUME','BID','ASK' fields only)
    fields = ['OPEN', 'HIGH', 'LOW', 'CLOSE',
              'CLOSEYIELD', 'VOLUME', 'BID', 'ASK']
    startTime = '2019-09-12T00:00:00'  # change your StartTime
    endtime = '2019-09-19T23:59:00'  # change your EndTime
    # interval = 'MINUTE' # change your interval between 'MINUTE', '5MINUTES', '30MINUTES' and 'HOUR'
    interval = input(
        'Input interested interval (\'MINUTE\' or \'5MINUTES\' or \'30MINUTES\' or \'HOUR\'): ')
    intradayRequestMsg = {
        'GetIntradayTimeSeries_Request_5': {
            'Field': fields,
            'TrimResponse': False,
            'Symbol': ricName,
            'StartTime': startTime,
            'EndTime': endtime,
            'Interval': interval,
            'MetaField': ['NAME', 'QOS', 'CCY', 'TZ', 'TZOFFSET', 'NAME_LL']
        }
    }
    # construct Time Series Intraday URL and header
    intradayURL = 'http://api.rkd.refinitiv.com/api/TimeSeries/TimeSeries.svc/REST/TimeSeries_1/GetIntradayTimeSeries_5'
    headers = {'content-type': 'application/json;charset=utf-8',
               'X-Trkd-Auth-ApplicationID': appid, 'X-Trkd-Auth-Token': token}

    print('############### Sending Time Series Intraday request message to RKD ###############')
    intradayResult = doSendRequest(intradayURL, intradayRequestMsg, headers)
    if intradayResult and intradayResult.status_code == 200:
        print('Time Series Intraday response message: ')
        # print(intradayResult.json())
        print(json.dumps(intradayResult.json(),
                         sort_keys=True, indent=2, separators=(',', ':')))


## ------------------------------------------ Main App ------------------------------------------ ##
if __name__ == '__main__':
    ## Get username, password and applicationid
    username = input('Please input username: ')
    ## Use getpass.getpass to hide user inputted password
    password = getpass.getpass(prompt='Please input password: ')
    appid = input('Please input appid: ') 

    token = CreateAuthorization(username, password, appid)
    print('Token = %s' % (token))
    # if authentication success, continue subscribing Time Series intraday
    if token:
        RetrieveIntraday(token, appid)
