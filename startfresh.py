#!/usr/bin/env python

import time
import transmission as send

time.sleep(45)
send.passthru(['rescan'])
send.passthru(['randomplay','tracks'])
