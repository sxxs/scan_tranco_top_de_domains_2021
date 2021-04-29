#!/usr/bin/env python3

import json
import glob

with open('de.csv', 'r') as f:
    rank = f.readlines()

out = []
c_unreachable = 0
c_notracker = 0

for fname in glob.glob('out/*/results.json'):
    with open(fname, 'r') as f:
        jsn = json.load(f)
        try:
            if not jsn['reachable']:
                c_unreachable += 1
                continue
        except KeyError:
            c_unreachable += 1
            continue

        site = jsn['site_url'][7:].strip()
        cks = []
        for cookie in jsn['cookies']:
            if cookie['is_thirdparty'] and cookie['is_tracker']:
                cks.append({
                    'domain': cookie['domain'],
                    'name': cookie['name'],
                    'value': cookie['value']
                })
        trackers = jsn['tracking']['trackers']
        trkrs = []
        for req in jsn['requests']:
            req_url = req['url']
            try:
                req_dom = req_url.split('://')[1].split('/')[0]
            except IndexError:
                print(req_url, site)
                continue
            if req_dom in trackers:
                trkrs.append(req_url)

        if len(cks) == 0 and len(trkrs) == 0:
            c_notracker += 1
            continue

        out.append({
            'url': site,
            'rank': rank.index(site + '\n'),
            'cookies': cks,
            'tracker': trkrs
        })
    # break

print()
print('Total: ', len(out) + c_unreachable + c_notracker)
print('Unreachable: ', c_unreachable)
print('No Trackers: ', c_notracker)
print('Remaining: ', len(out))
print()

out.sort(key=lambda k: k['rank'])
with open('abstract.json', 'w') as f:
    json.dump(out, f, indent=2)
# print(out)
