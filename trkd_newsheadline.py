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

## Perform News Headline request 
def RetrieveNewsHeadline(token, appid):
    ##construct news headline URL and header
    newsURL = 'https://api.trkd.thomsonreuters.com/api/News/News.svc/REST/News_1/RetrieveHeadlineML_1'
    headers = {'content-type': 'application/json;charset=utf-8' ,'X-Trkd-Auth-ApplicationID': appid, 'X-Trkd-Auth-Token' : token}
    ##construct a news headline request message
    ricName = raw_input('Please input Symbol: ')
    newsRequestMsg = {'RetrieveHeadlineML_Request_1': {
        'HeadlineMLRequest':{
            'MaxCount':25,
            'Filter':[
                {
                    'MetaDataConstraint':{
                        'class': 'any',
                        'Value': {
                            'Text' : ricName
                        }
                    }
                }
            ]
        }
    }}

    print '############### Sending News Headline request message to TRKD ###############'
    newsResult = doSendRequest(newsURL, newsRequestMsg,headers)
    if newsResult is not None and newsResult.status_code == 200:
        print 'News Headline response message: '
        print newsResult.json()



## ------------------------------------------ Main App ------------------------------------------ ##
##Get username, password and applicationid
username = raw_input('Please input username: ')
##use getpass.getpass to hide user inputted password
password = getpass.getpass(prompt='Please input password: ')
appid = raw_input('Please input appid: ')


token = CreateAuthorization(username,password,appid)
print 'Token = %s'%(token)

## if authentiacation success, continue subscribing News Headline
if token is not None:
    RetrieveNewsHeadline(token,appid)

