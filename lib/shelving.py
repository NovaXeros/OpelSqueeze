#!/usr/bin/env python

import os.path
import time
import transmission as send
import shelve
import smartshuffle as shf

def prime():
		s = shelve.open('check.db')
		try:
			s['key1'] = { 'last_checked_song': 'None', 'last_checked_time': 0 }
		finally:
			s.close()
			print "Priming a new database."
			shf.first_check()

def update_shelf():
	while True:
		s = shelve.open('check.db', writeback=True)
		current_song = send.passthru(['path','?'])
		current_time = time.time()
		
		last_song_loc = s['key1']['last_checked_song']
		last_check_time = s['key1']['last_checked_time']
		
		s['key1']['last_checked_time'] = current_time
		s['key1']['last_checked_song'] = current_song
		
		s.close()

def query(request):
	s = shelve.open('check.db')
	if request == 'song':
		answer = s['key1']['last_checked_song']
		s.close()
		return answer
	if request == 'time':
		answer = s['key1']['last_checked_time']
		s.close()
		return answer