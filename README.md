#Introduction
This is an example project that shows how to implement TRKD REST Client with python
- trkd_authen.py: An example application that shows how to authenticate with TRKD service


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
- Version 1: 1 Sep 2016
    - trkd_authen.py