from elasticsearch import Elasticsearch, helpers

import requests, sys, json, os

from pprint import pprint

from elasticsearch import Elasticsearch

import ast



es = Elasticsearch(
  ['localhost'],
  port=9200 
)

#default elastic #search PORT is #9200
res = requests.get('https://localhost:9200')

FILE = open("file.json",'r').read()
'''
ClearData = FILE.splitlines(True)

i = 0

json_str = ""

docs = {}

for line in ClearData:
    line = ' '.join(line.split())
    for word in line:
      if word != "}":
        json_str += word
      else:
        docs[i] = json_str + "}"
        json_str = ""
        es.index('tweets', doc_type='tweet', id = i, body = docs[i])
        i+=1

res = es.get(index='tweets', doc_type='tweet', id=0)

print (res['_source'])
''' 
def jsonToDicts(STR):
        
    STRI = list(STR)
    for i in range(0,len(STRI)):
        if STRI[i] == "\"":
            STRI[i] = "\'"

    STRIN = ''.join(STRI)
    STRING = ast.literal_eval(STRIN)

    return STRING











