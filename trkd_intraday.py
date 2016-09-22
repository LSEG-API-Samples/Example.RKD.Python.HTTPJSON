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


def doSendRequest(url, requestMsg, headers):
    result = None
    try:
        ##send request
        result = requests.post(url, data=json.dumps(requestMsg), headers=headers)
        if result.status_code == 500:
            print 'Request fail'
            print 'response status %s' % result.status_code
            print 'Error: %s' % result.json()
            sys.exit(1)
    except requests.exceptions.RequestException, e:
        print 'Exception!!!'
        print e
        sys.exit(1)
    return result


## Perform authentication
def CreateAuthorization(username, password, appid):
    token = None
    ##create authentication request URL, message and header
    authenMsg = {'CreateServiceToken_Request_1': { 'ApplicationID':appid, 'Username':username,'Password':password }}
    authenURL = 'https://api.trkd.thomsonreuters.com/api/TokenManagement/TokenManagement.svc/REST/Anonymous/TokenManagement_1/CreateServiceToken_1'
    headers = {'content-type': 'application/json;charset=utf-8'}
    print '############### Sending Authentication request message to TRKD ###############'
    authenResult = doSendRequest(authenURL, authenMsg, headers)
    if authenResult is not None and authenResult.status_code == 200:
        print 'Authen success'
        print 'response status %s'%(authenResult.status_code)
        ##get Token
        token = authenResult.json()['CreateServiceToken_Response_1']['Token']
    
    return token

## Perform Quote request 
def RetrieveIntraday(token, appid):

    ricName = raw_input('Please input Symbol: ')
    intradayRequestMsg = None
    fields = ['OPEN','HIGH','LOW','CLOSE','CLOSEYIELD','VOLUME','BID','ASK'] #change your fields (support these 'OPEN','HIGH','LOW','CLOSE','CLOSEYIELD','VOLUME','BID','ASK' fields only)
    startTime = '2016-09-12T00:00:00' #change your StartTime
    endtime = '2016-09-19T23:59:00'  #change your EndTime
    intradayRequestMsg = {
        'GetIntradayTimeSeries_Request_4':{
            'Field': fields,
            'TrimResponse': True,
            'Symbol': ricName,
            'StartTime':startTime,
            'EndTime':endtime,  
            'Interval':'MINUTE',
            'TrimResponse': True,
            'MetaField': ['NAME','QOS','CCY','TZ','TZOFFSET','NAME_LL']
        }
    }

    intradayURL = 'http://api.rkd.reuters.com/api/TimeSeries/TimeSeries.svc/REST/TimeSeries_1/GetIntradayTimeSeries_4'
    headers = {'content-type': 'application/json;charset=utf-8' ,'X-Trkd-Auth-ApplicationID': appid, 'X-Trkd-Auth-Token' : token}
    
    print '############### Sending Time Series Intraday request message to TRKD ###############'
    intradayResult = doSendRequest(intradayURL, intradayRequestMsg,headers)
    if intradayResult is not None and intradayResult.status_code == 200:
        print 'Time Series Intraday response message: '
        print intradayResult.json()


## ------------------------------------------ Main App ------------------------------------------ ##
##Get username, password and applicationid
username = raw_input('Please input username: ')
##use getpass.getpass to hide user inputted password
password = getpass.getpass(prompt='Please input password: ')
appid = raw_input('Please input appid: ')


token = CreateAuthorization(username,password,appid)
print 'Token = %s'%(token)
## if authentiacation success, continue subscribing Time Series intraday
if token is not None:
    RetrieveIntraday(token,appid)


             
             
             
             
    
        
        
        

    
   
    