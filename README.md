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

## API Access Guide
Straight.it implements the CRUD api model. So everything is easier now if you want to save, modify, delete, 
or even view the entire list of data that has been saved.

All matters concerning API access must use the following url.
```
http://yourhosturl.com/api/v1/links
```

All access to the API requires the api key that you have set yourself in the STRAIGHT_API_KEY environment and 
will be passed at the end of the url as a 'key' parameter as shown below.
```
http://yourhosturl.com/api/v1/links?key=<yourapikey>
```

### Store Data (create)
```
HTTP POST /api/v1/links?key=<yourapikey>
{
  "gateway": "<your gateway>", // if this field is not declared then the server will perform a random gateway selection
  "target": "<your target url, example: http://github.com/dhanuprys>" // required
}
```

### Get All the Data (read all)
> On development

```
HTTP GET /api/v1/links?key=<yourapikey>
```

### Get Specific Data (read spesific)
> On development

```
HTTP GET /api/v1/links?key=<yourapikey>
```

### Update Existing Data (update)
```
HTTP PUT /api/v1/links?key=<yourapikey>
{
  "gateway": "<your previous gateway>", // required
  "target": "<your new target>" // required
}
```

### Delete Existing Data 
```
HTTP DELETE /api/v1/links?key=<yourapikey>
{
  "gateway": "<your previous gateway>", // required
}
```
