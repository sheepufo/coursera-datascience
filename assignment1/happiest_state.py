#happiest_state.py
#Returns the name of the happiest state as a string

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
    
def get_state(tweet):
    #returns the string of state abbreviation
    #returns " " if no determinable state
    tweet_user = tweet.get('user')
    if type(tweet_user) is dict:
        tweet_loc = tweet_user.get('location')
        ll = len(tweet_loc)
        if len(tweet_loc) > 4 and tweet_loc[ll-3] == ' ' and tweet_loc[ll-4] == ',':
            state_id = tweet_loc[ll-2:ll]
            return state_id
    else:
        return ' '
      
def main():
    sent_file = open(sys.argv[1])#read in sent. vals
    tweet_file = open(sys.argv[2])#read in tweets
    
    scores = parse_sentiment(sent_file)
    key_terms = set(scores.keys())
    
    state_scores = {}#dict for state ids and scores
    tweet_scores = []#store tweet scores
    for line in tweet_file:#main loop, go through each tweet
        tweet = json.loads(line)#get the tweet
        this_score = 0
        if 'text' in tweet:#tweet actually has the 'text' key
            tweet_text = tweet['text']
            sentiment_words = parse_tweet(tweet_text, key_terms)#get the meaningful words
            for word in sentiment_words:
                this_score += scores[word]#get the summed score
        tweet_scores.append(str(this_score))#append score to list
        
        #update state dict with score
        state = get_state(tweet)
        if state != ' ':
            if state in state_scores:
                state_scores[state] += this_score
            else:
                state_scores[state] = this_score
    
    #get max of state scores
    sorted_scores = sorted(state_scores, key=state_scores.get, reverse=True)
    print state_scores['CA']
    print sorted_scores[2]
    

        


if __name__ == '__main__':
    main()