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
print(json.dumps(es.search(index = "songs", doc_type = "album", body = q3), indent = 2))	#search for albums having artists named  "Rihanna" released in 1975-2001
