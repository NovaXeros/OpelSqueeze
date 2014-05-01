#!/usr/bin/env python

#this is the startup script for the smartshuffle system.
# Pretty basic, really. Checks to see if database exists, if not, creates it.
# Then it checks the current time.
# The database is updated regularly with the location of the current song playing
# and the time of the current check.
# When the script starts it checks the current time against the last recorded time
# in the database. If it's been longer than 10 mins, it discards the last known song and
# starts a whole new random playlist, and does a rescan in case new songs were added
# during the downtime.

from lib import smartshuffle

smartshuffle.first_check()
