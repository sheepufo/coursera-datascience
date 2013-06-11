import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
pyresponse = json.load(response)

#print type(pyresponse)

#print pyresponse.keys()
results = pyresponse["results"]
"""print type(results)
print results[0]['text']
print type(results[0]['text'])
print results[0]['text'].lower()
"""
#print results[0]
#for i in range(10):
 #   print results[i]["text"]
 
 #get afinn words, make a set
 
afinnfile = open("AFINN-111.txt")
scores={}
for line in afinnfile:
    term, score = line.split("\t") #tab delimited file
    scores[term] = int(score) #store score with key term 
key_terms = set(scores.keys())
print type(key_terms)

results[0]['text'].lower()
tweet_words = results[0]['text'].lower().split()
print "Type of tweet words:"
print type(tweet_words)
print tweet_words
sent_words=[]
for word in tweet_words:
    if(word in key_terms):
        sent_words.append(word)
    print word    
#sent_words = " ".join(word for word in tweet_words if word in key_terms)
print type(sent_words)
print sent_words
print len(sent_words)


a = {}
a["Devin"]="math"
a["jeff"] = "neuroscience"
for key in a:
    print key, a[key]

   
   
 
 
 
 
 
 
 