#!/usr/bin/python

import subprocess

interface = input("Interface >")
mac_id = input("New MAC id > ")

subprocess.call(["sudo","ifconfig",interface,"down"])
subprocess.call(["sudo","ifconfig",interface,"hw","ether",mac_id])
subprocess.call(["sudo","ifconfig",interface,"up"])
