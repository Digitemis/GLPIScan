# GLPIScan

GLPIScan is a vulnerability scanner for GLPI.

## Prerequisites

* pychalk >= 2.0.1 - Recommended: latest 
* requests >= 2.18.4 - Recommended: latest 
* urllib3 >= 1.22 - Recommended: latest 
* packaging >= 19.0 - Recommended: latest 

## Installation

In order to install GLPIScan, you only need to clone the repository, and install the python dependencies using the requirements.txt


```bash
$ pip install -r requirements.txt
```

## Usage

List of options :

```
usage: GLPIScan.py [-h] -u url [-a] [-c] [-f] [-p] [-d]

GLPI Vulnerability Scanner.

optional arguments:
  -h, --help  show this help message and exit
  -u url      URL of GLPI application
  -a          Perform allcheck
  -c          Perform Credential Check
  -f          Perform Files Check
  -p          Perform Plugin Check
  -d          Debug mode
```

Most common usage :

```bash
$ python GLPIScan.py -u http://glpi/ -a
```

## Further configuration

The inc/Config.py file contain addiditional parameters.

The parameter "PROXY" allow you to configure a proxy :
```python
PROXY = {"http"  : "http://127.0.0.1:8080", "https" : "https://127.0.0.1:8080"}
```

The parameter "HEADER" allow you yo add custom header to each request
```python
HEADERS = {"X-FORWARDED-FOR" : "127.0.0.1"}
```
The parameter "VERSION" allow you force the version of the scanned GLPI (if you already know the version) :
```python
VERSION = "9.4.0" # for GLPI version 9.4.0
```

## Authors

* **David CARNOT** - [Digitemis](https://www.digitemis.com/)
* **Erwan R.** - [Digitemis](https://www.digitemis.com/)