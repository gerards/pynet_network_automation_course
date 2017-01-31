#!/usr/bin/env python

import telnetlib
import time

ip_addr = '184.105.247.70'
TELNET_PORT = 23
TELNET_TIMEOUT = 6
username = 'pyclass'
password = '88newclass'

remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)

remote_conn.read_until("sername:", TELNET_TIMEOUT)
remote_conn.write(username + "\n")

remote_conn.read_until("assword", TELNET_TIMEOUT)
remote_conn.write(password + "\n")

remote_conn.write("show int desc\n")

time.sleep(1)
output = remote_conn.read_very_eager()
print(output)

remote_conn.close()
