#!/usr/bin/python
# This was written for educational purpose and pentest only. Use it at your own risk.
# Author will be not responsible for any damage!
# 
# Coder           : Sandman
# Version         : 1.0
#  

import urllib2, re
from colorama import *
import os
def scan(vict):
    try:
        request = urllib2.Request(vict+"'")
        response = urllib2.urlopen(request)
        data = response.read()
        if "error in your SQL syntax" in data:
            print Fore.GREEN+"Error Estandar -->  "+vict
        elif "Query failed" in data:
            print Fore.GREEN+"Error Estandar -->  "+vict
        elif "supplied argument is not a valid MySQL result resource in" in data:
            print  Fore.GREEN+"Error MySQL -->  "+vict
        elif "You have an error in your SQL syntax" in data:
            print Fore.GREEN+"Error Estandar -->  "+vict
        elif "ORDER BY" in data:
            print Fore.GREEN+"Error Estandar -->  "+vict
        elif "mysql_num_rows()" in data:
            print Fore.GREEN+"Error MySQL -->  "+vict
        elif "SQL query failed" in data:
            print Fore.GREEN+"Error Estandar -->  "+vict
        elif "Microsoft JET Database Engine error '80040e14'" in data:
            print Fore.GREEN+"Error MSSQL -->  "+vict
        elif "Microsoft OLE DB Provider for Oracle" in data:
            print Fore.GREEN+"Error Oracle -->  "+vict
        elif "Error:unknown" in data:
            print Fore.GREEN+"Error Desconosido -->  "+vict
        elif "Fatal error" in data:
            print Fore.GREEN+"Error Desconocido -->  "+vict
        elif "mysql_fetch" in data:
            print Fore.GREEN+"Error MySQL -->  "+vict
        elif "Syntax error" in data:
            print Fore.GREEN+"Error Estandar -->  "+vict
        else:
            pass
    except:
        pass


def iprim(vict):
    try:
        request = urllib2.Request(vict+"'")
        response = urllib2.urlopen(request)
        data = response.read()
        request2 = urllib2.Request(vict+"admin")
        response2 = urllib2.urlopen(request2)
        data2 = response2.read()
        data2 = re.findall('<form name="loginform" id="loginform" action=',data2)
        print data2
        if "error in your SQL syntax" in data:
            print Fore.GREEN+"Error Estandar -->  "+vict
            os.system("echo 'Error Estandar -->  "+vict+"' >> targuets")
        elif "wp-login.php" in data2:
        	print Fore.MAGETA+"Wordpress -->  "+vict
        	os.system("echo 'wordpress -->  "+vict+"' >> targuets")        
        elif "Query failed" in data:
            print Fore.GREEN+"Error Estandar -->  "+vict
            os.system("echo 'Error Estandar -->  "+vict+"' >> targuets")
        elif "supplied argument is not a valid MySQL result resource in" in data:
            print  Fore.GREEN+"Error MySQL -->  "+vict
            os.system("echo 'Error MySQL -->  "+vict+"' >> targuets")
        elif "You have an error in your SQL syntax" in data:
            print Fore.GREEN+"Error Estandar -->  "+vict
            os.system("echo 'Error Estandar -->  "+vict+"' >> targuets")
        elif "ORDER BY" in data:
            print Fore.GREEN+"Error Estandar -->  "+vict
            os.system("echo 'Error Estandar -->  "+vict+"' >> targuets")
        elif "mysql_num_rows()" in data:
            print Fore.GREEN+"Error MySQL -->  "+vict
            os.system("echo 'Error MySQL -->  "+vict+"' >> targuets")
        elif "SQL query failed" in data:
            print Fore.GREEN+"Error Estandar -->  "+vict
            os.system("echo 'Error Estandar -->  "+vict+"' >> targuets")
        elif "Microsoft JET Database Engine error '80040e14'" in data:
            print Fore.GREEN+"Error MSSQL -->  "+vict
            os.system("echo 'Error MSSQL -->  "+vict+"' >> targuets")
        elif "Microsoft OLE DB Provider for Oracle" in data:
            print Fore.GREEN+"Error Oracle -->  "+vict
            os.system("echo 'Error Oracle -->  "+vict+"' >> targuets")
        elif "Error:unknown" in data:
            print Fore.GREEN+"Error Desconosido -->  "+vict
            os.system("echo 'Error Desconosido -->  "+vict+"' >> targuets")
        elif "Fatal error" in data:
            print Fore.GREEN+"Error Desconocido -->  "+vict
            os.system("echo 'Error Desconosido -->  "+vict+"' >> targuets")
        elif "mysql_fetch" in data:
            print Fore.GREEN+"Error MySQL -->  "+vict
            os.system("echo 'Error MySQL -->  "+vict+"' >> targuets")
        elif "Syntax error" in data:
            print Fore.GREEN+"Error Estandar -->  "+vict
            os.system("echo 'Error Estandar -->  "+vict+"' >> targuets")
        else:
            pass
    except:
        pass
