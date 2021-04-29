#!/usr/bin/env python3

import json

counts = {}


def check_is_tracker(testurl):
    is_bad = False
    for badurl in [
        'https://pagead2.googlesyndication.com/pagead/gen',
        'https://www.google-analytics.com/collect?',
        'https://www.google-analytics.com/j/collect?',
        'https://googleads4.g.doubleclick.net/pcs/view?',
        'https://googleads.g.doubleclick.net/pagead/viewthroughconversion',
        'https://www.econda-monitor.de/l/'
    ]:
        if testurl.startswith(badurl):
            try:
                counts[badurl] += 1
            except KeyError:
                counts[badurl] = 1
            is_bad = True
    return is_bad


out_sure = []
out_none = []
out_else = []
c_ncbu = 0

with open('abstract.json', 'r') as f:
    for dom in json.load(f):
        if len(dom['cookies']) == 0:
            has_bad_urls = False
            for trkr in dom['tracker']:
                if check_is_tracker(trkr):
                    has_bad_urls = True
                    break
            if has_bad_urls:
                c_ncbu += 1
                out_sure.append(dom)
            else:
                out_none.append(dom)
            continue

        is_sure = False
        for cook in dom['cookies']:
            if cook['domain'] == '.ioam.de' or \
                cook['domain'] == 'responder.wt-safetag.com' or \
                cook['domain'] == 'm.exactag.com' or \
                (cook['domain'] == '.yandex.com' and cook['name'] == 'i') or \
                (cook['domain'] == '.rubiconproject.com' and cook['name'] == 'rsid') or \
                (cook['domain'] == '.google.com' and cook['name'] == 'NID') or \
                (cook['domain'] == '.doubleclick.net' and cook['name'] == 'IDE') or \
                    (cook['domain'] == '.consensu.org' and cook['name'].startswith('__cmpconsent')):
                if cook['value'] != '':
                    is_sure = True
                    try:
                        counts[cook['domain']] += 1
                    except KeyError:
                        counts[cook['domain']] = 1
                    # break

        for trkr in dom['tracker']:
            if check_is_tracker(trkr):
                is_sure = True
                break

        if is_sure:
            out_sure.append(dom)
            continue

        out_else.append(dom)


print()
print('tracker url but no cookies:', c_ncbu)
for x, y in [('sure', out_sure), ('nocookies', out_none), ('else', out_else)]:
    print(x, ':', len(y))
    with open('abstract-{}.json'.format(x), 'w') as f:
        json.dump(y, f, indent=2)
print()
ccc = sorted(counts.items(), key=lambda x: -x[1] if x[0].startswith('https:')
             else -x[1] * 1000)
for x, y in ccc:
    print('{} ({})  '.format(x, y))
print()
