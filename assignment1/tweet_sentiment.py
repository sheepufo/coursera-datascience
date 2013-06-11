import sys
import json

def lines(fp):
    print str(len(fp.readlines()))
    
def parse_sentiment(file):
    #takes tab delimited file, makes dictionary
    scores={}
    for line in file:
        term, score = line.split("\t") #tab delimited file
        scores[term] = int(score) #store score with key term
    return scores 
    
def parse_tweet(tweet_text, key_words):
    #takes the text of the tweet and returns words from sent_file
    tweet_words = tweet_text.lower().split()
    sent_words = []
    for word in tweet_words:
        if(word in key_words):
            sent_words.append(word)
    return sent_words      
    
      
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    scores = parse_sentiment(sent_file)
    key_terms = set(scores.keys())
    
    tweet_scores = []
    for line in tweet_file:#main loop, go through each tweet
        tweet = json.loads(line)#get the tweet
        this_score = 0
        if 'text' in tweet:#tweet actually has the 'text' key
            tweet_text = tweet['text']
            sentiment_words = parse_tweet(tweet_text, key_terms)#get the meaningful words
            for word in sentiment_words:
                this_score += scores[word]#get the summed score
        tweet_scores.append(str(this_score))#append score to list
    
    for score in tweet_scores:
        print int(score)#print scores to stdout
        


if __name__ == '__main__':
    main()
    
