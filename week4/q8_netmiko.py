#!/usr/bin/env python
'''
Question from Pynet Network Automation course
'''

from netmiko import ConnectHandler

CONFIG_FILE = 'q8_config_commands.txt'
PASSWORD = '88newclass'

PYNET1 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'PASSWORD': PASSWORD,
    'secret': '',
    'port': 22
}

PYNET2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'PASSWORD': PASSWORD,
    'secret': '',
    'port': 22
}


if __name__ == '__main__':
    PYNET_RTR1 = ConnectHandler(**PYNET1)
    PYNET_RTR2 = ConnectHandler(**PYNET2)

    for rtr in PYNET_RTR1, PYNET_RTR2:
        with open(CONFIG_FILE) as f:
            print('*** ' + rtr.host + ' START ***')
            print(rtr.send_command('show run | in logging buffered'))
            print(rtr.send_config_set(f))
            print(rtr.send_command('show run | in logging buffered'))
            print('*** ' + rtr.host + ' END ***')
