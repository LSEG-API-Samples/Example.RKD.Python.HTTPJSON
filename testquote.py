import requests
import json

username = 'trcsmnldauki@thomsonreuters.com'
appid = 'rkdapi'
password = 'Welcome75'

authenURL = 'https://api.trkd.thomsonreuters.com/api/TokenManagement/TokenManagement.svc/REST/Anonymous/TokenManagement_1/CreateServiceToken_1'

authenMsg = {'CreateServiceToken_Request_1': { 'ApplicationID':appid, 'Username':username,'Password':password }}
headers = {'content-type': 'application/json'}

result = requests.post(authenURL, data = json.dumps(authenMsg), headers=headers)
print 'response status %s'%(result.status_code)
print 'response header %s'%(result.headers)
print 'response raw data = %s'%(result.json())

token = result.json()['CreateServiceToken_Response_1']['Token']


quoteURL = 'https://api.trkd.thomsonreuters.com/api/Quotes/Quotes.svc/REST/Quotes_1/RetrieveItem_3'

headers = {'content-type': 'application/json;charset=utf-8' ,'X-Trkd-Auth-ApplicationID': appid, 'X-Trkd-Auth-Token' : token}

quoteRequestMsg = {
'RetrieveItem_Request_3': {
    'TrimResponse': False,
    'ItemRequest': [
      {
        'Fields': 'CF_LAST:CF_HIGH:CF_LOW:CF_BID:CF_ASK:CF_YIELD:CF_DATE:CF_TIME:CF_VOLUME:CF_CLOSE:CF_OPEN:CF_NAME',
        'RequestKey': [
          {
            'Name': 'VOD.L',
            'NameType': 'RIC'
          }
        ],
        'Scope': 'List',
        'ProvideChainLinks': True
      }
    ]
  }
}

quoteresult = requests.post(quoteURL, data = json.dumps(quoteRequestMsg), headers=headers)
print quoteresult.json()
