#!/usr/bin/env python
# coding: utf

# 2020-04-19
# https://github.com/MadameMinty/scrappy
# Service list. Requires Scraphead.
from scraphead import *;from time import sleep
# ---------------- service list start


# ---------------- CHROME EXAMPLE
def _chre():
	url = 'https://www.x-kom.pl/'
	r = request('chrome', url)
	hash = filter(r, 'hash', '')
	price = filter(r, 'regex', r'>(\d+,\d{2} zł)<', group=1)
	return price + ' and the hash is ' + hash


# ---------------- WGET/XPATH EXAMPLE
def _wgxp():
	url = 'https://www.x-kom.pl/'
	sleep(5.0) #fine-tuning execution time
	r = request('wget', url)
	name  = filter(r, 'xpath', '//*[@id="hotShot"]/div[2]/div[1]/p')
	return 'X-Kom: ' + name + '\n' + url


# ---------------- service list end
changes( sys.argv[1], eval('_' +sys.argv[1]+ '()') ) if len(sys.argv) > 1 else print('No task to run, exiting')
