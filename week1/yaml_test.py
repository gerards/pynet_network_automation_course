#!/usr/bin/env python

import yaml

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 'some text', 'oh you want more!', {'attribs': [ 0, 1, 2, 3, 4 ], 'ip_addr': '10.10.10.249'}]

# Prints condensed format
print yaml.dump(my_list)

# Prints in human readable format
print(yaml.dump(my_list, default_flow_style=False))
