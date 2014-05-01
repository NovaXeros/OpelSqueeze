#!/usr/bin/python

import os
import spidev
import time
import transmission as send

spi = spidev.SpiDev()
spi.open(0,0)

def readadc(adcnum):
	if ((adcnum >7) or (adcnum < 0)):
		return -1
	r = spi.xfer2([1,(8+adcnum)<<4,0])
	adcout = ((r[1]&3) << 8) + r[2]
	return adcout

while True:
	averact = int(readadc(0))

	if (averact >= 80) and (averact < 125):
		send.passthru(['pause'])
		time.sleep(0.5)
	elif (averact >= 140) and (averact < 195):
		send.passthru(['button','jump_fwd'])
		time.sleep(0.5)
	elif (averact >= 230) and (averact < 285):
		send.passthru(['button','jump_rew'])
		time.sleep(0.5)  
	elif (averact >= 375) and (averact < 425):
		send.passthru(['randomplay','tracks'])
		time.sleep(0.5)
	time.sleep(0.05)
