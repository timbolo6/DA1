#!/usr/bin/env python3
"""mapper.py"""

import sys
#Load Tweets
import json
import pandas as pd
import re
# Load and parse JsonObject from text file
def read_input():
    tweets_list = []
    for jsonObject in sys.stdin:
        #Ignore Space in text file
        if not jsonObject.isspace():
                tweets_Dict = json.loads(jsonObject)
                tweets_list.append(tweets_Dict)

    tweet_data_frame = pd.DataFrame.from_dict(tweets_list)
    # Lowercase of column "TEXT"
    tweet_data_frame["text"] = tweet_data_frame["text"].apply(lambda str: str.lower())
    # Delete Retweets based on retweeted attribute
    tweet_unique = tweet_data_frame[tweet_data_frame.retweeted == False]
    return tweet_unique["text"]

def mapper():
    # Pattern of word allows no letter from a to z before and after the word 
    hen_patter = re.compile("[^a-z]hen[^a-z]")
    han_patter = re.compile("[^a-z]han[^a-z]")
    hon_patter = re.compile("[^a-z]hon[^a-z]")
    den_patter = re.compile("[^a-z]den[^a-z]")
    det_patter = re.compile("[^a-z]det[^a-z]")
    denna_patter = re.compile("[^a-z]denna[^a-z]")
    denne_patter = re.compile("[^a-z]denne[^a-z]")
    inputstream = read_input()
    for index, line in inputstream.iteritems():
        # Hen Patter
        if hen_patter.search(line):
            print("hen\t1")
        # “han” Patter
        if han_patter.search(line):
            print("han\t1")
        # HON
        if hon_patter.search(line):
            print("hon\t1")
        # DEN
        if den_patter.search(line):
            print("den\t1")
        # DET
        if det_patter.search(line):
            print("det\t1")
        # DENNA
        if denna_patter.search(line):
            print("denna\t1")
        # DENNE
        if denne_patter.search(line):
            print("denne\t1")

if __name__ == "__main__":
    # input comes from STDIN (standard input)
    mapper()
