#!/usr/bin/env python

import sys


kind_dict = {"Both Candidate": {"likes": 0, "retweets": 0, "web": 0, "iphone": 0, "android": 0},
             "Donald Trump": {"likes": 0, "retweets": 0, "web": 0, "iphone": 0, "android": 0},
             "Joe Biden": {"likes": 0, "retweets": 0, "web": 0, "iphone": 0, "android": 0}}

for line in sys.stdin:
    line.strip()
    kind, likes, retweets, web, iphone, android = line.split("\t")
    likes = int(float(likes))
    retweets = int(float(retweets))
    web = int(float(web))
    iphone = int(float(iphone))
    android = int(float(android))

    kind_dict[kind]["likes"] += likes
    kind_dict[kind]["retweets"] += retweets
    kind_dict[kind]["web"] += web
    kind_dict[kind]["iphone"] += iphone
    kind_dict[kind]["android"] += android

for kind, kind_info in kind_dict.items():
    kind_info_str = '\t'.join(map(str, kind_info.values()))
    print(f'{kind}\t {kind_info_str}')
