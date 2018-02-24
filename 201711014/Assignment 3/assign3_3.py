#Named Entity Extraction using Spacy


import spacy
import csv
import en_core_web_sm
import pandas as pd

nlp = en_core_web_sm.load()

#uploading the csv file

df = pd.read_csv('C:\\Anaconda\\albums.csv')
print("\n")

#NEE of Album Name

print("Named Entity Extraction on Album Name")

for item in df['album']:
    doc=nlp(item)
    for ent in doc:
        print(ent.text,'/',ent.label_)

print("\n")

#NEE of Artists

print("Named Entity Extraction on Artist")
for item1 in df['artist']:
    doc=nlp(item1)
    for ent in doc:
	print(ent.text,'/',ent.label_)

print("\n")

#NEE of Genres

print("Named Entity Extraction on Genre")
for item1 in df['genre']:
    doc=nlp(item1)
    for ent in doc:
        print(ent.text,'/',ent.label_)          
