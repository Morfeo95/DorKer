#!/usr/bin/python
# This was written for educational purpose and pentest only. Use it at your own risk.
# Author will be not responsible for any damage!
# 
# Toolname        : DorKer.py
# Coder           : Sandman
# Version         : 1.0
#  


import os
import sys
import subprocess
import commands
import urllib2
import urllib
import mechanize
import re
import random



def logo():
	print("Piensa en un bonito logo :3")
	
def finder():
	logo()
	useragent = ['Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/20100207 Ubuntu/9.04 (jaunty) Namoroka/3.6.2pre',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;',
            'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)',
            'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
            'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)',
            'Microsoft Internet Explorer/4.0b1 (Windows 95)',
            'Opera/8.00 (Windows NT 5.1; U; en)',
            'Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)',
            'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
            'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ZoomSpider.net bot; .NET CLR 1.1.4322)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QihooBot 1.0 qihoobot@qihoo.net)',
            'Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.11 [en]']
	headers = random.choice(useragent)
	header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)'}
	browser = mechanize.Browser()
	browser.set_handle_robots(False)
	browser.addheaders = [('User-agent',useragent)]
	page = ["0"]
	print('Ingresa tu Dork: ')
	dork = str(raw_input('----->   '))
	for i in page:
		try:
			duck =  "https://duckduckgo.com/q="+dork+"?ia=web"+i
			html = browser.open(duck).read()
			print (html)
			patron = re.compile("<h3 class=\"r\"><a href=\"/url\?q=(.*?)&amp.*?\">.*?</a></h3>")
			found = re.findall(patron,html)
			print (found,"lol")
		except:
			pass
finder()
	
