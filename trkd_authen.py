'''
The RKD API sample code is provided for informational purposes only 
and without knowledge or assumptions of the end users development environment. 
We offer this code to provide developers practical and useful guidance while developing their own code. 
However, we do not offer support and troubleshooting of issues that are related to the use of this code 
in a particular environment; it is offered solely as sample code for guidance. 
Please see the Refinitiv Knowledge Direct (RKD) API (formerly known as TRKD API) product page at https://my.refinitiv.com 
for additional information regarding the RKD API.'''

import sys
import json
import getpass
import requests


if __name__ == '__main__':
    # Get username, password and applicationid
    username = input('Please input username: ')
    # use getpass.getpass to hide user inputted password
    password = getpass.getpass(prompt='Please input password: ')
    appid = input('Please input appid: ')
    print('############### Sending Authentication request message to TRKD ###############')

    # create authentication request URL, message and header
    authenMsg = {'CreateServiceToken_Request_1': {
        'ApplicationID': appid, 'Username': username, 'Password': password}}
    authenURL = 'https://api.trkd.thomsonreuters.com/api/TokenManagement/TokenManagement.svc/REST/Anonymous/TokenManagement_1/CreateServiceToken_1'
    headers = {'content-type': 'application/json;charset=utf-8'}

    try:
        # send request
        result = requests.post(
            authenURL, data=json.dumps(authenMsg), headers=headers)
        # request success
        if result.status_code == 200:
            print('Request success')
            print('response status %s' % (result.status_code))
            # get Token
            token = result.json()['CreateServiceToken_Response_1']['Token']
            print('Token: %s' % (token))
            # get expiraion
            expire = result.json()[
                'CreateServiceToken_Response_1']['Expiration']
            print('Expire: %s' % (expire))
        # handle error
        else:
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
