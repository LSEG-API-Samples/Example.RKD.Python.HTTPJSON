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
                #print('Error: %s'%(result.json()))
                print('Error: %s' % (json.dumps(result.json(),
                                                sort_keys=True, indent=2, separators=(',', ':'))))
            result.raise_for_status()
        # if result.status_code == 500:
            #print('Request fail')
            #print('response status %s' % result.status_code)
            #print('Error: %s' % result.json())
            # sys.exit(1)
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

# Perform Quote request


def RetrieveQuotes(token, appid):

    ricName = input('Please input Symbol: ')
    fieldFiltering = input('Subscribe all Field? (Yes|No)')
    quoteRequestMsg = None
    fieldsName = 'CF_LAST:CF_HIGH:CF_LOW:CF_BID:CF_ASK:CF_YIELD:CF_SOURCE:CF_SRC_PAGE:CF_LOTSIZE:CF_DATE:CF_TIME:CF_TICK:CF_NETCHNG:CF_EXCHNG:CF_VOLUME:CF_CLOSE:CF_OPEN:CF_NAME:CF_CURRENCY'
    if fieldFiltering == 'Yes':
        # Request all Fields
        quoteRequestMsg = \
            {'RetrieveItem_Request_3': {'TrimResponse': False,
                                        'ItemRequest': [{'RequestKey': [{'Name': ricName, 'NameType': 'RIC'}], 'Scope': 'All',
                                                         'ProvideChainLinks': True}]}}
    elif fieldFiltering == 'No':
        # Request specific Fields
        fieldsName = input(
            'Input interested Field Name in the following format (BID:ASK:TRDPRC_1)')
        quoteRequestMsg = \
            {'RetrieveItem_Request_3': {'TrimResponse': False,
                                        'ItemRequest': [{
                                            'RequestKey': [{'Name': ricName, 'NameType': 'RIC'}],
                                            'Fields': fieldsName,
                                            'Scope': 'List',
                                            'ProvideChainLinks': True
                                        }]}}

    quoteURL = 'https://api.rkd.refinitiv.com/api/Quotes/Quotes.svc/REST/Quotes_1/RetrieveItem_3'
    headers = {'content-type': 'application/json;charset=utf-8',
               'X-Trkd-Auth-ApplicationID': appid, 'X-Trkd-Auth-Token': token}

    print('############### Sending Quote request message to RKD ###############')
    quoteResult = doSendRequest(quoteURL, quoteRequestMsg, headers)
    if quoteResult and quoteResult.status_code == 200:
        print('Quote response message: ')
        # print(quoteResult.json())
        print(json.dumps(quoteResult.json(), sort_keys=True,
                         indent=2, separators=(',', ':')))


## ------------------------------------------ Main App ------------------------------------------ ##

if __name__ == '__main__':
    ## Get username, password and applicationid
    username = input('Please input username: ')
    ## Use getpass.getpass to hide user inputted password
    password = getpass.getpass(prompt='Please input password: ')
    appid = input('Please input appid: ')   


    token = CreateAuthorization(username, password, appid)
    print('Token = %s' % (token))
    # if authentication success, continue subscribing Quote
    if token:
        RetrieveQuotes(token, appid)
