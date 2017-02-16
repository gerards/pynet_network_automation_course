#!/usr/bin/env python


import paramiko
import time
from getpass import getpass

pynet_rtr2 = {
    'device':'Cisco 881',
    'ip_addr':'184.105.247.71',
    'username':'pyclass',
    'password':'',
    'snmp_port':161,
    'ssh_port':22,
}

def ssh_connect():
    pynet_rtr2['password'] = getpass()

    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        remote_conn_pre.connect(pynet_rtr2['ip_addr'], \
                                username=pynet_rtr2['username'], \
                                password=pynet_rtr2['password'], \
                                look_for_keys=False, \
                                allow_agent=False, \
                                port=pynet_rtr2['ssh_port'])
    except paramiko.ssh_exception.AuthenticationException:
        print "Authentication Failure"
        return "AuthenticationException"
    return remote_conn_pre.invoke_shell()

def ssh_send(command_list):
    for command in command_list:
        remote_conn.send(command + "\n")
    time.sleep(1)
    output = remote_conn.recv(5000)
    print output


if __name__ == '__main__':
    remote_conn_pre = paramiko.SSHClient()
    remote_conn = ssh_connect()
    while(remote_conn == "AuthenticationException"):
        remote_conn = ssh_connect()

    ssh_send(["show running-config | include ^logging buffered"])
    ssh_send(["configure terminal", "logging buffered 10001", "exit"])
    ssh_send(["show running-config | include ^logging buffered"])

