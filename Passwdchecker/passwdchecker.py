#!/bin/python3
from colorama import Fore, Back, Style
import re
file = open('xato-net-10-million-passwords.txt', encoding ='latin1')
lines = file.read().strip('\n')


print ("██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗      ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗") 
print ("██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗")
print ("██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝")
print ("██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗")
print ("██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║")
print ("╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝      ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝")

while True:
                                                                                                                             
	password = input("Please Enter password you want to check: ")
	valid_pass = False

	if password in lines[0:1000000*1000000]:
			print (Fore.RED + "THIS PASSWORD IS NOT SECURE AS IT IS INCLUDED IN PUBLIC WORDLISTS\n-Please use a password of at least six characters\n-Include at least one number\n-Include at least one upper case letter\n-Include at least one lower case letter\n-Include at least one special character")
			print(Style.RESET_ALL)

	elif (len(password)<6):
			print (Fore.RED + "PLEASE USE A PASSWORD OF AT LEAST SIX CHARACTERS\n-Include at least one number\n-Include at least one upper case letter\n-Include at least one lower case letter\n-Include at least one special character")
			print(Style.RESET_ALL)

	elif not re.search("[1-9]", password):
			print (Fore.RED + "PLEASE INCLUDE AT LEAST ONE NUMBER\n-Use a password of at least six characters\n-Include at least one upper case letter\n-Include at least one lower case letter\n-Include at least one special character")
			print(Style.RESET_ALL)

	elif not re.search("[A-Z]", password):
			print(Fore.RED + "PLEASE INCLUDE AT LEAST ONE UPPER CASE LETTER\n-Use a password of at least six characters\n-Include at least one number\n-Include at least one lower case letter\n-Include at least one special character")
			print(Style.RESET_ALL)

	elif not re.search("[a-z]", password):
    		print(Fore.RED + "PLEASE INCLUDE AT LEAST ONE LOWER CASE LETTER\n-Use a password of at least six characters\n-Include at least one number\n-Include at least one upper case letter\n-Include at least one special character")
    		print(Style.RESET_ALL)

	elif not re.search("[?><.,/`~!@#$%^&*]", password):
			print(Fore.RED + "PLEASE INCLUDE AT LEAST ONE SPECIAL CHARACTER\n-Use a password of at least six characters\n-Include at least one number\n-Include at least one upper case letter\n-Include at least one lower case letter")
			print(Style.RESET_ALL)

	else:
		valid_pass = True
		break
	
if(valid_pass):
	print (Fore.GREEN + "Good Password as it meets all the security requirements")

