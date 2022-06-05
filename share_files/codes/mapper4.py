#!/usr/bin/env python

import sys
import csv


def check_source(source):
    web_app, iphone, android = 0, 0, 0
    if "Twitter Web App" in source:
        web_app = 1
    elif "Twitter for iPhone" in source:
        iphone = 1
    elif "Twitter for Android" in source:
        android = 1

    return f'{web_app}\t {iphone}\t {android}'


def mapper(row):
    tweet, likes, retweet, source = row[2], row[3], row[4], row[5]

    # Both Candidate
    if ("#Trump" in tweet or "#DonaldTrump" in tweet) and ("#Biden" in tweet or "#JoeBiden" in tweet):
        print(f'Both Candidate\t {likes}\t {retweet}\t {check_source(source)}')

    # Donald Trump
    elif "#Trump" in tweet or "#DonaldTrump" in tweet:
        print(f'Donald Trump\t {likes}\t {retweet}\t {check_source(source)}')

    # Joe Biden
    elif "#Biden" in tweet or "#JoeBiden" in tweet:
        print(f'Joe Biden\t {likes}\t {retweet}\t {check_source(source)}')


# file = open('../light_dataset/light_dataset.csv', encoding='utf8')
# rows = csv.reader(file)

rows = csv.reader(sys.stdin)

for row in rows:
    try:
        mapper(row)
    except:
        pass
