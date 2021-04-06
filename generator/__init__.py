import shortuuid
from flask import g

def generate_id():
    return shortuuid.ShortUUID().random(length=18)

def shorted_url(gateway):
    return g.get("current_host") + gateway