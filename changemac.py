#!/usr/bin/python

import subprocess
import optparse

def machanger(interface, mac_id):
	print ("[*] Changing MAC addr for " + interface + " interface to " + mac_id)

	#Executing sequential commands for changing the MAC address.

	subprocess.call(["sudo","ifconfig",interface,"down"])
	subprocess.call(["sudo","ifconfig",interface,"hw","ether",mac_id])
	subprocess.call(["sudo","ifconfig",interface,"up"])
	


#Defining our parser variable, which will parse user supplied command-line arguments

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Mention the interface name whose MAC address has to be changed." )
parser.add_option("-m", "--mac", dest="mac_id", help="Enter the desired mac address." )

(options, arguments) = parser.parse_args()

#Defining the variables and taking input from the user.

interface = options.interface
mac_id = options.mac_id

#Calling the function

machanger(interface, mac_id)
