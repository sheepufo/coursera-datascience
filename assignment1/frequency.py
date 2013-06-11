#frequency.py
#computes term frequency histogram of livestream twitter data collected by twitterstream.py

import sys
import json

def lines(fp):
    print str(len(fp.readlines()))        
      
def main():
    tweet_file = open(sys.argv[1])
    
    word_count = {}
    
    for line in tweet_file:#main loop, go through each tweet
        tweet = json.loads(line)#get the tweet
        if 'text' in tweet:#tweet actually has the 'text' key
            tweet_text = tweet['text']
            tweet_words = tweet_text.split()
            for word in tweet_words:
                if (word in word_count):
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    
    for word in word_count:
        word_count[word] = word_count[word]/sum(word_count.values())
        print word, word_count[word]
    


if __name__ == '__main__':
    main()
