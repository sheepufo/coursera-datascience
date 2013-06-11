import sys
import json

tweet_file = open(sys.argv[1])
    
tweets = []
for line in tweet_file:
    tweet = json.loads(line)
    tweet_hashtags = tweet.get('entities', {}).get('hashtags')
    if type(tweet_hashtags) == type([]):
       for tag in tweet_hashtags:
           print tag['text']
           print type(tag['text'])
    
    
#print type(tweet)
#print tweet['place']
#print tweets[6]['text']
"""tweet_6 = tweets[6]['text'].split()
print tweets[7]['text']
tweet_7 = tweets[7]['text'].split()
print tweets[8]['text']
tweet_8 = tweets[8]['text'].split()

tweet_words.append(tweet_6)
print tweet_words

for word in tweet_words:
    print word   
    """
  
    