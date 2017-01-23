#!/usr/bin/env python3

from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

crypto_maps = cisco_cfg.find_objects(r'^crypto map CRYPTO')
crypto_maps_group2 = cisco_cfg.find_objects_w_child(parentspec=r'^crypto map CRYPTO', childspec=r'group2$')
crypto_maps_no_aes = cisco_cfg.find_objects_wo_child(parentspec=r'^crypto map CRYPTO', childspec=r'AES')

for cmap in crypto_maps:
    print(cmap.text)
    for cmap_line in cmap.all_children:
        print(cmap_line.text)

print("--- Crypto Maps using group2 ---")
for cmap in crypto_maps_group2:
    print(cmap.text)

print("--- Crypto Maps without AES-SHA ---")
for cmap in crypto_maps_no_aes:
    print(cmap.text)
