#!/usr/bin/env python

import pexpect
import sys
import re
from getpass import getpass

ip_addr = '184.105.247.71'
username = 'pyclass'
port = 22
password = getpass()

ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
ssh_conn.timeout = 10
ssh_conn.expect('ssword:')
ssh_conn.sendline(password)
ssh_conn.expect('pynet-rtr2#')

ssh_conn.sendline('show ip int brief')
ssh_conn.expect('pynet-rtr2#')
print ssh_conn.before
