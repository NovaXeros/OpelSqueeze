#!/usr/bin/env python

import json
import urllib
import urllib2
import time

def passthru(command):
	
	host = 'http://192.168.1.132:9000'
	tgt_rescan = ''
	tgt = '00:00:00:00:00:22'
	
	if not (command == ['rescan']):
		return transmit(host, command, tgt)
	else:
		transmit(host, command, '')

def transmit(host, cmd, tgt):
    _cmd = "_"+cmd[0]
    data = {'id': 1, 'method': 'slim.request', 'params': [tgt,cmd]}
    data = json.JSONEncoder().encode(data)
    
    content = {'Content-Type': 'application/json'}
    
    req = urllib2.Request(host+'/jsonrpc.js', data, content)
    urldo = urllib2.urlopen(req)
    
    response = json.load(urldo)
    package = response["result"]
    
    try:
        result = package[_cmd]
        return result
    except:
        return