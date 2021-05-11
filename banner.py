#!/usr/bin/env python3

import json

# urls = set()
# with open('domains-w-banner.txt') as f:
#     for line in f.readlines():
#         urls.add(line.strip())

# with open('abstract.json', 'r') as f:
#     dom = json.load(f)

# for e in dom:
#     e['banner'] = e['url'] in urls

# with open('abstract.json', 'w') as f:
#     json.dump(dom, f, indent=2)

with open('abstract-sure.json', 'r') as f:
    for e in json.load(f):
        if e['banner'] and len(e['cookies']) > 0:
            print(e['url'])
