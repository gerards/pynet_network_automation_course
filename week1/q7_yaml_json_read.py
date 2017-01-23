#!/usr/bin/env python3

import yaml, json
import pprint

pp = pprint.PrettyPrinter(indent=4)

with open("q6_yaml_stuff.yml") as f:
    cisco_yaml = yaml.load(f)

with open("q6_json_stuff.json") as f:
    cisco_json = json.load(f)

print("--- YAML ---")
pp.pprint(yaml.dump(cisco_yaml))

print("--- JSON ---")
pp.pprint(json.dumps(cisco_json))
