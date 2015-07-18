#!/usr/bin/env bash

# example of the run script for running the word count
cat ./tweet_input/tweets.txt | ./src/mapper.py | ./src/reducer.py > ./tweet_output/ft1.txt
# example of the run script for running the word count
cat ./tweet_input/tweets.txt | ./src/median.py > ./tweet_output/ft2.txt

# I'll execute my programs, with the input directory tweet_input and output the files in the directory tweet_output
# python ./src/words_tweeted.py ./tweet_input/tweets.txt ./tweet_output/ft1.txt
# python ./src/median_unique.py ./tweet_input/tweets.txt ./tweet_output/ft2.txt