#!/usr/bin/env python3

import yaml, json
from ciscoconfparse import CiscoConfParse

c2600_config = CiscoConfParse('c2960_config.txt')
ints = []


for int in c2600_config.find_objects(r'^interface'):
    int_name = int.text[10:]

    ## If a Vlan interface grab entire configuration
    if(int_name[:4] == 'Vlan'):
        ints.append({int_name: []})
        for line in int.all_children:
            ints[-1][int_name].append(line.text)
    else:
        ints.append(int_name)

with open("q6_yaml_stuff.yml", "w") as f:
    f.write(yaml.dump(ints, default_flow_style=False))

with open("q6_json_stuff.json", "w") as f:
    json.dump(ints, f)



'''
print("\n\n--- YAML ---")
print(yaml.dump(ints, default_flow_style=False))

print("\n\n--- JSON ---")
print(json.dumps(ints))

for i in ints:
    print(i)
'''
