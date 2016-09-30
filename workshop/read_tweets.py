# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 01:28:21 2016

@author: shubham
"""
import json

tweets_data_path = 'twitter_modi_kejriwal.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue