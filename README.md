# Straight.it
![logo](https://raw.githubusercontent.com/dhanuprys/arts/master/straight-it-logo.png)
Developed with flasks to facilitate and speed up the development of link shortener applications.

## Requirements
- Python 3 or higher
- PIP 3 or higher
- Several python libraries, will be explained later in the installation section

## Step by Step to Install
### Download from Github
```bash
$ git clone https://github.com/dhanuprys/straight-it
```

```bash
$ cd straight-it
```

### Install the Required Dependencies
```bash
$ pip3 install -r requirements.txt
```

> Wait a few moments for it to finish

## Run the Application
Before running the application, you must pay attention to the following things such as port settings, 
access keys and others. 

**All these configurations can be configured through the environment.**

Simply the application can be run with the following command:
```bash
$ STRAIGHT_API_KEY=yourprivatekey python3 __main__.py
```

### API Key Settings (required)
```bash
$ STRAIGHT_API_KEY=<yourprivatekey> ...
```

### HTTP Redirect Settings
```bash
$ STRAIGHT_HTTP_REFERRER=<drivertype> ...
```

HTTP driver type list:
- http
- javascript / js

### Port Settings (default: 8080)
```bash
$ PORT=<portvalue> ...
```

## Access Guide API
COMING SOON
