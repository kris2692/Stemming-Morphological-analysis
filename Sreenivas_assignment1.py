#Name: KRISHNA SREENIVAS    
#Student ID: 800984436

# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 11:03:43 2017

@author: krish, ver: 1.0.0
"""

import re
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import *
from nltk import FreqDist
import json

def split_string(string):
    temp=string.split()
    return temp

################################
def split_word(string):
    for i in range(len(string)):
        if i==1:
            return string[i]

################################
def splitting_till_sleep(string):
    temp=split_string(funny)
    phrase=temp[:temp.index('sleep')]
    return phrase

################################
def joining_back_phrases(string):
    temp=' '.join(string)
    print(temp)

################################
def print_words_alpha():
    for word in sorted(temp):
        print(word)

################################
def word_freq_order():
    string3=input("Enter a string\n")
    t2=string3.split()
    for word in sorted(set(t2)):
        print("Word: ",word," Frequency: ",t2.count(word))
    print("Words in sentence: ", t2,"Total no. of words: ", len(t2))

################################
def email_locator(string):
    print("\n Following is the text \n")
    print(string,"\n")
    regex='[\w\.]+@[\w.]+'
    email=list(re.findall(regex,string))
    print("Below is the list of email ids \n")
    for ids in email:
        print(ids)

################################
def duplicate_lines_removal():
    text=input("Enter filename:")
    string=[]
    temp=[]
    file=open(text,'r')
    for line in file:
        string.append(line)
    sentences=nltk.sent_tokenize(' '.join(string))
    for line in sentences:
        if line not in temp:
            temp.append(line)
    file=open("output.txt","w")
    for line in temp:
        file.write(line)
    print(temp)
    file.close()
    
#################################
def assign_statements_speaker():
    regex='\(\w+\)'
    patterns=[]
    text=[]
    debate_text=[]
    file=open('debate.txt','r')
    for line in file:
        temp = re.findall(regex,line)
        if temp != []:
            patterns.append(temp[0])
        text.append(line)
    
    patterns = set(patterns)
    for sent in text:
        for pattern in patterns:
            sent=sent.replace(pattern,'')
        debate_text.append(sent)
        
    debate_text=[sent for sent in debate_text if len(sent)>1]
    debate_text=debate_text[6:448]
    prev_speaker=''
    for sent in debate_text:
        speaker=re.match('^[A-Z]+:',sent)
        if speaker:
            speakername=speaker.group().lower()[:-1]
            if speakername=='lehrer':
                lehrer.append(sent[8:])
            elif speakername=='romney':
                romney.append(sent[8:])
                
            elif speakername=='obama':
                obama.append(sent[7:])
            prev_speaker=speakername
        else:
            if prev_speaker=='lehrer':
                lehrer.append(sent)
            elif prev_speaker=='romney':
                romney.append(sent)
            elif prev_speaker=='obama':
                obama.append(sent)
    file.close()
    
################################

def preprocess(array):
    speaker_words=[]
    speaker=[]
    for i in range(len(array)):
        speaker=re.sub(r'[^a-zA-Z_ ]','',array[i])
        tokens=nltk.word_tokenize(speaker)
        speakers=[w.lower() for w in tokens if not re.fullmatch('[' + string.punctuation + ']+', w)]
        speaker_words.append([w for w in speakers if w not in stopwords.words("english")])
    return speaker_words   

################################
#Stemming and frequency calculation

def freq_dist(array):
    fdist=FreqDist(array)
    print(fdist.most_common(10))
    return fdist

def porter_stemmer(array):
    porter_words=[]
    top_porter_words=[]
    pstemmer=PorterStemmer()
    for sent in array:
        porter_words.append([pstemmer.stem(plural) for plural in sent ])
    for i in range(len(porter_words)):
        for word in porter_words[i]:
            top_porter_words.append(word)
    freq_dist(top_porter_words)
    return top_porter_words

def snowball_stemmer(array):
    snowball_words=[]
    top_snowball_words=[]
    sstemmer=SnowballStemmer('english')
    for sent in array:
        snowball_words.append([sstemmer.stem(plural) for plural in sent])
    for i in range(len(snowball_words)):
        for word in snowball_words[i]:
            top_snowball_words.append(word)
    freq_dist(top_snowball_words)
    return top_snowball_words

def lancaster_stemmer(array):
    lancaster_words=[]
    top_lancaster_words=[]
    lstemmer=LancasterStemmer()
    for sent in array:
        lancaster_words.append([lstemmer.stem(plural) for plural in sent])
    for i in range(len(lancaster_words)):
        for word in lancaster_words[i]:
            top_lancaster_words.append(word)
    freq_dist(top_lancaster_words)
    return top_lancaster_words

def positive_porter_stemmer(array):
    porter_positive_words=[]
    pstemmer=PorterStemmer()
    for line in array:
        porter_positive_words.append(pstemmer.stem(line))
    porter_words=list(sorted(set(porter_positive_words)))
    return porter_words
        
################################
#loading positive words dictionary file

def load_positive_words():
    positive_words=[]
    with open('positive.txt',mode='r') as file:
        for line in file:
            line=line.rstrip()
            positive_words.append(line)
        return positive_words

################################
#obtaining top 10 positive words of speaker

def compare_positive_words(array):
    top_positive_words=[]
    for word in sorted(array):
        for pos_word in sorted(positive_porter_words):
            if word==pos_word:
                top_positive_words.append(word)
    return freq_dist(top_positive_words)
    
################################
#word rate
def word_rate(array):
    positive_words=[]
    for word in sorted(array):
        for pos_word in sorted(positive_porter_words):
            if word==pos_word:
                positive_words.append(word)
    print("Number of positive words: ",len(list(set(positive_words))))
    return list(set(positive_words))

################################
################################
#function calling

funny='colorless green ideas sleep furiously'
print("\n----Problem 1a----")
print(split_string(funny))
print("\n----Problem 1b----")
temp=split_string(funny)
t1=[]
for word in temp:
    t1.append(split_word(word))
print(''.join(t1))
print("\n----Problem 1c----")
phrase=splitting_till_sleep(funny)
print(phrase)
print("\n----Problem 1d----")
joining_back_phrases(phrase)
print("\n----Problem 1e----")
print_words_alpha()
print("\n----Problem 2----")
word_freq_order()
print("\n----Problem 3----")
print("Regex for locating determiners is: \\b\s(a|an|the)\s")
print("Regex for capturing arithmetic expression is \d*[\*|\+]\d*[\*|\+]\d+")
text="... austen-emma.txt:hart@vmd.cso.uiuc.edu (internet) hart@uiucvmd (bitnet)... austen-emma.txt:Internet (72600.2026@compuserve.com); TEL: (212-254-5093) ... austen-persuasion.txt:Editing by Martin Ward (Martin.Ward@uk.ac.durham)...blake-songs.txt:Prepared by David Price, email ccx074@coventry.ac.uk ..."
print("\n----Problem 4----")
email_locator(text)
print("\n----Problem 5----")
duplicate_lines_removal()
print("\n----Problem 6----")
print("The provided code reads a file. If a blank line or a '#' is encountered at the start of the line, the program terminates. The re.sub command replaces the opening braces () with '(.' and ').'. The final for loop returns text present within the parenthesis.\nSo, the input file should contain text present within the parenthesis, so that the text between them could be retrieved\n")
print("\n----Problem 7a----")
print("Please wait...")
romney=[]
obama=[]
lehrer=[]
assign_statements_speaker()
print("Statements assigned to speakers")
print("\n----Problem 7b & 7c----")
print("Please wait...")
lehrer_words=preprocess(lehrer)
romney_words=preprocess(romney)
obama_words=preprocess(obama)
print("Text preprocessed")
print("\n---* Top words used by Lehrer and its frequencies *---")
print("\n Porter Stemmer")
porter_lehrer_stem_words=porter_stemmer(lehrer_words)
print("\n Snowball Stemmer")
snowball_lehrer_stem_words=snowball_stemmer(lehrer_words)
print("\n Lancaster Stemmer")
lancaster_lehrer_stem_words=lancaster_stemmer(lehrer_words)


print("\n---* Top words used by Romney and its frequencies *---")
print("\n Porter Stemmer")
porter_romney_stem_words=porter_stemmer(romney_words)
print("\n Snowball Stemmer")
snowball_romney_stem_words=snowball_stemmer(romney_words)
print("\n Lancaster Stemmer")
lancaster_romney_stem_words=lancaster_stemmer(romney_words)


print("\n---* Top words used by Obama and its frequencies *---")
print("\n Porter Stemmer")
porter_obama_stem_words=porter_stemmer(obama_words)
print("\n Snowball Stemmer")
snowball_obama_stem_words=snowball_stemmer(obama_words)
print("\n Lancaster Stemmer")
lancaster_obama_stem_words=lancaster_stemmer(obama_words)


print("\n----Problem 7d----")
positive_words=load_positive_words() 
print("\n Positive words loaded from file...")
positive_porter_words=positive_porter_stemmer(positive_words)
print("\n Porter stemmed the positive words...")


print("\n----Problem 7e----")
print("\n Top positive words of Lehrer")
with open('lehrer.json','w') as lehrer_file:
    json.dump(compare_positive_words(porter_lehrer_stem_words),lehrer_file)
print("\n Top positive words of Romney")
with open('romney.json','w') as romney_file:
    json.dump(compare_positive_words(porter_romney_stem_words),romney_file)
print("\n Top positive words of Obama")
with open('obama.json','w') as obama_file:
    json.dump(compare_positive_words(porter_obama_stem_words),obama_file)

print("\n----Problem 7f----")
print("\nLehrer Statistics")
word_rate(porter_lehrer_stem_words)
print("\nRomney Statistics")
word_rate(porter_romney_stem_words)
print("\nObama Statistics")
word_rate(porter_obama_stem_words)


