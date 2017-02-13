#!/usr/bin/env python

import snmp_helper
import datetime
import os.path
import yaml

yaml_file = "q1.yml"

pynet_rtr2_IP = '184.105.247.71' 
pynet_rtr2 = (pynet_rtr2_IP, 161)

snmp_username = 'pysnmp'
snmp_auth_key = 'galileo1'
snmp_encrypt_key = 'galileo1'

oid_running_last_changed = '1.3.6.1.4.1.9.9.43.1.1.1.0' 

output = {}


snmp_user_data = (snmp_username, snmp_auth_key, snmp_encrypt_key)

snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr2, 
                                        snmp_user_data, 
                                        oid=oid_running_last_changed)

running_last_changed = snmp_helper.snmp_extract(snmp_data)

if(os.path.isfile(yaml_file)):
    with open(yaml_file, 'r') as f:
        output = yaml.load(f)
    #print output

if(output["pynet_rtr2"] < running_last_changed):
    print("CHANGED")
else:
    print("NO CHANGE")

with open(yaml_file, 'w') as f:
    output['pynet_rtr2'] = running_last_changed
    f.write(yaml.dump(output, default_flow_style=False))  


