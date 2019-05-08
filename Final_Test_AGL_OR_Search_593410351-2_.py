# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 14:36:35 2019

@author: singto
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 14:59:21 2019

@author: singto
"""

import nltk 
import nltk.corpus
from collections import Counter
from collections import defaultdict
from nltk import ngrams

listfile=["1.txt","2.txt","3.txt","4.txt","5.txt"] #นำไฟล์เข้ามาเพื่อตัดคำ stopword
data=[] #เก็บคำเอาไว้ใน array
for i in listfile:
    with open(i,"r",encoding="utf-8-sig") as f:
        data.append(f.read())
list_word=[]
for i in data:
    list_word.append(nltk.word_tokenize(i))

stop = set(nltk.corpus.stopwords.words('english')) #ตัดคำในภาษาอังกฤษ
j=0
while j<5: #วนลูปให้ครบไฟล์
    list_word[j]=[i for i in list_word[j] if i not in stop]
    j+=1
wordcount=[]
for i in list_word:
    wordcount.append(dict(Counter(i)))
dictwordall=[]
for i in wordcount:
    dictwordall+=i.keys()
dictwordall=list(set(dictwordall))
my_dict = defaultdict(list)

listall=[]
for i in dictwordall:
    if i in list_word[0]:
        my_dict[i]+=[1]
    if i in list_word[1]:
        my_dict[i]+=[2]
    if i in list_word[2]:
        my_dict[i]+=[3]
    if i in list_word[3]:
        my_dict[i]+=[4]
    if i in list_word[4]:
        my_dict[i]+=[5]
def orword(word1,word2):
    numlist=[]
    if word1 in my_dict or word2 in my_dict:
     v1=my_dict[word1]
     v2=my_dict[word2]
     for i in v1:
         if i in v2:
             numlist.append(i)
    return "This word is in : "+str(numlist)

print('Input word:');
a = input();
print('Input word');
b=input();
print('Input grams');
c=input();
list_ngram = ngrams(list(a), int(c))
print(list(list_ngram))

list_word_ngram=[]
for i in list_ngram:
    string=""
    for j in i:
        list_word_ngram.append(string)
list_ngram=list_word_ngram

     
from nltk.corpus import words
english_word=list(words.words())[100:]

list_ngram_word=[]
for i,data in enumerate(list_ngram):
    list_ngram_word.append([])
    for j in english_word:
        if data in j:
            list_ngram_word[i].append(j)
            
list_ngram = ngrams(list(b), int(c))
print(list(list_ngram))

list_word_ngram=[]
for i in list_ngram:
    string=""
    for j in i:
        list_word_ngram.append(string)
list_ngram=list_word_ngram

     
from nltk.corpus import words
english_word=list(words.words())[100:]

list_ngram_word=[]
for i,data in enumerate(list_ngram):
    list_ngram_word.append([])
    for j in english_word:
        if data in j:
            list_ngram_word[i].append(j)
            
            
print(list_word_ngram)            
print(orword(a,b))