#test to make sure Elastic search is up and running
import requests
res = requests.get('http://localhost:9200')
print(res.content)

#connect to cluster
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

#index test data

es.index(index = 'test-index', doc_type = 'test', id = 1, body = {'test' : 'test'})

#delete test data 
es.delete(index = 'test-index', doc_type = 'test', id = 1)

#itereate over json file and index them
import json
r = requests.get('http://localhost:9200')

file = open("file.json", 'r').read()

newData = file.splitlines(True)

i = 0

json_string = ""

docs = {}

for line in newData:
	line = ''.join(line.split())
	for word in line:
		if word != "}":
			json_string += word
		else:
			docs[i] = json_string + "}"
			json_string = ""
			es.index(index = 'twp', doc_type = 'tweet', id = i, body = docs[i])
			i+=1
			res = es.get(index='tweets', doc_type='tweet', id=0)
			print (res['_source'])
