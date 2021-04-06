import time

def generate_id():
    return str(time.time())[4:10].replace(".", "")

def shorted_url(gateway):
    return "http://me.com/r/{}".format(gateway)