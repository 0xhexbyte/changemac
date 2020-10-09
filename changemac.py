#!/usr/bin/python

import subprocess

#Defining the variables and taking input from the user.

interface = input("Interface > ")
mac_id = input("New MAC id > ")

print ("[*] Changing MAC addr for " + interface + " interface to " + mac_id)

#Executing sequential commands for changing the MAC address.

subprocess.call(["sudo","ifconfig",interface,"down"])
subprocess.call(["sudo","ifconfig",interface,"hw","ether",mac_id])
subprocess.call(["sudo","ifconfig",interface,"up"])
	
