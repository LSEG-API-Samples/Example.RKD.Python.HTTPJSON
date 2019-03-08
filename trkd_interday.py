'''
The TRKD API sample code is provided for informational purposes only 
and without knowledge or assumptions of the end users development environment. 
We offer this code to provide developers practical and useful guidance while developing their own code. 
However, we do not offer support and troubleshooting of issues that are related to the use of this code 
in a particular environment; it is offered solely as sample code for guidance. 
Please see the Thomson Reuters Knowledge Direct product page at http://customers.thomsonreuters.com 
for additional information regarding the TRKD API.'''


import os
import sys
import requests
import json
import getpass

# Send HTTP request for all services
def doSendRequest(url, requestMsg, headers):
    result = None
    try:
        ##send request
        result = requests.post(url, data=json.dumps(requestMsg), headers=headers)
        # print('outgoing message is %s'%(json.dumps(requestMsg)))
        ## handle error
        if result.status_code is not 200:
            print('Request fail')
            print('response status %s'%(result.status_code))
            if result.status_code == 500: ## if username or password or appid is wrong
                print('Error: %s'%(result.json()))
            result.raise_for_status()
    except requests.exceptions.RequestException as e:
        print('Exception!!!')
        print(e)
        sys.exit(1)
    return result


## Perform authentication
def CreateAuthorization(username, password, appid):
    token = None
    ##create authentication request URL, message and header
    authenMsg = {'CreateServiceToken_Request_1': { 'ApplicationID':appid, 'Username':username,'Password':password }}
    authenURL = 'https://api.trkd.thomsonreuters.com/api/TokenManagement/TokenManagement.svc/REST/Anonymous/TokenManagement_1/CreateServiceToken_1'
    headers = {'content-type': 'application/json;charset=utf-8'}
    print('############### Sending Authentication request message to TRKD ###############')
    authenResult = doSendRequest(authenURL, authenMsg, headers)
    if authenResult and authenResult.status_code == 200:
        print('Authen success')
        print('response status %s'%(authenResult.status_code))
        ##get Token
        token = authenResult.json()['CreateServiceToken_Response_1']['Token']
    
    return token

## Perform Interday request 
def RetrieveInteraday(token, appid):
    ##construct Time Series Interday request message
    ricName = input('Please input Symbol: ')
    interdayRequestMsg = None
    fields = ['OPEN','HIGH','LOW','CLOSE','CLOSEYIELD','VOLUME','BID','ASK'] #change your fields (support these 'OPEN','HIGH','LOW','CLOSE','CLOSEYIELD','VOLUME','BID','ASK' fields only)
    startTime = '2015-09-22T00:00:00' #change your StartTime
    endtime = '2016-09-22T23:59:00'  #change your EndTime
    #interval = 'DAILY' # change your interval between 'DAILY', 'WEEKLY', 'MONTHLY', 'QUARTERLY' and 'ANNUAL'
    interval = input('Input interested interval (\'DAILY\' or \'WEEKLY\' or \'MONTHLY\' or \'QUARTERLY\' or \'ANNUAL\'): ')
    interdayRequestMsg = {
        'GetInterdayTimeSeries_Request_4':{
            'Field': fields,
            'TrimResponse': True,
            'Symbol': ricName,
            'StartTime':startTime,
            'EndTime':endtime,  
            'Interval':interval,
            'TrimResponse': True,
            'MetaField': ['NAME','QOS','CCY','TZ','TZOFFSET','NAME_LL']
        }
    }
    ##construct Time Series Interday URL and header
    #interdayURL = 'http://api.rkd.reuters.com/api/TimeSeries/TimeSeries.svc/REST/TimeSeries_1/GetInterdayTimeSeries_4'
    interdayURL = 'http://api.trkd.thomsonreuters.com/api/TimeSeries/TimeSeries.svc/REST/TimeSeries_1/GetInterdayTimeSeries_4'
    headers = {'content-type': 'application/json;charset=utf-8' ,'X-Trkd-Auth-ApplicationID': appid, 'X-Trkd-Auth-Token' : token}
    
    print('############### Sending Time Series Interday request message to TRKD ###############')
    interdayResult = doSendRequest(interdayURL, interdayRequestMsg, headers)
    if interdayResult and interdayResult.status_code == 200:
        print('Time Series Interday response message: ')
        print(interdayResult.json())


## ------------------------------------------ Main App ------------------------------------------ ##
if __name__ == '__main__':
    ##Get username, password and applicationid
    username = input('Please input username: ')
    ##use getpass.getpass to hide user inputted password
    password = getpass.getpass(prompt='Please input password: ')
    appid = input('Please input appid: ')

    token = CreateAuthorization(username, password, appid)
    print('Token = %s'%(token))
    ## if authentiacation success, continue subscribing Time Series interday
    if token:
        RetrieveInteraday(token, appid)
