#!/usr/bin/env python

from snmp_helper import snmp_get_oid, snmp_extract

COMMUNITY_STRING = 'galileo'
SNMP_PORT = 161
IP = '184.105.247.70'

a_device = (IP, COMMUNITY_STRING, SNMP_PORT)
OID_sysDescr = '1.3.6.1.2.1.1.1.0'
OID_sysName = '1.3.6.1.2.1.1.5.0'


def get_oid(device, oid):
    snmp_data = snmp_get_oid(device, oid=oid)
    output = snmp_extract(snmp_data)
    print(output)
    

get_oid(a_device, OID_sysDescr)
get_oid(a_device, OID_sysName)
