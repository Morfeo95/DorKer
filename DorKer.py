#!/usr/bin/python
# This was written for educational purpose and pentest only. Use it at your own risk.
# Author will be not responsible for any damage!
# 
# Toolname        : DorKer.py
# Coder           : Sandman
# Version         : 1.0
#  

import re 
import urllib2
import sqlscann
import commands
import os
import csv
import sys
import subprocess
from colorama import *

def logo():
	print Fore.RED+"________                ____  __.            "
	print "\______ \   ___________|    |/ _|___________ "
	print " |    |  \ /  _ \_  __ \      <_/ __ \_  __ \ "
	print " |    `   (  <_> )  | \/    |  \  ___/|  | \/"
	print "/_______  /\____/|__|  |____|__ \___  >__|   "
	print "        \/                     \/   \/       "
	print "              By: Sandman"
	print "Correo y Xmpp: sandman95@cock.li twitter: @Sandman__95"

def clean():

	if sys.platform == "linux" or sys.platform == "linux2":
		subprocess.call(["clear"], shell=True)

	else:
		subprocess.call(["cls"], shell=True)
		
clean()			
logo()
print """
    [1] Ingresar Dork
    [2] Utilizar txt con diferentes dorks
"""
	
while True:
	respuesta = raw_input("=>:  ")
	if respuesta == "1":
		print Fore.WHITE+"DorKer"
		print ""
		impr = raw_input("Te Gustaria guardar las URL's en un Documento? Y/n  ")
		dork = raw_input("Dork: ")
		if " " in dork:
			dork=dork.replace(" ", "+")

		def finder(dork):
			first = 1
			while first<=500:
				response = urllib2.urlopen("http://www.bing.com/search?q={}&first={}".format(dork, first))
				payload = response.read()
				results = re.findall('<h2><a(.*?)h="', payload)
				for result in results:
					result = result.lstrip(" href=")
					result = result.lstrip('"')
					result = result.rstrip('" ')
					vict = result
					sqlscann.scan(vict)
					first = first + 10
		def printer(dork):
			first = 1
			while first<=500:
				response = urllib2.urlopen("http://www.bing.com/search?q={}&first={}".format(dork, first))
				payload = response.read()
				results = re.findall('<h2><a(.*?)h="', payload)
				for result in results:
					result = result.lstrip(" href=")
					result = result.lstrip('"')
					result = result.rstrip('" ')
					vict = result
					sqlscann.iprim(vict)
					first = first + 10
		if impr == "y" or impr == "Y" or impr == "":
			printer(dork)
		elif impr == "N" or impr == "n": 
			finder(dork)
		print ""
		print "Listo"
	
	elif respuesta == "2":
		print Fore.WHITE+"Dorker"
		print ""
		impr = raw_input("Te Gustaria guardar las URL's en un Documento? Y/n  ")
		print "Introduce la ruta de tus dorks"
		print "ex. /home/user/dorks.txt"
		
		dork = raw_input("=>:  ")
		lista = commands.getoutput("cat "+dork)
		os.system("echo '"+lista+"' > Dorks.txt")
		dorklist = open("Dorks.txt","r")
		reader = csv.reader(dorklist)
		lista = [row for row in reader]
		nl = 0
		dork = str(lista [nl])
		i = 1
		print len(lista)
		while True:
			
			if "['" in dork:
				dork=dork.replace("['", "")
				dork=dork.replace("']","")
			if " " in dork:
				dork=dork.replace(" ", "+")

			def finder(dork):
				print (Fore.YELLOW+"Buscando el Dorck "+dork)
				first = 1
				while first<=500:
					response = urllib2.urlopen("http://www.bing.com/search?q={}&first={}".format(dork, first))
					payload = response.read()
					results = re.findall('<h2><a(.*?)h="', payload)
					for result in results:
						result = result.lstrip(" href=")
						result = result.lstrip('"')
						result = result.rstrip('" ')
						vict = result
						sqlscann.scan(vict)
						first = first + 10
			def printer(dork):
				print (Fore.YELLOW+"Buscando el Dorck "+dork)
				first = 1
				while first<=500:
					response = urllib2.urlopen("http://www.bing.com/search?q={}&first={}".format(dork, first))
					payload = response.read()
					results = re.findall('<h2><a(.*?)h="', payload)
					for result in results:
						result = result.lstrip(" href=")
						result = result.lstrip('"')
						result = result.rstrip('" ')
						vict = result
						sqlscann.iprim(vict)
						first = first + 10
			if impr == "y" or impr == "Y" or impr == "":
				printer(dork)
			elif impr == "N" or impr == "n": 
				finder(dork)
			nl = nl + 1
			i = i + 1
			if i <= len(lista):
				dork = str(lista [nl])
			elif i > len(lista):
				print ""
				print "Todos Los Dorks Escaneados..."
				os.system("rm Dorks.txt")
				sys.exit(0)
		
