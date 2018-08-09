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
import urllib

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
    if authenResult is not None and authenResult.status_code == 200:
        print('Authen success')
        print('response status %s'%(authenResult.status_code))
        ##get Token
        token = authenResult.json()['CreateServiceToken_Response_1']['Token']
    
    return token

## Perform Chart request 
def RetrieveChart(token, appid):
    ##construct a Chart request message
    ricName = input('Please input Symbol: ')
    chartRequestMsg = {'GetChart_Request_2': {'chartRequest': {
    'TimeSeries': {'TimeSeriesRequest_typehint': ['TimeSeriesRequest'],
                   'TimeSeriesRequest': [{'Symbol': ricName,
                   'Reference': 'd1'}]},
    'Analyses': {'Analysis_typehint': ['Analysis', 'Analysis'],
                 'Analysis': [{'Reference': 'a1',
                 'OHLC': {'Instrument1': {'Reference': 'd1'}}},
                 {'Reference': 'a2',
                 'Vol': {'Instrument1': {'Reference': 'd1'}}}]},
    'StandardTemplate': {
        'Interval': {'CommonType': 'Days', 'Multiplier': '1'},
        'ShowNonTradedPeriods': False,
        'ShowHolidays': False,
        'ShowGaps': True,
        'XAxis': {'Range': {'Fixed': {'First': '2015-09-22T00:00:00',
                  'Last': '2016-09-22T00:00:00'}}, 'Visible': True,
                  'Position': 'Bottom'},
        'Subchart': [{'YAxis': [{
            'Analysis': [{'Reference': 'a1'}],
            'Visible': True,
            'Position': 'Right',
            'Invert': False,
            'Logarithmic': False,
            'Display': {'Mode': 'Automatic'},
            'Range': {'Automatic': ''},
            }], 'Weight': 5.0}, {'YAxis': [{
            'Analysis': [{'Reference': 'a2'}],
            'Visible': True,
            'Position': 'Right',
            'Invert': False,
            'Logarithmic': False,
            'Display': {'Mode': 'Automatic'},
            'Range': {'Automatic': ''},
            }], 'Weight': 2.0}],
        'Title': {'Caption': {'Visible': True, 'Customized': False},
                  'Range': {'Visible': True}},
        'Legend': {
            'Visible': True,
            'Information': 'Long',
            'Layout': 'MultiLine',
            'Position': 'Overlaid',
            },
        'Instrument': 'Symbol',
        'Delimiter': '%',
        'GridLines': 'None',
        'YAxisMarkers': 'None',
        'YAxisTitles': 'All',
        'Brand': 'None',
        },
    'Scheme': {
        'Background': {
            'BackgroundMode': 'Solid',
            'StartColor': {'Named': 'White'},
            'EndColor': {'Named': 'White'},
            'HatchStyle': 'LargeGrid',
            'GradientMode': 'ForwardDiagonal',
            'ImageMode': 'Centered',
            },
        'Border': {'Color': {'RGB': '139;139;155'},
                   'DashStyle': 'Solid', 'Width': 1.0},
        'GridLines': {'Color': {'RGB': '139;139;155'},
                      'DashStyle': 'Dot', 'Width': 1.0},
        'Title': {'Caption': {
            'Color': {'Named': 'Black'},
            'Family': 'Arial',
            'Style': 'Bold',
            'Size': 12.0,
            }, 'Range': {
            'Color': {'Named': 'Black'},
            'Family': 'Arial',
            'Style': 'Regular',
            'Size': 8.25,
            }},
        'Legend': {
            'Color': {'Named': 'Black'},
            'Family': 'Arial',
            'Style': 'Regular',
            'Size': 8.25,
            },
        'XAxis': {'Major': {
            'Color': {'Named': 'Black'},
            'Family': 'Arial',
            'Style': 'Bold',
            'Size': 9.75,
            }, 'Minor': {
            'Color': {'Named': 'Black'},
            'Family': 'Arial',
            'Style': 'Regular',
            'Size': 8.25,
            }},
        'YAxis': {'Major': {
            'Color': {'Named': 'Black'},
            'Family': 'Arial',
            'Style': 'Bold',
            'Size': 9.75,
            }, 'Minor': {
            'Color': {'Named': 'Black'},
            'Family': 'Arial',
            'Style': 'Regular',
            'Size': 8.25,
            }, 'Title': {
            'Color': {'Named': 'Black'},
            'Family': 'Arial',
            'Style': 'Regular',
            'Size': 8.25,
            }},
        'Series': [
            {
                'Color': {'Named': 'Black'},
                'DashStyle': 'Solid',
                'Width': 0.0,
                'FillColor': {'Named': 'Black'},
                'FillStyle': 'Percent20',
                },
            {
                'Color': {'Named': 'Red'},
                'DashStyle': 'Solid',
                'Width': 0.0,
                'FillColor': {'Named': 'Red'},
                'FillStyle': 'Percent20',
                },
            {
                'Color': {'RGB': '62;169;0'},
                'DashStyle': 'Solid',
                'Width': 0.0,
                'FillColor': {'RGB': '62;169;0'},
                'FillStyle': 'Percent20',
                },
            {
                'Color': {'RGB': '156;38;115'},
                'DashStyle': 'Solid',
                'Width': 0.0,
                'FillColor': {'RGB': '156;38;115'},
                'FillStyle': 'Percent20',
                },
            {
                'Color': {'RGB': '255;120;0'},
                'DashStyle': 'Solid',
                'Width': 0.0,
                'FillColor': {'RGB': '255;120;0'},
                'FillStyle': 'Percent20',
                },
            {
                'Color': {'RGB': '25;108;229'},
                'DashStyle': 'Solid',
                'Width': 0.0,
                'FillColor': {'RGB': '25;108;229'},
                'FillStyle': 'Percent20',
                },
            {
                'Color': {'RGB': '60;117;28'},
                'DashStyle': 'Solid',
                'Width': 0.0,
                'FillColor': {'RGB': '60;117;28'},
                'FillStyle': 'Percent20',
                },
            {
                'Color': {'RGB': '230;176;18'},
                'DashStyle': 'Solid',
                'Width': 0.0,
                'FillColor': {'RGB': '230;176;18'},
                'FillStyle': 'Percent20',
                },
            {
                'Color': {'RGB': '0;186;193'},
                'DashStyle': 'Solid',
                'Width': 0.0,
                'FillColor': {'RGB': '0;186;193'},
                'FillStyle': 'Percent20',
                },
            {
                'Color': {'RGB': '255;178;127'},
                'DashStyle': 'Solid',
                'Width': 0.0,
                'FillColor': {'RGB': '255;178;127'},
                'FillStyle': 'Percent20',
                },
            {
                'Color': {'RGB': '100;79;190'},
                'DashStyle': 'Solid',
                'Width': 0.0,
                'FillColor': {'RGB': '100;79;190'},
                'FillStyle': 'Percent20',
                },
            {
                'Color': {'RGB': '209;36;33'},
                'DashStyle': 'Solid',
                'Width': 0.0,
                'FillColor': {'RGB': '209;36;33'},
                'FillStyle': 'Percent20',
                },
            {
                'Color': {'RGB': '38;87;135'},
                'DashStyle': 'Solid',
                'Width': 0.0,
                'FillColor': {'RGB': '38;87;135'},
                'FillStyle': 'Percent20',
                },
            {
                'Color': {'RGB': '94;176;176'},
                'DashStyle': 'Solid',
                'Width': 0.0,
                'FillColor': {'RGB': '94;176;176'},
                'FillStyle': 'Percent20',
                },
            ],
        'LevelLine': [{'Color': {'RGB': '0;0;153'}, 'DashStyle': 'Solid'
                      , 'Width': 1.0}, {'Color': {'RGB': '120;120;120'
                      }, 'DashStyle': 'Solid', 'Width': 1.0}],
        },
    'ImageType': 'PNG',
    'Width': 500,
    'Height': 400,
    'Culture': 'en-US',
    'ReturnPrivateNetworkURL': False,
    }}}
    ##construct Chart URL and header
    chartURL = 'http://api.trkd.thomsonreuters.com/api/Charts/Charts.svc/REST/Charts_1/GetChart_2'
    headers = {'content-type': 'application/json;charset=utf-8' ,'X-Trkd-Auth-ApplicationID': appid, 'X-Trkd-Auth-Token' : token}
    
    print('############### Sending Chart request message to TRKD ###############')
    chartResult = doSendRequest(chartURL, chartRequestMsg,headers)
    if chartResult is not None and chartResult.status_code == 200:
        print('Time Series Interday response message: ')
        print(chartResult.json())
        ##print returned server, tag and image url
        server = chartResult.json()['GetChart_Response_2']['ChartImageResult']['Server']
        print('\nServer: %s'%(server))
        tag = chartResult.json()['GetChart_Response_2']['ChartImageResult']['Tag']
        print('Tag: %s'%(tag))
        imageUrl = chartResult.json()['GetChart_Response_2']['ChartImageResult']['Url']
        print('Url: %s'%(imageUrl))
        return imageUrl

##download image url from the TRKD Chart service as chart.png
def downloadChartImage(chartURL):
    ##create header
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    print('\nDownlading chart.png file from %s'%(chartURL))
    ##download image using Python3 urllib
    downloadResult = urllib.request.Request(chartURL, headers=headers)
    imgData = urllib.request.urlopen(downloadResult).read()
    ##write file
    fileName = './chart.png'
    with open(fileName,'wb') as outfile:
        outfile.write(imgData)
        print('save chart.png file complete')



## ------------------------------------------ Main App ------------------------------------------ ##

if __name__ == '__main__':
    ##Get username, password and applicationid
    username = input('Please input username: ')
    ##use getpass.getpass to hide user inputted password
    password = getpass.getpass(prompt='Please input password: ')
    appid = input('Please input appid: ')   

    token = CreateAuthorization(username,password,appid)
    print('Token = %s'%(token))
    ## if authentiacation success, continue subscribing Chart
    if token:
        chartURL = RetrieveChart(token,appid)
        ## if chart request success, continue downloading Chart image
        if chartURL:
            print('############### Downloading Chart file from TRKD ###############')
            downloadChartImage(chartURL)
            