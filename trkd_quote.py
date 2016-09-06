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

## Perform authentication
def CreateAuthorization(username, password, appid):
    token = None
    ##create authentication request URL, message and header
    authenMsg = {'CreateServiceToken_Request_1': { 'ApplicationID':appid, 'Username':username,'Password':password }}
    authenURL = 'https://api.trkd.thomsonreuters.com/api/TokenManagement/TokenManagement.svc/REST/Anonymous/TokenManagement_1/CreateServiceToken_1'
    headers = {'content-type': 'application/json;charset=utf-8'}
    print '############### Sending Authentication request message to TRKD ###############'
    try:
        ##send request
        result = requests.post(authenURL, data = json.dumps(authenMsg), headers=headers)
        if result.status_code == 200:
            print 'Authen success'
            print 'response status %s'%(result.status_code)
            ##get Token
            token = result.json()['CreateServiceToken_Response_1']['Token']
        elif result.status_code == 500:
            print 'Request fail'
            print 'response status %s'%(result.status_code)
            print 'Error: %s'%(result.json())
    except requests.exceptions.RequestException as e:
        print 'Exception!!!'
        print e
        sys.exit(1)
    
    return token

## Perform Quote request 
def RetrieveQuotes(token, appid):

    ricName = raw_input('Please input Symbol: ')
    fieldFiltering = raw_input('Subscribe all Field? (Yes|No)')
    quoteRequestMsg = None
    fieldsName = 'CF_LAST:CF_HIGH:CF_LOW:CF_BID:CF_ASK:CF_YIELD:CF_SOURCE:CF_SRC_PAGE:CF_LOTSIZE:CF_DATE:CF_TIME:CF_TICK:CF_NETCHNG:CF_EXCHNG:CF_VOLUME:CF_CLOSE:CF_OPEN:CF_NAME:CF_CURRENCY'
    if fieldFiltering == 'Yes':
        ## Request all Fields
        quoteRequestMsg = \
            {'RetrieveItem_Request_3': {'TrimResponse': False,
             'ItemRequest': [{'RequestKey': [{'Name': ricName, 'NameType': 'RIC'}], 'Scope': 'All',
             'ProvideChainLinks': True}]}}
    elif fieldFiltering == 'No':
        ## Request specific Fields
        fieldsName = raw_input('Input interested Field Name in the following format (BID:ASK:TRDPRC_1)')
        quoteRequestMsg = \
            {'RetrieveItem_Request_3': {'TrimResponse': False,
             'ItemRequest': [{
            'RequestKey': [{'Name': ricName, 'NameType': 'RIC'}],
            'Fields': fieldsName,
            'Scope': 'List',
            'ProvideChainLinks': True,
            }]}}

    quoteURL = 'https://api.trkd.thomsonreuters.com/api/Quotes/Quotes.svc/REST/Quotes_1/RetrieveItem_3'
    headers = {'content-type': 'application/json;charset=utf-8' ,'X-Trkd-Auth-ApplicationID': appid, 'X-Trkd-Auth-Token' : token}
    
    print '############### Sending Quote request message to TRKD ###############'
    try:
        ##send request
        quoteresult = requests.post(quoteURL, data = json.dumps(quoteRequestMsg), headers=headers)
        if quoteresult.status_code == 200:
            print 'Quote request success'
            print quoteresult.json()
        else:
            print 'Request fail'
            print 'response status %s'%(quoteresult.status_code)
            print 'Error: %s'%(quoteresult.json())

    except requests.exceptions.RequestException as e:
        print 'Exception!!!'
        print e 
        sys.exit(1)


## ------------------------------------------ Main App ------------------------------------------ ##
##Get username, password and applicationid
username = raw_input('Please input username: ')
##use getpass.getpass to hide user inputted password
password = getpass.getpass(prompt='Please input password: ')
appid = raw_input('Please input appid: ')

token = CreateAuthorization(username,password,appid)
print 'Token = %s'%(token)

RetrieveQuotes(token,appid)


             
             
             
             
    
        
        
        

    
   
    