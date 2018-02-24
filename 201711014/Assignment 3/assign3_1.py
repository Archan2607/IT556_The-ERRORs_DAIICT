#Noun Extraction Using Spacy

import spacy
import csv
import en_core_web_sm
import pandas as pd

nlp = en_core_web_sm.load()

#Uploading CSV File

df = pd.read_csv('C:\\Anaconda\\albums.csv')
print("\n")


#Noun Extraction on Album Names

print("Noun Extraction on Album Name")
df1 = df['album'].apply(nlp)
for temp in df1:
        for chunk in temp.noun_chunks:
          print(chunk.root.text)
print("\n")

#Noun Extraction on Artists

print("Noun Extraction on Artists")          
df2 = df['artist'].apply(nlp)
for temp in df2:
        for chunk in temp.noun_chunks:
          print(chunk.root.text)
print("\n")

#Noun Extraction on Genres

print("Noun Extraction on Genres")
df3 = df['genre'].apply(nlp)
for temp in df3:
        for chunk in temp.noun_chunks:
          print(chunk.root.text)
          
