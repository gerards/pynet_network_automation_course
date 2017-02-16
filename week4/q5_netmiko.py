#!/usr/bin/env python

from netmiko import ConnectHandler 
from getpass import getpass

password = '88newclass' 

pynet1 = {
	'device_type': 'cisco_ios',
	'ip': '184.105.247.70',
	'username': 'pyclass',
	'password': password,
	'port': 22
}

pynet2 = {
	'device_type': 'cisco_ios',
	'ip': '184.105.247.71',
	'username': 'pyclass',
	'password': password,
	'secret': '',
	'port': 22
}

juniper_srx = {
	'device_type': 'juniper',
	'ip': '184.105.247.76',
	'username': 'pyclass',
	'password': password,
	'port': 22
}

pynet_rtr1 = ConnectHandler(**pynet1)
pynet_rtr2 = ConnectHandler(**pynet2)
pynet_srx1 = ConnectHandler(**juniper_srx)

pynet_rtr1.config_mode()
if(pynet_rtr1.check_config_mode() == True):
	print("Currently in config mode")
