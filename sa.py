import pandas as pd
import numpy as np
import json
from nltk.tokenize import sent_tokenize, word_tokenize
import csv
from fuzzywuzzy import fuzz

#input your clean data csv
data = pd.read_csv("YourData.csv")

#load indonesian opinion words
pos = pd.read_csv('pos.csv', delimiter=';')
neg = pd.read_csv('neg.csv', delimiter=';')

#twit to list
twit = []
for row in data.iterrows():
    twit.append(row[1].tweet)

#tokenizing twit to word
word = []
for w in twit:
    word.append(word_tokenize(w))
    
#combining all words into single list
words = []
for w in word:
    for ww in w:
        words.append(ww)

#save the indonesian opinion words in dict
positive = {}
negative = {}
for w in pos.iterrows(): 
    if type(w[1].word) == str:
        positive[w[1].word] = w[1].weight
for w in neg.iterrows():
    if type(w[1].word) == str:
        negative[w[1].word] = w[1].weight

#save the sentiment score per word in list
senpos = []
senneg = []
for w in words:
    for key, val in positive.items():
        if type(w) == str:
            #80% match
            if fuzz.ratio(w,key) > 80:
                senpos.append(val)
    for key, val in negative.items():
        if type(w) == str:
            #80% match
            if fuzz.ratio(w,key) > 80:
                senneg.append(val)

pos_score = sum(senpos)
neg_score = sum(senneg)
#score betweer -5 till +5
sentiment = (pos_score + neg_score) / (len(senpos) + len(senneg))

print(pos_score)
print(neg_score)
print(sentiment) 

print('✅ Process done!')
