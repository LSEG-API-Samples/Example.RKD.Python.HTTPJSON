# RKD HTTP JSON with Python Examples
- version: 1.6.0
- Last update: Mar 2022
- Environment: Windows, Linux
- Compiler: Python
- Prerequisite: [Demo prerequisite](#prerequisite)

Example Code Disclaimer:
ALL EXAMPLE CODE IS PROVIDED ON AN “AS IS” AND “AS AVAILABLE” BASIS FOR ILLUSTRATIVE PURPOSES ONLY. REFINITIV MAKES NO REPRESENTATIONS OR WARRANTIES OF ANY KIND, EXPRESS OR IMPLIED, AS TO THE OPERATION OF THE EXAMPLE CODE, OR THE INFORMATION, CONTENT, OR MATERIALS USED IN CONNECTION WITH THE EXAMPLE CODE. YOU EXPRESSLY AGREE THAT YOUR USE OF THE EXAMPLE CODE IS AT YOUR SOLE RISK.

## <a id="overview"></a>Overview
The [Refinitiv Knowledge Direct (RKD) API](https://developers.refinitiv.com/en/api-catalog/refinitiv-knowledge-direct/refinitiv-knowledge-direct-api-rkd-api) (formerly known as TRKD API) integrates into your website, trading platform, company intranet/extranet, advisory portal and mobile applications to provide up-to-date financial market data, news and analytics and powerful investment tools.

RKD offers a wide range of Refinitiv' information and services delivered in a request-response scenario via web services using today's industry standard protocols (SOAP/XML and REST/JSON). Connectivity can be via HTTP and HTTPS, over the Internet or Delivery Direct. All data are snapshot (non-streaming) data.

This is an example project that shows how to implement RKD HTTP JSON client and RKD Streaming client with Python programming language. The project example are in both console and Jupyter Notebook applications.

*Note:* The Jupyter Notebook example does not contain all the same RKD services service as console examples yet. [TBD]

## <a id="project_files"></a>Application Files
This project contains the following example scripts for each RKD services
- trkd_authen.py: An example application that shows how to authenticate with RKD service
- trkd_quote.py: An example application that shows how to subscribe (all fields and specific fields) the Quote data from RKD service
- trkd_newsheadline.py: An example application that shows how to subscribe the News Headline data from RKD service
- trkd_newsstory.py: An example application that shows how to subscribe the News Story data from RKD service
- trkd_intraday.py: An example application that shows how to subscribe the Intraday Time-series data from RKD service
- trkd_interday.py: An example application that shows how to subscribe the Interday Time-series data from RKD service
- trkd_onlinereport.py: An example application that shows how to subscribe the Online Report data from RKD service
- trkd_chart.py: An example application that shows how to subscribe and download the Chart image data from RKD service
- trkd_wsstreaming.py: An example application that show how to subscribe the Quote data from RKD Streaming service via a WebSocket connection
- notebook folder:
	- *notebook/trkd_authentication.ipynb*: A Jupyter Notebook RKD Authentication service example
	- *notebook/trkd_timeseries_interday.ipynb*: A Jupyter Notebook RKD Time-Series Interday service example
	- *notebook/trkd_timeseries_intraday.ipynb*: A Jupyter Notebook RKD Time-Series Intraday service example
- requestments.txt: A requirement file contains a list of required libraries for HTTP JSON and WebSocket connections. 

All source code and scripts are provided under the Apache 2.0 license. They are provided AS IS with no warranty or guarantee of fit for purpose. See the project's LICENSE.md for details. 

## <a id="prerequisite"></a>Prerequisite
The following softwares are required to use this script
- RKD API credentials. Please reach out to your Refinitiv representative to acquire RKD access credentials.
- Python [Anaconda](https://www.anaconda.com/distribution/) or [MiniConda](https://docs.conda.io/en/latest/miniconda.html) distribution/package manager.
- The [JupyterLab](https://jupyter.org/) runtime (for the Notebook example application)

All scripts support Python 3 only and not compatible with Python 2.

*Note:* 
- You can install Jupyter Notebook on your local machine and then test the example on the machine. The alternate choice is a free Jupyter Notebook on cloud environment such as [Azure Notebook](https://notebooks.azure.com/) provided by Microsoft. You can find more details from [this tutorial](https://docs.microsoft.com/en-us/azure/notebooks/tutorial-create-run-jupyter-notebook). If you are not familiar with Jupyter Notebook, the following [tutorial](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook) created by DataCamp may help.


### <a id="python_example_run"></a>How to run the Python Console examples

1. Open Anaconda Prompt and go to the project's Python folder
2. Run the following command in the Anaconda Prompt application to create a Conda environment named *RKD_Python* for the project.
    ```
    (base) $>conda create --name RKD_Python python=3.9
    ```
3. Once the environment is created, activate a Conda environment named ```RKD_Python``` with this command in Anaconda Prompt.
    ```
    (base) $>conda activate RKD_Python
    ```
4. Run the following command to the dependencies in the *RKD_Python* environment with a **requirements.txt** file.
    ```
    (RKD_Python) $>pip install -r requirements.txt
    ```
5. Once the dependencies installation process success, Go to the project's Python folder. and create a file name ```.env``` with the following content.
    ```
	#RKD Access Credentials
    RKD_USERNAME=<RKD Username>
	RKD_PASSWORD=<RKD Password>
	RKD_APP_ID=<RKD App ID>
    ```
6. Run the script via the command line (or shell)
    ```
    (RKD_Python) $>python <application>.py
    ```

### <a id="python_example_run"></a>How to run the Python Notebook examples

1. Open Anaconda Prompt and go to the project's Python folder
2. Run the following command in the Anaconda Prompt application to create a Conda environment named *RKD_Python_Notebook* for the project.
    ```
    (base) $>conda create --name RKD_Python_Notebook python=3.9
    ```
3. Once the environment is created, activate a Conda environment named ```RKD_Python_Notebook``` with this command in Anaconda Prompt.
    ```
    (base) $>conda activate RKD_Python_Notebook
    ```
4. Run the following command to the dependencies in the *RKD_Python_Notebook* environment with a **requirements-notebook.txt** file.
    ```
    (RKD_Python_Notebook) $>pip install -r requirements-notebook.txt
    ```
5. Once the dependencies installation process success, Go to the project's notebook folder. and create a file name ```.env``` with the following content.
    ```
	#RKD Access Credentials
    RKD_USERNAME=<RKD Username>
	RKD_PASSWORD=<RKD Password>
	RKD_APP_ID=<RKD App ID>
    ```
6. Run the following command to start the Jupyter Lab application
    ```
    (RKD_Python_Notebook) $>notebook>jupyter lab
    ```

Please follow the [JupyterLab installation guide](https://jupyter.org/install) page.

## <a id="rdp"></a>RDP and Refinitiv Real-Time - Optimized

You may consider the strategic [Refinitiv Data Platform (RDP)](https://developers.refinitiv.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-platform-apis) web base APIs platform. RDP APIs give you seamless and holistic access to all of Refinitiv content such as Historical Pricing, Environmental Social and Governance (ESG), News, Research, etc and commingled with your own content, enriching, integrating and distributing the data through a single interface, delivered wherever you need it.  The RDP APIs delivery mechanisms are following:
* Request - Response: RESTful web service (HTTP GET, POST, PUT or DELETE) 
* Alert: delivery is a mechanism to receive asynchronous updates (alerts) to a subscription. 
* Bulks:  deliver substantial payloads, like the end of day pricing data for the whole venue. 
* Streaming: deliver real-time delivery of messages.

Please see [RDP APIs Overview page](https://developers.refinitiv.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-platform-apis) for more detail.

As part of RDP, [Refinitiv Real-Time - Optimized (RTO)](https://developers.refinitiv.com/en/api-catalog/refinitiv-real-time-opnsrc/refinitiv-websocket-api/tutorials#connect-to-refinitiv-real-time-optimized) gives you access to best in class Real Time market data delivered in the cloud.  RTO is a new delivery mechanism for RDP, using the AWS (Amazon Web Services) cloud. Once a connection to RDP is established using RTO, data can be retrieved using [WebSocket API](https://developers.refinitiv.com/en/api-catalog/refinitiv-real-time-opnsrc/refinitiv-websocket-api) (the same as RKD Streaming Service).

Key benefit of the strategic RDP and RTO platform are the Cloud Delivery. The Platform is based on [Amazon AWS](https://aws.amazon.com/), the world class leading Cloud Provider for developers. The RDP and RTO support output for multiple cloud vendors such as AWS, Azure, GCS, etc. for cloud-native or on-premise integration. The RTO servers are hosted in multiple location world-wide which lets the application choose the closest server based on their region for full potential. 

## <a id="references"></a>References
For further details, please check out the following resources:
* [Refinitiv Knowledge Direct API page](https://developers.refinitiv.com/en/api-catalog/refinitiv-knowledge-direct/refinitiv-knowledge-direct-api-rkd-api) on the [Refinitiv Developers Community](https://developers.refinitiv.com/) website.
* [Refinitiv Knowledge Direct API Catalog](https://support-portal.rkd.refinitiv.com/SupportSite/TestApi/Catalog) website.
* [WebSocket API](https://developers.refinitiv.com/websocket-api) page on the [Refinitiv Developers Community](https://developers.refinitiv.com/) website.
* [Refinitiv Data Platform (RDP) APIs page](https://developers.refinitiv.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-platform-apis).
* [Refinitiv Data Platform (RDP) APIs Gateway page](https://apidocs.refinitiv.com/Apps/ApiDocs).

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
	- revise README.md to support markdown.
- version 1.0.6: 3 May 2017
	- revise README.md.
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
	- Add trkd_wsstreaming.py application for RKD Streaming service.
	- Add License.md file
- version 1.0.12: March 2019
	- Change all scripts to print JSON message in beauty format.
- version 1.5: July 2019
	- Add RKD Authentication Jupyter Notebook.
- version 1.5.1: July 2019
	- Add RKD Interday and Intraday Jupyter Notebooks.
- version 1.5.2: October 2019
	- Update RKD Interday and Intraday services operations.
- version 1.5.3: May 2020
	- Update RDP and Refinitiv Real-Time - Optimized information.
- version 1.5.4: June 2020
	- Update API name and information.
	- Fix all typo errors
- version 1.5.5: May 2021
	- Re-branding Product names and URLs.
	- add trkd_wsstreaming.py Batch support.
- version 1.6.0: Mar 2022
	- Add ```dotenv``` and Environment Variable for credentials
	- Update requirements.txt and requirements-notebook.txt files
	- Update libraries versions
