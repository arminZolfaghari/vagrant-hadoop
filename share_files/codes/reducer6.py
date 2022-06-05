#!/usr/bin/env python

import sys

state_dict = {"new york": {"Both Candidate": 0, "Joe Biden": 0, "Donald Trump": 0, "sum": 0},
              "california": {"Both Candidate": 0, "Joe Biden": 0, "Donald Trump": 0, "sum": 0}}


for line in sys.stdin:
    line.strip()
    state, tw_both_candidate, tw_joe_biden, tw_donald_trump = line.split("\t")

    if state in state_dict:
        state_dict[state]["Both Candidate"] += int(tw_both_candidate)
        state_dict[state]["Joe Biden"] += int(tw_joe_biden)
        state_dict[state]["Donald Trump"] += int(tw_donald_trump)
        state_dict[state]["sum"] += 1


for state, state_info in state_dict.items():
    all_tweets = state_info["sum"]
    both_candidate_percentage = state_info["Both Candidate"] / all_tweets
    joe_biden_percentage = state_info["Joe Biden"] / all_tweets
    donald_trump_percentage = state_info["Donald Trump"] / all_tweets
    print(f'{state}\t {both_candidate_percentage}\t {joe_biden_percentage}\t {donald_trump_percentage}\t {all_tweets}')