#!/usr/bin/env python

import json
import urllib
import urllib2
import time

def passthru(command):
    if not (command == ['rescan']):
        transmit('http://127.0.0.1:9000', command, 'b8:27:eb:c8:56:60')
    else:
        transmit('http://127.0.0.1:9000', command, '')

def transmit(host, cmd, tgt):
    data = {'id': 1, 'method': 'slim.request', 'params': [tgt,cmd]}
    data = json.JSONEncoder().encode(data)
    
    content = {'Content-Type': 'application/json'}
    
    req = urllib2.Request(host+'/jsonrpc.js', data, content)
    urldo = urllib2.urlopen(req)