#I used csv files from the given reference Link:  https://github.com/woodm1979/CsvMusicApi

import elasticsearch
import json
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import csv
import time
import sys
reload(sys)  
sys.setdefaultencoding('Cp1252')

es=Elasticsearch([{"host" : "127.0.0.1", "port" : 9200}])
mapping = {
	"mappings" : {
		"album" : {
		  "properties" : {
			"album" : {
			  "type" : "text",
			  "index_options" : "docs"
			},
			"artist" : {
			  "type" : "text",
			  "index_options" : "docs"
			},
			"genre" : {
			  "type" : "text",
			  "index_options" : "docs"
			},
			"year" : {
			  "type" : "long",
			}
		  }
		}
	}
}

q1 = {
	"query" : {
		"match" : {
			"album" : "ANTI"
		}
	}
}

q2 = {
	"query" : {
		"range" : {
			"year" : {
				"gte" : 2014
			}
		}
	}
}

q3 = {
	"query" : {
		"bool" : {
			"must" : [
				{
					"range" : {
						"Year" : {
							"gte" : 1975,
							"lte" : 2001
						}
					}
				},
				{
					"match" : {
						"Artist" : {
							"query" : "Rihanna",
							"operator" : "and"
						}
					}
				}
			]
		}
	}
}



es.indices.create(index = 'albums', body = mapping)

with open('albums.csv') as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index='songs', doc_type='album')

time.sleep(2)
	
print ("q1")
print(json.dumps(es.search(index = "albums", doc_type = "album", body = q1), indent = 2))	#search album "ANTI"
print ("q2")
print(json.dumps(es.search(index = "songs", doc_type = "album", body = q2), indent = 2))	#search albums released after 2014
print ("q3")
print(json.dumps(es.search(index = "songs", doc_type = "album", body = q3), indent = 2))	#search for albums having artists named"Rihanna" released in 1975-2001


#Outputs:

q1
{
  "took": 331,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 0,
    "max_score": null,
    "hits": []
  }
}
q2
{
  "took": 247,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 15,
    "max_score": 1.0,
    "hits": [
      {
        "_index": "songs",
        "_type": "album",
        "_id": "rnSaqWEBv7UBv9hU3TdJ",
        "_score": 1.0,
        "_source": {
          "album": "Little Seeds",
          "artist": "Shovels & Rope",
          "genre": "Folk",
          "year": "2016"
        }
      },
      {
        "_index": "songs",
        "_type": "album",
        "_id": "7nSaqWEBv7UBv9hU3TdJ",
        "_score": 1.0,
        "_source": {
          "album": "Dirty Heads",
          "artist": "Dirty Heads",
          "genre": "Reggae",
          "year": "2016"
        }
      },
      {
        "_index": "songs",
        "_type": "album",
        "_id": "73SaqWEBv7UBv9hU3TdJ",
        "_score": 1.0,
        "_source": {
          "album": "Every Open Eye",
          "artist": "CHVRCHES",
          "genre": "Indie",
          "year": "2016"
        }
      },
      {
        "_index": "songs",
        "_type": "album",
        "_id": "mXSaqWEBv7UBv9hU3TdJ",
        "_score": 1.0,
        "_source": {
          "album": "Singles",
          "artist": "Future Islands",
          "genre": "Indie",
          "year": "2014"
        }
      },
      {
        "_index": "songs",
        "_type": "album",
        "_id": "m3SaqWEBv7UBv9hU3TdJ",
        "_score": 1.0,
        "_source": {
          "album": "Disappear Here",
          "artist": "Bad Suns",
          "genre": "Rock",
          "year": "2016"
        }
      },
      {
        "_index": "songs",
        "_type": "album",
        "_id": "nHSaqWEBv7UBv9hU3TdJ",
        "_score": 1.0,
        "_source": {
          "album": "ANTI",
          "artist": "Rihanna",
          "genre": "Hip hop",
          "year": "2016"
        }
      },
      {
        "_index": "songs",
        "_type": "album",
        "_id": "p3SaqWEBv7UBv9hU3TdJ",
        "_score": 1.0,
        "_source": {
          "album": "The Life of Pablo",
          "artist": "Kanye West",
          "genre": "Hip hop",
          "year": "2016"
        }
      },
      {
        "_index": "songs",
        "_type": "album",
        "_id": "53SaqWEBv7UBv9hU3TdJ",
        "_score": 1.0,
        "_source": {
          "album": "No No No",
          "artist": "Beirut",
          "genre": "Indie",
          "year": "2015"
        }
      },
      {
        "_index": "songs",
        "_type": "album",
        "_id": "6XSaqWEBv7UBv9hU3TdJ",
        "_score": 1.0,
        "_source": {
          "album": "V",
          "artist": "Maroon 5",
          "genre": "Pop",
          "year": "2015"
        }
      },
      {
        "_index": "songs",
        "_type": "album",
        "_id": "pXSaqWEBv7UBv9hU3TdJ",
        "_score": 1.0,
        "_source": {
          "album": "Blackstar",
          "artist": "David Bowie",
          "genre": "Rock",
          "year": "2016"
        }
      }
    ]
  }
}
q3
{
  "took": 9,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 0,
    "max_score": null,
    "hits": []
  }
}
