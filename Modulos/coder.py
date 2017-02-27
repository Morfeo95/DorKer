#!/usr/bin/python
# This was written for educational purpose and pentest only. Use it at your own risk.
# Author will be not responsible for any damage!
# 
# Toolname: coder.py
# Coder   : Sandman
# Version : 1.0
#  
import os
def coder(index2):
	if "<" in index2:
		index2 = index2.replace("<","%3C")
		index2 = index2.replace(">","%3E")
		index2 = index2.replace(" ","%20")
		index2 = index2.replace("/","%2F")
	os.system("echo '"+index2+"' > indexcodeada")