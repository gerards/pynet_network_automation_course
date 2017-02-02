#!/usr/bin/env python

import q3_telnetlib
import telnetlib
import time
import socket
import sys
import getpass


def main():
    '''
    Write a script that connects to the lab pynet-rtr1, logins, and executes the
    'show ip int brief' command.
    '''
    ip_addr = raw_input("IP address: ")
    ip_addr = ip_addr.strip()
    username = 'pyclass'
    password = getpass.getpass()

    remote_conn = q3_telnetlib.telnet_connect(ip_addr)
    output = q3_telnetlib.login(remote_conn, username, password)

    time.sleep(1)
    remote_conn.read_very_eager()
    q3_telnetlib.disable_paging(remote_conn)

    output = q3_telnetlib.send_command(remote_conn, 'show ip int brief')

    print "\n\n"
    print output
    print "\n\n"

    remote_conn.close()

if __name__ == "__main__":
    main()
