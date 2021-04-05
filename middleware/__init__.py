import re
from flask import request, g
import pprint

def api_key_filter():
    if g.is_api and not request.args.get("key") == g.app_key:
        return "Request autheticated"

def safe_api_request():
    if len(re.findall("/api/v1/links", request.url)) > 0:
        g.is_api = True
    else:
        g.is_api = False

    # Forward to api_key_filter