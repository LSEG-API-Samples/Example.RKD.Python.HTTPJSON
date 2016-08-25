import zeep

username = 'trcsmnldauki@thomsonreuters.com'
appid = 'rkdapi'
password = 'Welcome75'

authen_wsdl = 'http://api.rkd.reuters.com/schemas/wsdl/TokenManagement_1_HttpsAndAnonymous.wsdl'
quote_wsdl = 'http://api.rkd.reuters.com/schemas/wsdl/Quotes_1_HttpAndRKDToken.wsdl'
client = zeep.Client(wsdl=authen_wsdl)

authen_request = client.get_type
