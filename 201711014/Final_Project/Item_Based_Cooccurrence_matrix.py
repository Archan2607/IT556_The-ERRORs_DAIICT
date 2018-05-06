#importing necessary libraries



import pandas
from sklearn.cross_validation import train_test_split
import numpy as np
import os,sys
import time
from sklearn.externals import joblib
import Recommenders as Recommenders #Recommenders.py library has been uploaded along with this file in final project

#Read userid-songid-listen_count triplets
#This step might take time to download data from external sources
triplets_file = 'https://static.turi.com/datasets/millionsong/10000.txt'
songs_metadata_file = 'https://static.turi.com/datasets/millionsong/song_data.csv'

song_df_1 = pandas.read_table(triplets_file,header=None)
song_df_1.columns = ['user_id', 'song_id', 'listen_count']

#Read song  metadata
song_df_2 =  pandas.read_csv(songs_metadata_file)

#Merge the two dataframes above to create input dataframe for recommender systems
song_df = pandas.merge(song_df_1, song_df_2.drop_duplicates(['song_id']), on="song_id", how="left")


print(song_df.head()) #Lists out features of the dataset

print(len(song_df))  #prints length of the song dataset

song_df = song_df.head(10000)

#Merge song title and artist_name columns to make a merged column
song_df['song'] = song_df['title'].map(str) + " - " + song_df['artist_name']

song_grouped = song_df.groupby(['song']).agg({'listen_count': 'count'}).reset_index()
grouped_sum = song_grouped['listen_count'].sum()
song_grouped['percentage']  = song_grouped['listen_count'].div(grouped_sum)*100
song_grouped.sort_values(['listen_count', 'song'], ascending = [0,1])

#unique Users
users=song_df['user_id'].unique()

print(len(users)) #prints number of unique users

#Unique songs
songs=song_df['song'].unique()

print(len(songs)) #prints number of unique songs

#Song Recommender
train_data, test_data = train_test_split(song_df, test_size = 0.20, random_state=0)
print(train_data.head(5))

#Recommenders.popularity_recommender_py

pm = Recommenders.popularity_recommender_py()
pm.create(train_data, 'user_id', 'song')

user_id = users[5]
pm.recommend(user_id)

###Fill in the code here
user_id = users[7]
pm.recommend(user_id)

#Recommenders.item_similarity_recommender_py
#Personalized algorithm

is_model = Recommenders.item_similarity_recommender_py()
is_model.create(train_data, 'user_id', 'song')

#Print the songs for the user in training data
user_id = users[5]
user_items = is_model.get_user_items(user_id)
#
print("------------------------------------------------------------------------------------")
print("Training data songs for the user userid: %s:" % user_id)
print("------------------------------------------------------------------------------------")

for user_item in user_items:
    print(user_item)

print("----------------------------------------------------------------------")
print("Recommendation process going on:")
print("----------------------------------------------------------------------")

#Recommend songs for the user using personalized model
is_model.recommend(user_id)


user_id = users[7]
#Fill in the code here
user_items = is_model.get_user_items(user_id)
#
print("------------------------------------------------------------------------------------")
print("Training data songs for the user userid: %s:" % user_id)
print("------------------------------------------------------------------------------------")

for user_item in user_items:
    print(user_item)

print("----------------------------------------------------------------------")
print("Recommendation process going on:")
print("----------------------------------------------------------------------")

#Recommend songs for the user using personalized model
is_model.recommend(user_id)


#Using model to fetch similiar songs to any song u type
is_model.get_similar_items(['Fix You - Coldplay'])

