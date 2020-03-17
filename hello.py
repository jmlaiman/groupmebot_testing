import os
import json

import logging
from logging.handlers import RotatingFileHandler

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

from time import sleep

app = Flask(__name__)

@app.route('/',methods=['POST'])
def webhook():
    data = request.get_json()

    if data['name'] != 'Samalytics dev version':
        if 'hello sambot' in data['text'].lower():
            msg = 'Hello'
            sleep(1)
            send_message(msg)

    return "ok", 200

@app.route('/')
def hello_world():
    return 'Hello, World!\n'

def send_message(msg):
    url = 'https://api.groupme.com/v3/bots/post'

    data = {
        'bot_id' : '2120a75e790452f8e87eff6271',
	'text'   : msg
	}
    request_s = Request(url,urlencode(data).encode())
    json_s = urlopen(request_s).read().decode()


if __name__ == '__main__':
    handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(host='0.0.0.0', port=7551)
    
    #app.run(host='2601:246:5500:9bd0:8846:bd38:29db:53e0', port=7551)
    #app.run(host='10.0.0.110', port=7551)
