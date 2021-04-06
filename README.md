# Straight.it
![logo](https://raw.githubusercontent.com/dhanuprys/arts/master/straight-it-logo.png)
Developed with flasks to facilitate and speed up the development of link shortener applications.

## Requirements 📄
- Python 3 or higher
- PIP 3 or higher
- Several python libraries, will be explained later in the installation section

## Step by Step to Install :walking:
### Download from Github :arrow_heading_down:
```bash
$ git clone https://github.com/dhanuprys/straight-it
```

```bash
$ cd straight-it
```

### Install the Required Dependencies :building_construction:
```bash
$ pip3 install -r requirements.txt
```

> Wait a few moments for it to finish

## Run the Application :rocket:
Before running the application, you must pay attention to the following things such as port settings, 
access keys and others. 

**All these configurations can be configured through the environment.**

Simply the application can be run with the following command:
```bash
$ STRAIGHT_API_KEY=yourprivatekey python3 __main__.py
```

### API Key Settings (required) :key:
```bash
$ STRAIGHT_API_KEY=<yourprivatekey> ...
```

### HTTP Redirect Settings :arrow_right:
```bash
$ STRAIGHT_HTTP_REFERRER=<drivertype> ...
```

HTTP driver type list:
- http **(default)**
- javascript / js

If you choose *http*, the server will provide a response in the form of a status code which will redirect to the intended link. 
But if you use *javascript* / *js* then the server will display an html page containing javascript code which will redirect to the destination page

### Port Settings (default: 8080) :door:
```bash
$ PORT=<portvalue> ...
```

## API Access Guide :link:
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

### Store Data (create) :heavy_plus_sign:
```
HTTP POST /api/v1/links?key=<yourapikey>
{
  "gateway": "<your gateway>", // if this field is not declared then the server will perform a random gateway selection
  "target": "<your target url, example: http://github.com/dhanuprys>" // required
}
```

### Get All the Data (read all) :eye:
> On development

```
HTTP GET /api/v1/links?key=<yourapikey>
```

### Get Specific Data (read spesific) :eyeglasses:
```
HTTP GET /api/v1/links?key=<yourapikey>&gateway=<yourgateway>
```

### Update Existing Data (update) :eyeglasses: :heavy_minus_sign: :heavy_plus_sign:
```
HTTP PUT /api/v1/links?key=<yourapikey>
{
  "gateway": "<your previous gateway>", // required
  "target": "<your new target>" // required
}
```

### Delete Existing Data (delete) :heavy_minus_sign:
```
HTTP DELETE /api/v1/links?key=<yourapikey>
{
  "gateway": "<your previous gateway>", // required
}
```
