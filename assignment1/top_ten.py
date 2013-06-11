#top_ten.py
#computes the ten most frequently occurring hash tags from twitter data file

import sys
import json
from collections import defaultdict

def lines(fp):
    print str(len(fp.readlines()))
    
def get_hashtags(tweet):
    #returns a list of the hashes in the tweet
    hashtags = []
    tweet_hashtags = tweet.get('entities',{}).get('hashtags')
    if type(tweet_hashtags) == type([]):
       for tag in tweet_hashtags:
           tag_text = tag['text']
           hashtags.append(tag_text)
    return hashtags
             

      
def main():
    tweet_file = open(sys.argv[1])
    
    hashtag_dict = defaultdict(int)
    tweet_scores = []
    for line in tweet_file:#main loop, go through each tweet
        tweet = json.loads(line)#get the tweet
        new_tags = get_hashtags(tweet)
        for tag in new_tags:
            hashtag_dict[tag] += 1
    
    #print the top 10 hashtags in the tweets in the file
    i=0        
    for key, value in sorted(hashtag_dict.items()):
        if i == 10:
            break
        else:
            print key, value
        i+=1    


if __name__ == '__main__':
    main()