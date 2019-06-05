import re
import functions
from flask import Flask, render_template, request
app = Flask(__name__)
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
			#json_string += "_"
			#print(type(json_string))
		else:
			docs[i] = json_string + "}"
			json_string = ""
			es.index(index = 'tweets', doc_type = 'tweet', id = i, body = docs[i])
			i+=1
			#res = es.get(index='tweets', doc_type='tweet', id=0)
			#print (res['_source'])
			#print(type(res['_source']))



def find_average_tweet_length():

	avg_length = 0
	for i in range (0,42):
		
		res = es.get(index='tweets', doc_type = 'tweet',id = i)
		
		bag = res['_source']['tweet']
		avg_length += len(bag)
		
	return ((float(avg_length)/100))
		

				
				
				
def find_number_of_docs(term):


	n = 0			
	for i in range(0,42):
		res = es.get(index = 'tweets', doc_type = 'tweet', id = i)
		if (len(re.findall(term, res['_source']['tweet'])) > 0):
				n += 1
				
	return n
				
	

@app.route("/", methods=['GET', 'POST'])
def main():


	tweets_and_scores = []
	time_sorter = []
	if request.method == 'POST':


		query = request.form.get('query',-1)
		#query = "girlfriend offered"
		terms = query.split()

		AVG = find_average_tweet_length()
		
		n = 0	
		for i in range(0,42):
		
				
			res = es.get(index = 'tweets', doc_type = 'tweet', id = i)
			#print(res['_source'])
			#print(res['_source']['tweet'])	
			K = (1.2 * (0.25))
			K += (0.75) * ((len(res['_source']['tweet']))/AVG)
			 	
				
			#print(K)	
				
						
			score = 0
			for j in range(0, len(terms)):
				
				f = re.findall(terms[j], res['_source']['tweet'])
				n = find_number_of_docs(terms[j])
				score += functions.BM25(n,K,len(f))
			
			t = (res['_source'], score)
			#print(t)
			tweets_and_scores.append(t)


		tweets_and_scores = sorted(tweets_and_scores, key=lambda tweets_and_scores: tweets_and_scores[1])
		tweets_and_scores = tweets_and_scores[-10:]
		#tweets_and_scores = sorted(tweets_and_scores, key=lambda tweets_and_scores: tweets_and_scores[0]['Time'])
		#print(tweets_and_scores[1][0]['Time'])	
		no_time_list = []
		for i in range(0,10):
			#t = (tweets_and_scores[i][0]['Time'],i)
			#print(tweets_and_scores[i][0])
			
			if 'Time' in tweets_and_scores[i][0].keys():

				t = (tweets_and_scores[i][0]['Time'],i)
	


				time_sorter.append(t)

			else:
				no_time_list.append(i)


			



		time_sorter = sorted(time_sorter, key=lambda time_sorter: time_sorter[0])
		#print(time_sorter)
		#time_sorter.reverse()
		#print(time_sorter)	
		sorted_tweets = []
		for i in range(0, len(time_sorter)):

			sorted_tweets.append(tweets_and_scores[i])


		#sorted_tweets.extend(no_time_list)


		for i in range(0, len(no_time_list)):
			sorted_tweets.append(tweets_and_scores[i])


		#print(sorted_tweets)

		just_tweets = []
		for i in range(0,len(sorted_tweets)):
		
			#just_tweets.append(sorted_tweets[i][0]['tweet'])
			#print(sorted_tweets[i])
			#print(type(sorted_tweets[i]))

			if type(sorted_tweets[i] == tuple):
				just_tweets.append(sorted_tweets[i][0]['tweet'])
			#elif type(sorted_tweets[i] == dict):
			#	just_tweets.append(sorted_tweets[i]['tweet'])



			
		return render_template('index.html', just_tweets = just_tweets)		






	return render_template('index.html')













if __name__ == "__main__":
	app.run()



