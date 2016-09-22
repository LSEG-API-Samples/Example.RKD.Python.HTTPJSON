#Introduction
This is an example project that shows how to implement TRKD REST Client with python
- trkd_authen.py: An example application that shows how to authenticate with TRKD service
- trkd_quote.py: An example application that shows how to subscribe (all fields and specific fields) the Quote data from TRKD service
- trkd_newsheadline.py: An example application that shows how to subscribe the News Headline data from TRKD service
- trkd_newsstory.py: An example application that shows how to subscribe the News Story data from TRKD service
- trkd_intraday.py: An example application that shows how to subscribe the Intraday Time-series data from TRKD service
- trkd_interday.py: An example application that shows how to subscribe the Interday Time-series data from TRKD service


#prerequisite
The following softwares are required to use this script
- Python 2.7.10
- The [requests](http://docs.python-requests.org/en/master/) library 

The script does not support Python 3!

#how to run the script
Run the script via the command line (or shell)
```
$>python <application>.py
```


#Optional - How to install requests
The best way is to get the pip package management tool 
1. export <Python_folder>\Scripts to your OS PATH environment
2. call pip command to install lxml
	```
	$>pip install requests
	```
3. If you are behind proxy, set the proxy first
	```
	export https_proxy="http://<proxy.server>:<port>"
	$>pip install requests
	```
#Releae Note
- Version 1: 6 Sep 2016
    - trkd_authen.py
	- trkd_quote.py
- Version 1.0.1: 7 Sep 2016
	- trkd_newsheadline.py
	- changed code structure to separate call http request 
- Version 1.0.2: 19 Sep 2016
	- trkd_newsstory.py
- version 1.0.3: 22 Sep 2016
	- trkd_intraday.py
	- trkd_interday.py
	