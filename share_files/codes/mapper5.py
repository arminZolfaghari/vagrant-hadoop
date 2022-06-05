#!/usr/bin/env python

import sys
import csv
import datetime

START_TIME = datetime.time(9, 0, 0)
FINISH_TIME = datetime.time(17, 0, 0)
STATES = ["new york", "texas", "california", "florida"]


#
# def convert_time_to_24_hour(time):
#     '''
#     :param time: time 12-hour
#     :param period: AM or PM
#     :return: time 24-hour
#     '''
#     [hours, minutes, seconds] = time.split(':')
#     # if period == "PM":
#     #     hours += 12
#
#     return [int(hours), int(minutes), int(seconds)]


def check_tweet_time(created_at):
    [date, time] = created_at.split()
    [hours, minutes, seconds] = time.split(":")

    tweet_time = datetime.time(int(hours), int(minutes), int(seconds))
    if START_TIME <= tweet_time <= FINISH_TIME:
        return 1

    return 0


# print(check_tweet_time("10/15/2020  8:01:23 AM"))
# exit()

def check_state(state):
    if state.lower() in STATES:
        return 1
    return 0


def mapper(row):
    created_at, tweet, state = row[0], row[2], row[18]
    # print(created_at)

    # Both Candidate
    if ("#Trump" in tweet or "#DonaldTrump" in tweet) and (
            "#Biden" in tweet or "#JoeBiden" in tweet) and check_tweet_time(created_at) and check_state(state):
        print(f'{state.lower()}\t {1}\t {0}\t {0}')

    # Donald Trump
    elif ("#Trump" in tweet or "#DonaldTrump" in tweet) and check_tweet_time(created_at) and check_state(state):
        print(f'{state.lower()}\t {0}\t {0}\t {1}')

    # Joe Biden
    elif ("#Biden" in tweet or "#JoeBiden" in tweet) and check_tweet_time(created_at) and check_state(state):
        print(f'{state.lower()}\t {0}\t {1}\t {0}')


rows = csv.reader(sys.stdin)
# file = open('../light_dataset/light_dataset.csv', encoding='utf8')
# rows = csv.reader(file)

for row in rows:
    try:
        mapper(row)
    except:
        pass
