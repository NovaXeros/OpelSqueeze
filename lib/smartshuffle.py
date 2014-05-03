#!/usr/bin/env python

import os.path
import time
import transmission as send
import shelving as db

def first_check():
	if os.path.isfile('check.db') == False:
		db.prime()
	else:
		if send.passthru(['mode','?']) == 'play':
			db.update_shelf()
		else:
			perform_start_tasks()

def perform_start_tasks():
	last_known_check = db.query('time')
	last_known_song = db.query('song')
	time_without = time.time() - int(last_known_check)
	
	if last_known_song == 'PRIMED':
		send.passthru(['randomplay','tracks'])
	else:
		if (time_without < 600):
			send.passthru(['playlist','play',last_known_song])
			time.sleep(1)
			send.passthru(['playlist','add','randomplay://track'])
			db.update_shelf()
		else:
			send.passthru(['rescan'])
			time.sleep(2)
			send.passthru(['randomplay','tracks'])
			db.update_shelf()