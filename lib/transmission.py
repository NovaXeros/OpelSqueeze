#!/usr/bin/env python

import json
import urllib
import urllib2
import time

host = 'http://192.168.1.1:9000'

def rp_add():
	randomplay_host = host+'/plugins/RandomPlay/mix.html'
	params = {'type': 'track', 'addOnly': 1, 'player': 'PiCarSquared'}
	data = urllib.urlencode(params)
	u = urllib2.urlopen(randomplay_host, data)

def passthru(command):
	
	tgt_rescan = ''
	tgt = 'b8:27:eb:c8:56:60'
	
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