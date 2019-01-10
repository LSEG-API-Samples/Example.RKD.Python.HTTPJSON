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
import time
import getopt
import socket
import websocket
import threading
from threading import Thread, Event

from datetime import datetime, timezone, timedelta
import dateutil.parser


# Global Default Variables
ws_address = 'wss://streaming.trkd.thomsonreuters.com/WebSocket/'
trkd_authen_address = 'https://api.trkd.thomsonreuters.com/api/TokenManagement/TokenManagement.svc/REST/Anonymous/TokenManagement_1/CreateServiceToken_1'
ws_protocol = 'tr_json2'
position = socket.gethostbyname(socket.gethostname())

# Global Variables
web_socket_app = None
web_socket_open = False
username = None
password = None
appid = None
token = None
expiration = None
logged_in = False

ric_name = 'EUR='

expire_time_in_seconds = None
time_before_expire_in_seconds = 15 * 60 # 15 Minutes to Seconds

## ------------------------------------------ TRKD HTTP REST functions ------------------------------------------ ##

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
    expiration = None
    ##create authentication request URL, message and header
    authenMsg = {'CreateServiceToken_Request_1': { 'ApplicationID':appid, 'Username':username,'Password':password }}
    headers = {'content-type': 'application/json;charset=utf-8'}
    print('############### Sending Authentication request message to TRKD ###############')
    authenResult = doSendRequest(trkd_authen_address, authenMsg, headers)
    if authenResult and authenResult.status_code == 200:
        print('Authentication success')
        print('response status %s'%(authenResult.status_code))
        print('Authentication response %s'%json.dumps(authenResult.json(), sort_keys=True, indent=2, separators=(',', ':')))
        ##get Token
        token = authenResult.json()['CreateServiceToken_Response_1']['Token']
        expiration = authenResult.json()['CreateServiceToken_Response_1']['Expiration'] # Expiration time of this session in UTC 

        ## Calcuate Expiration time
        expire_datetime_utc = dateutil.parser.parse(expiration) ## Parse incoming Expiration to Python datetime object (UTC)
        utc_time_now = datetime.now(timezone.utc) ## Get current machine datetime in UTC 

        time_difference = expire_datetime_utc - utc_time_now ## Get time different between now and expiration time value 
        time_difference_in_seconds = int(round(time_difference / timedelta(seconds=1))) ## convert it to second as a round int

    return token, expiration, time_difference_in_seconds

## ------------------------------------------ TRKD WebSocket functions ------------------------------------------ ##

def process_message(message_json):
    """ Parse at high level and output JSON of message """
    message_type = message_json['Type']

    if message_type == "Refresh":
        if 'Domain' in message_json:
            message_domain = message_json['Domain']
            if message_domain == "Login":
                process_login_response(message_json)
    elif message_type == "Ping":
        pong_json = { 'Type':'Pong' }
        web_socket_app.send(json.dumps(pong_json))
        print("SENT:")
        print(json.dumps(pong_json, sort_keys=True, indent=2, separators=(',', ':')))


def process_login_response(message_json):
    """ Send item request """
    global logged_in

    logged_in = True
    send_market_price_request(ric_name)


def send_market_price_request(ric_name):
    """ Create and send simple Market Price request """
    mp_req_json = {
        'ID': 2,
        'Key': {
            'Name': ric_name,
        },
    }
    web_socket_app.send(json.dumps(mp_req_json))
    print("SENT:")
    print(json.dumps(mp_req_json, sort_keys=True, indent=2, separators=(',', ':')))


def send_login_request(is_refresh_token=False):
    """ Generate a login request from command line data (or defaults) and send """
    login_json = {
        'ID': 1,
        'Domain': 'Login',
        'Key': {
            'Name': '',
            'NameType': 'AuthnToken',
            'Elements': {
                'ApplicationId': '',
                'Position': '',
                'AuthenticationToken': ''
            }
        }
    }

    login_json['Key']['Name'] = username
    login_json['Key']['Elements']['ApplicationId'] = appid
    login_json['Key']['Elements']['Position'] = position
    login_json['Key']['Elements']['AuthenticationToken'] = token

    # If the token is a refresh token, this is not our first login attempt.
    if is_refresh_token:
        login_json['Refresh'] = False

    web_socket_app.send(json.dumps(login_json))
    print("SENT:")
    print(json.dumps(login_json, sort_keys=True, indent=2, separators=(',', ':')))


def on_message(_, message):
    """ Called when message received, parse message into JSON for processing """
    print("RECEIVED: ")
    message_json = json.loads(message)
    print(json.dumps(message_json, sort_keys=True, indent=2, separators=(',', ':')))

    for singleMsg in message_json:
        process_message(singleMsg)


def on_error(__file__, error):
    """ Called when websocket error has occurred """
    print(error)


def on_close(_):
    """ Called when websocket is closed """
    global web_socket_open
    print("WebSocket Closed")
    web_socket_open = False


def on_open(_):
    """ Called when handshake is complete and websocket is open, send login """

    print("WebSocket successfully connected!")
    global web_socket_open
    web_socket_open = True
    send_login_request(is_refresh_token=False)

## ------------------------------------------ Main App ------------------------------------------ ##

if __name__ == '__main__':
    ## Get username, password and applicationid
    username = input('Please input username: ')
    ## use getpass.getpass to hide user inputted password
    password = getpass.getpass(prompt='Please input password: ')
    appid = input('Please input appid: ')

    token, expiration, expire_time_in_seconds = CreateAuthorization(username,password,appid)
    print('Token = %s'%(token))
    print('Expiration  = %s'%(expiration))
    print('Expiration in next = %d seconds'%(expire_time_in_seconds))
    ## if authentiacation success, continue subscribing Quote
    if token and expiration:
        print('Do WS here')
        # doWebSocketConnection(username, appid, token)
        print("Connecting to WebSocket " + ws_address + " ...")
        web_socket_app = websocket.WebSocketApp(ws_address, header=['User-Agent: Python'],
            on_message=on_message,
            on_error=on_error,
            on_close=on_close,
            subprotocols=[ws_protocol])
        web_socket_app.on_open = on_open
        # for test

        # expire_time_in_seconds = 120
        # time_before_expire_in_seconds = 15
        # Event loop
        wst = threading.Thread(target=web_socket_app.run_forever)
        wst.start()

        try:
            while True:
                #time.sleep(1)
                if (expire_time_in_seconds > time_before_expire_in_seconds):
                    time.sleep(expire_time_in_seconds-time_before_expire_in_seconds)
                else:
                    # failt the refresh sine value too small
                    sys.exit(1)
                token, expiration, expire_time_in_seconds = CreateAuthorization(username,password,appid)
                print('new Token = %s'%(token))
                print('new Expiration  = %s'%(expiration))
                print('new Expiration in next = %d seconds'%(expire_time_in_seconds))
                if not token:
                    sys.exit(1)
                if logged_in:
                    print('############### Re-new Authentication to TRKD ###############')
                    send_login_request(is_refresh_token=True)
        except KeyboardInterrupt:
            web_socket_app.close()