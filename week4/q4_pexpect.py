#!/usr/bin/env python

import pexpect
import sys
import re
from getpass import getpass

ip_addr = '184.105.247.71'
username = 'pyclass'
port = 22
#password = getpass()
password = "88newclass"

ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
ssh_conn.timeout = 10
ssh_conn.expect('ssword:')
ssh_conn.sendline(password)
ssh_conn.expect('pynet-rtr2#')

ssh_conn.sendline('terminal length 0')
ssh_conn.expect('pynet-rtr2#')

ssh_conn.sendline('show run | in logging buffered')
ssh_conn.expect('pynet-rtr2#')
print ssh_conn.before

ssh_conn.sendline('configure terminal')
ssh_conn.sendline('logging buffered 20101')
ssh_conn.sendline('exit')
ssh_conn.expect('pynet-rtr2#')
print ssh_conn.before

ssh_conn.sendline('show run | in logging buffered')
ssh_conn.expect('pynet-rtr2#')
print ssh_conn.before
