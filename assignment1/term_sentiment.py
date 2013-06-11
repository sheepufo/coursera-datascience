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
    
def remove_words(tweet_text, words_to_remove):
    #removes words_to_remove from tweet_text, returns remaining words as list
    rest_of_words = [words for words in tweet_text.lower().split() if words not in words_to_remove ]
    return rest_of_words          
    
      
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    scores = parse_sentiment(sent_file)
    key_terms = set(scores.keys())
    
    non_afinn = {}#dictionary for new words
    tweet_scores = []
    for line in tweet_file:#main loop, go through each tweet
        tweet = json.loads(line)#get the tweet
        this_score = 0
        if 'text' in tweet:#tweet actually has the 'text' key
            tweet_text = tweet['text']
            sentiment_words = parse_tweet(tweet_text, key_terms)#get the meaningful words
            other_words = remove_words(tweet_text, sentiment_words)
            for word in sentiment_words:
                this_score += scores[word]#get the summed score
            for word in other_words:
                #if other word already in dictionary, increment
                if (word in non_afinn):
                    non_afinn[word]+=this_score
                #otherwise add it and the sentiment score
                else:
                    non_afinn[word] = this_score
        tweet_scores.append(this_score)#append score to list
        
    for key in non_afinn:
        print key, non_afinn[key]
        
    
    
        



if __name__ == '__main__':
    main()
