#!/usr/bin/env python

import sys
import csv
import datetime

START_TIME = datetime.time(9, 0, 0)
FINISH_TIME = datetime.time(17, 0, 0)
STATES = {"new york": {"min_long": -79.7624, "max_long": -71.7517, "min_lat": 40.4772, "max_lat": 45.0153},
          "california": {"min_long": -124.6509, "max_long": -114.1315, "min_lat": 32.5121, "max_lat": 42.0126}}


def check_tweet_time(created_at):
    [date, time] = created_at.split()
    [hours, minutes, seconds] = time.split(":")

    tweet_time = datetime.time(int(hours), int(minutes), int(seconds))
    if START_TIME <= tweet_time <= FINISH_TIME:
        return 1

    return 0


def check_lat_long(lat, long):
    if (STATES["new york"]["min_long"] < long < STATES["new york"]["max_long"]) and (
            STATES["new york"]["min_lat"] < lat < STATES["new york"]["max_lat"]):
        return 1, "new york"
    elif (STATES["california"]["min_long"] < long < STATES["california"]["max_long"]) and (
            STATES["california"]["min_lat"] < lat < STATES["california"]["max_lat"]):
        return 1, "california"


def mapper(row):
    created_at, tweet, lat, long = row[0], row[2], row[13], row[14]
    lat, long = float(lat), float(long)

    # Both Candidate
    if ("#Trump" in tweet or "#DonaldTrump" in tweet) and (
            "#Biden" in tweet or "#JoeBiden" in tweet) and check_tweet_time(created_at):
        res, state = check_lat_long(lat, long)
        if res:
            print(f'{state.lower()}\t {1}\t {0}\t {0}')

    # Donald Trump
    elif ("#Trump" in tweet or "#DonaldTrump" in tweet) and check_tweet_time(created_at):
        res, state = check_lat_long(lat, long)
        if res:
            print(f'{state.lower()}\t {0}\t {0}\t {1}')

    # Joe Biden
    elif ("#Biden" in tweet or "#JoeBiden" in tweet) and check_tweet_time(created_at):
        res, state = check_lat_long(lat, long)
        if res:
            print(f'{state.lower()}\t {0}\t {1}\t {0}')


rows = csv.reader(sys.stdin)
# file = open('../light_dataset/light_dataset.csv', encoding='utf8')
# rows = csv.reader(file)

for row in rows:
    try:
        mapper(row)
    except:
        pass
