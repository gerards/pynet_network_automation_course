#!/usr/bin/env python3

import yaml, json
from pprint import pprint

with open("q6_yaml_stuff.yml") as f:
    cisco_yaml = yaml.load(f)

with open("q6_json_stuff.json") as f:
    cisco_json = json.load(f)

print("--- YAML ---")
pprint(yaml.dump(cisco_yaml))

print("--- JSON ---")
pprint(json.dumps(cisco_json))
