import spacy
import csv
import en_core_web_sm
import pandas as pd

nlp = en_core_web_sm.load()

df = pd.read_csv('C:\\Anaconda\\albums.csv')
print("\n")
print("Lemmatization on Album Name")

for item in df['album']:
    doc=nlp(item)
    #print(doc)
    for token in doc:
        print(token.text, token.lemma_)

print("\n")
print("Lemmatization on Artist")
for item1 in df['artist']:
    doc=nlp(item1)
    #print(doc)
    for token in doc:
        print(token.text, token.lemma_)

print("\n")
print("Lemmatization on Genre")
for item1 in df['genre']:
    doc=nlp(item1)
    #print(doc)
    for token in doc:
        print(token.text, token.lemma_)          