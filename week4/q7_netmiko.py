#!/usr/bin/env python

from netmiko import ConnectHandler 
from getpass import getpass

password = '88newclass' 

pynet2 = {
	'device_type': 'cisco_ios',
	'ip': '184.105.247.71',
	'username': 'pyclass',
	'password': password,
	'secret': '',
	'port': 22
}

if __name__ == '__main__':
    pynet_rtr2 = ConnectHandler(**pynet2)
    
    output = pynet_rtr2.send_command("show running-config | include ^logging buffered")
    print output
    pynet_rtr2.send_config_set(['logging buffered 10002'])
    output = pynet_rtr2.send_command("show running-config | include ^logging buffered")
    print output
