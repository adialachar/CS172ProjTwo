#json object to dictionary
import json
json_file = open('file.json', 'r')
json_str = '5'
json_data = json.loads(json_str)
#FILE = open('file.json','r')
'''
#data = json.load(FILE)

#list = data['tweet']
#i = {}
for var in list:
	j = {var['tweet']}
	i = dict(list(j.items()))
print (i)

'''
#replace string with _
import re

def urlify(s):

	s = re.sub(r"[^\w\s]", '', s)
	s = re.sub(r"\s+", '_', s)
	return s
print(urlify("testing f o r "))

#dictionary into json
i = json.dumps(json_data)
load = json.loads(i)


#file.write(str(json_data['tweet']))


