#!/usr/bin/python

import subprocess
import optparse
import re


#Defining the function to take arguments.
def get_args():
	#Defining our parser variable, which will parse user supplied command-line arguments.
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", help="Mention the interface name whose MAC address has to be changed." )
	parser.add_option("-m", "--mac", dest="mac_id", help="Enter the desired mac address." )
	(options, arguments) =  parser.parse_args()
	if not options.interface:
		parser.error("[-] Please supply a value for interface, use --help for more info.")
	elif not options.mac_id:
		parser.error("[-] Please supply the desired MAC address, use --help for more info.")
	else:
		return options

#Defining the function to change mac address.
def machanger(interface, mac_id):
	print ("[*] Changing MAC addr for " + interface + " interface to " + mac_id)
	#Executing sequential commands for changing the MAC address.
	subprocess.call(["sudo","ifconfig",interface,"down"])
	subprocess.call(["sudo","ifconfig",interface,"hw","ether",mac_id])
	subprocess.call(["sudo","ifconfig",interface,"up"])

#Function for grepping initial MAC addr from ifconfig.
def get_mac(interface):
	ifconfig_res = subprocess.check_output(["ifconfig",interface])
	#Grepping the MAC addr of the required interface through regex.
	current_mac = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_res.decode())
	print("")
	if current_mac:
		return current_mac.group(0)
	else:
		print("[-] Could not find any MAC address.")
	

options = get_args()
current_mac = get_mac(options.interface)
print("[+] Current MAC: " + str(current_mac))


#Changing MAC address
machanger(options.interface, options.mac_id)

current_mac = get_mac(options.interface)

if current_mac == options.mac_id:
	print("[+] MAC addr changed to " + current_mac)
else:
	print("[-] MAC addr couldn't be changed.")
