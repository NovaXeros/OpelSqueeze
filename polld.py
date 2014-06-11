#!/usr/bin/env python

# This is the startup script for the steering wheel polling system.
# The polling system polls the ADC every so often to see what value
# returning.
# Depending on the value at the time of reading, the polling file
# will request the transmission file send a corresponding JSON command to
# the underlying LMS system. Standard.

from lib import polling

polling.poll()
