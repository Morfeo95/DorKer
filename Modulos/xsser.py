#!/usr/bin/python
# This was written for educational purpose and pentest only. Use it at your own risk.
# Author will be not responsible for any damage!
# 
# Toolname: XSSeR.py
# Coder   : Sandman
# Version : 1.0
#  
import os
import urllib2
from colorama import *
def xsscan(vict,index,index2):
	try:
		request = urllib2.Request(vict+index)
		response = urllib2.urlopen(request)
		data = response.read()
		if index in data:
			print Fore.GREEN+"XSS Podria Ser Un Error -->  "+vict+index
		elif index2 in data:
			print Fore.GREEN+"XSS Podria Ser Un Error -->  "+vict+index
		else:
			pass
	except:
		pass


def xssimpr(vict,index,index2):
	try:
		request = urllib2.Request(vict+index)
		response = urllib2.urlopen(request)
		data = response.read()
		if index in data:
			print Fore.GREEN+"XSS Podria Ser Un Error -->  "+vict+index
			os.system("echo 'XSS Podria Ser Un Error -->  "+vict+index+"' >> targuets")
		elif index2 in data:
			print Fore.GREEN+"XSS Podria Ser Un Error -->  "+vict+index
			os.system("echo 'XSS Podria Ser Un Error -->  "+vict+index+"' >> targuets")
		else:
			pass
	except:
		pass	
