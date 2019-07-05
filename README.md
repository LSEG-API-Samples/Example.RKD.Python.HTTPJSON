# TRKD HTTP JSON with Python Example
## Overview
The [Thomson Reuters Knowledge Direct (TRKD) API](https://developers.thomsonreuters.com/thomson-reuters-knowledge-direct-trkd) integrates into your website, trading platform, company intranet/extranet, advisory portal and mobile applications to provide up-to-date financial market data, news and analytics and powerful investment tools.

TRKD offers a wide range of Refinitiv' information and services delivered in a request-response scenario via web services using today's industry standard protocols (SOAP/XML and REST/JSON). Connectivity can be via HTTP and HTTPS, over the Internet or Delivery Direct. All data are snapshot (non-streaming) data.

This is an example project that shows how to implement TRKD HTTP JSON client and TRKD Streaming client with Python programming lanugage. The project example are in both console and Jupyter Notebook applications.

*Note:* The Jupyter Notebook example does not contain all the same TRKD services service as console example yet. [TBD]

## Application Files
This project contains the following example scripts for each TRKD services
- trkd_authen.py: An example application that shows how to authenticate with TRKD service
- trkd_quote.py: An example application that shows how to subscribe (all fields and specific fields) the Quote data from TRKD service
- trkd_newsheadline.py: An example application that shows how to subscribe the News Headline data from TRKD service
- trkd_newsstory.py: An example application that shows how to subscribe the News Story data from TRKD service
- trkd_intraday.py: An example application that shows how to subscribe the Intraday Time-series data from TRKD service
- trkd_interday.py: An example application that shows how to subscribe the Interday Time-series data from TRKD service
- trkd_onlinereport.py: An example application that shows how to subscribe the Online Report data from TRKD service
- trkd_chart.py: An example application that shows how to subscribe and download the Chart image data from TRKD service
- trkd_wsstreaming.py: An example application that show how to subscribe the Quote data from TRKD Streming service via a WebSocket connection
- notebook folder:
	- *notebook/trkd_authentication.ipynb*: A Jupyter Notebook TRKD Authentication service example
- requestments.txt: A requirement file contains a list of required libraries for HTTP JSON and WebSocket connections. 
- docs\TRKD_REST_with_Python.docx: A document that describes the trkd_authen.py and trkd_quote.py applications

All source code and scripts are provided under the Apache 2.0 license. Thye are provided AS IS with no warranty or guarantee of fit for purpose. See the project's LICENSE.md for details. 

## Prerequisite
The following softwares are required to use this script
- TRKD API credentials. Please reach out to your Refinitiv sales associate to acquire TRKD access credentials.
- Python 3 
- The [requests](http://docs.python-requests.org/en/master/) library
- The [websocket-client](https://pypi.org/project/websocket-client/) library (*version 0.49 or greater*, for trkd_wsstreaming.py application only)
- The [python-dateutil](https://pypi.org/project/python-dateutil/) library (for trkd_wsstreaming.py application only)
- [Jupyter Notebook](https://jupyter.org/) runtime (for the Notebook example application)

All scripts support Python 3 and not compatible with Python 2.

*Note:* 
- You can install Jupyter Notebook on your local machine and then test the example on the machine. The alternate choice is a free Jupyter Notebook on cloud environment such as [Azure Notebook](https://notebooks.azure.com/) provided by Microsoft. You can find more details from [this tutorial](https://docs.microsoft.com/en-us/azure/notebooks/tutorial-create-run-jupyter-notebook). If you are not familiar with Jupyter Notebook, the following [tutorial](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook) created by DataCamp may help.

## How to run the script
Run the script via the command line (or shell)
```
$>python <application>.py
```

## Optional - How to install requests
The best way is via the pip package management tool
1. export <Python_folder>\Scripts to your OS PATH environment
2. call pip command to install requests
	```
	$>pip install -r requestments.txt
	```
3. If you are behind proxy, set the proxy first
	```
	export https_proxy="http://<proxy.server>:<port>"
	$>pip install -r requestments.txt
	```

*Note*: If you aim to use only TRKD HTTP JSON services, you can just install requests library via a ```pip install requests``` command.

## References
For further details, please check out the following resources:
* [Thomson Reuters Knowledge Direct API page](https://developers.thomsonreuters.com/thomson-reuters-knowledge-direct-trkd) on the [Thomson Reuters Developer Community](https://developers.thomsonreuters.com/) web site.
* [Thomson Reuters Knowledge Direct API Catalog](https://www.trkd.thomsonreuters.com/SupportSite/RequestBuilder/requestbuilder.aspx) web site.
* [Elektron WebSocket API](https://developers.thomsonreuters.com/websocket-api) page on the [Thomson Reuters Developer Community](https://developers.thomsonreuters.com/) web site.

## Release Note
- Version 1: 6 Sep 2016
    - trkd_authen.py.
	- trkd_quote.py.
- Version 1.0.1: 7 Sep 2016
	- trkd_newsheadline.py.
	- changed code structure to separate call http request
- Version 1.0.2: 19 Sep 2016
	- trkd_newsstory.py.
- version 1.0.3: 22 Sep 2016
	- trkd_intraday.py.
	- trkd_interday.py.
	- trkd_onlinereport.py.
	- trkd_chart.py.
- version 1.0.4: 28 Oct 2016
	- docs\TRKD_REST_with_Python.docx.
	- revise some code.
- version 1.0.5: 27 Apr 2017
	- revies README.md to support markdown.
- version 1.0.6: 3 May 2017
	- revies README.md.
	- modify trkd_authen.py.
	- modify trkd_quote.py.
- version 1.0.7: 9 May 2017
	- revise README.md.
	- modify the rest of application files.
- version 1.0.7: 31 Aug 2017
	- revise README.md
- version 1.0.8: 04 Sep 2017
	- Port all scripts to support Python 3.
	- Fix the issue that some scripts still send request message to the old REST endpoint.
- version 1.0.9: 26 Jan 2018
	- Add debug log for checking outgoing message (disabled by default).
- version 1.0.10: 9 Aug 2018
	- remove all ```is not None``` statements and make them a bit more **Pythonic**.
- version 1.0.11: January 2019
	- Add trkd_wsstreaming.py application for TRKD Streaming service.
	- Add License.md file
- version 1.0.12: March 2019
	- Change all scripts to print JSON message in beauty format.
- version 1.5: July 2019
	- Add TRKD Authentication Jupyter Notebook.
