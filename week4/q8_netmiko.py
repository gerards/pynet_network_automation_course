#!/usr/bin/env python

from netmiko import ConnectHandler 
from getpass import getpass

config_file = 'q8_config_commands.txt'
password = '88newclass' 

pynet1 = {
	'device_type': 'cisco_ios',
	'ip': '184.105.247.70',
	'username': 'pyclass',
	'password': password,
	'secret': '',
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


if __name__ == '__main__':
    pynet_rtr1 = ConnectHandler(**pynet1)
    pynet_rtr2 = ConnectHandler(**pynet2)
    
    for rtr in pynet_rtr1, pynet_rtr2:
        with open(config_file) as f:
            print('*** ' + rtr.host + ' START ***')
            print rtr.send_command('show run | in logging buffered')
            print rtr.send_config_set(f)
            print rtr.send_command('show run | in logging buffered')
            print('*** ' + rtr.host + ' END ***')
