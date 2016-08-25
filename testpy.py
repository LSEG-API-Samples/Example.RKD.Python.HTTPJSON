import requests
import json

username = 'trcsmnldauki@thomsonreuters.com'
appid = 'rkdapi'
password = 'Welcome75'

authenURL = 'https://api.trkd.thomsonreuters.com/api/TokenManagement/TokenManagement.svc/REST/Anonymous/TokenManagement_1/CreateServiceToken_1'

authenMsg = {'CreateServiceToken_Request_1': { 'ApplicationID':appid, 'Username':username,'Password':password }}
headers = {'content-type': 'application/json;charset=utf-8'}

result = requests.post(authenURL, data = json.dumps(authenMsg), headers=headers)
print 'response status %s'%(result.status_code)
print 'response header %s'%(result.headers)
print 'response raw data = %s'%(result.json())

token = result.json()['CreateServiceToken_Response_1']['Token']
print token
expire = result.json()['CreateServiceToken_Response_1']['Expiration']

