import math
from elasticsearch import Elasticsearch

def BM25(n,K,f):
	
	
	value = 100 - n + 0.5
	value = value/n
	score = math.log(value,10)
	
	score *= ((2.2) * f)/(K + f))
	
	score *= (float(101)/100)
	
	return score
	


def find_average_tweet_length():

	avg_length = 0
	for i in range (0,100):
		
		es.get(....,id = i)
		
		bag = remove_u(res['_source']['tweet'])
		avg_length += len(bag)
		
		return ((float(avg_length)/100)
		
		
def remove_u(s):

	char_list = list(s)
	
	word_list = []
	temp = ""
	
	for i in range(0, len(char_list)):
		
		if (char_list[i] is not '_'):
			temp += str(char_list[i])
		else:
			word_list.append(temp)
			temp = ""
	
	
	
	
	
	
