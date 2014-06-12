#!/usr/bin/env python

import os
import time
import transmission as send
import shelve
import smartshuffle as shf

floc = '/var/squeezewheel/'
checkfile = floc+'check.db'

def check_for_dir():
	if os.path.isdir(floc) == True:
		check_for_file()
	else:
		try:
			os.mkdir(floc)
			os.chmod(floc,0777)
			check_for_file()
		except:
			check_for_file()

def check_for_file():
	if os.path.isfile(checkfile) == True:
		shf.first_check()
	else:
		prime()
		

def prime():
	s = shelve.open(checkfile)
	try:
		s['last_checked_song'] = 'PRIMED'
		s['last_checked_time'] = 0
		s['last_checked_prog'] = 0 
	finally:
		s.close()
		print "Priming a new database."
		shf.first_check()

def update_shelf():
	while True:
		s = shelve.open(checkfile, writeback=True)
		current_song = send.passthru(['path','?'])
		current_prog = send.passthru(['time','?'])
		current_time = time.time()
		
		s['last_checked_time'] = current_time
		s['last_checked_song'] = current_song
		s['last_checked_prog'] = current_prog
		
		s.close()

def query(request):
	s = shelve.open(checkfile)
	if request == 'song':
		answer = s['last_checked_song']
		s.close()
		return answer
	if request == 'time':
		answer = s['last_checked_time']
		s.close()
		return answer
	if request == 'prog':
		answer = s['last_checked_prog']
		s.close()
		return answer
