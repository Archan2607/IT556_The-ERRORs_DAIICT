import json
import requests
from elasticsearch import Elasticsearch
from collections import namedtuple

INDEX_NAME='music_data'

es = Elasticsearch([{
    'host': 'localhost',
    'port': 9200
}])


# 1.Boolean FOormation

#Query to display all the albums released till today by 'The Beatles'

res = es.search(index=INDEX_NAME, body={
    "query": {
    "bool": {
      "must":
        { "match": { "Artist": "The Beatles"}}
    }
  }
})
#print(" response: '%s'" % (res))

# Query to display all the albums with Genre as 'Rock'

res = es.search(index=INDEX_NAME, body={

    "query": {
    "bool": {
      "must":
        { "match": { "Genre": "Rock"}}
    }
  }
})
#print(" response: '%s'" % (res))


# Query to display albums by 'The Beach Boys' in the Genre 'Rock' , released after '1965'
res = es.search(index=INDEX_NAME, body={
    "query": {

        "bool": {
            "must": {
                "match": {"Genre": "Rock"}
            },
            "filter": {
                "match": {"Artist": "The Beach Boys"}
            },
            "must_not": {
                "range": {
                    "Year": {"lte": 1965}
                }
            }
        }
    }
})
#print(" response: '%s'" % (res))








# 2.BOOSTING

res = es.search(index=INDEX_NAME, body={
    "query": {
        "boosting": {
            "positive": {
                "term": {
                    "Year": "1990"
                }
            },
            "negative": {
                "term": {
                    "Genre": "Rock"
                }
            },
            "negative_boost": 0.4
        }

    }
})
#print(" response: '%s'" % (res))

#3. MIinimum_Should_Match

# Query to display with minimum_should_match as 1.
#Display results where artist is 'Marvin Gayle' or genre is 'Funk/Soul' or year of release is '1971'

res = es.search(index=INDEX_NAME, body={
    "query": {

        "bool": {

            "should": [
                {"match": {"Artist":"Marvin Gayle"}},
                {"match": {"Genre": "Funk / Soul"}},
                {"match": {"Year": 1971}}
            ],
            "minimum_should_match": 1

        }
    }
})
#print(" response: '%s'" % (res))


#Query to display with minimum_should_match as 3.
#Display results where artist is 'Marvin Gayle' and genre is 'Funk/Soul' and year of release is '1971'

res = es.search(index=INDEX_NAME, body={
    "query": {

        "bool": {

            "should": [
                {"match": {"Artist":"Marvin Gayle"}},
                {"match": {"Genre": "Funk/Soul"}},
                {"match": {"Year": 1971}}
            ],
            "minimum_should_match": 3

        }
    }
})
#print(" response: '%s'" % (res))

#Query to display all albums of genre 'Jazz' in the year '1959' using minimun_should_match

res = es.search(index=INDEX_NAME, body={
    "query": {

        "bool": {

            "should": [
                {"match": {"Genre": "Jazz"}},
                {"match": {"Year": 1959}}
            ],
            "minimum_should_match": 2

        }
    }
})
#print(" response: '%s'" % (res))
