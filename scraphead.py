#!/usr/bin/env python
# coding: utf

# 2020-04-19 by Madame Minty
# https://github.com/MadameMinty/scrappy
# Scraphead. Required to execute service list.

import sys                         #arguments
import subprocess                  #communicate, browser
from lxml.html import fromstring   #xpath parsing
from lxml.etree \
   import tostring as htmlstring
import zlib                        #hashing
import re                          #regex


def communicate(text):
	chatid = 'YOUR CONVERSATION ID HERE'
	subprocess.call( ['python3', 'hangouts.py', chatid, text ] )


def changes(service, new):
	filepath = '/var/log/scrappy/scrappy-'+service+'.log'
	
	try:
		file = open(filepath, 'r+')
		old = str(file.read())
		file.close()
	except FileNotFoundError:
		old = ''

	if old != new :
		file = open(filepath, 'w')
		communicate(new)
		file.write(str(new))
		file.close()


def request(browser, url):
	if browser == '':
		browser = 'chrome'

	cmd = {
		'chrome': 'chromium --headless --disable-gpu --window-size=1920x1080 --dump-dom ',
		'wget': 'wget --user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.63 Safari/537.36" -q -O - '
	}
	
	return subprocess.run([ cmd[browser]+url ],shell=True,stdout=subprocess.PIPE).stdout.decode('utf-8').rstrip("\n")
	

def filter(request, method, pattern, group=''):

	if method == 'hash' or method == '':
		return hex(zlib.crc32( request.stdout ))

	elif method == 'xpath':
		node = fromstring( str(request) ).xpath(pattern)[0]
		return node.text + ''.join(etree.tostring(e) for e in node)

	elif method == 'regex':
		return re.search( pattern, request ).group(group)
