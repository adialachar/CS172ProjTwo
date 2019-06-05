import json
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os
import re
from lxml.html import parse
from http.client import BadStatusLine
import urllib
from urllib.request import urlopen
import requests
import sys
import datetime
credentials = {}
credentials['CONSUMER_KEY'] = 'vJsGsCMmiZapsIoEpYVahW76L'
credentials['CONSUMER_SECRET'] = 'SVHB6pHLVZPOoppBYywcsXlRkxDGBzdLufDwoingipDoEH66lX'
credentials['ACCESS_TOKEN'] = '3051117252-VLcksCEUJgk6kSRPjvkPqbZbT1jQC62cJHowgKq'
credentials['ACCESS_SECRET'] = '48VbkQrhuieXAVwQObdvVuIBGDT5rCYCKjuh7FhCdVbqC'
#Content-Type: text/html; charset=utf-8


FILE = open('file.json','a')


class listener(StreamListener):


    def __init__(self, api=None):
        super(listener, self).__init__()
        self.num_tweets = 0


    def on_connect(self):
        print("Connection Established")    

    
    def on_status(self,status):

        try:
            link = re.search("(?P<url>https?://[^\s]+)", status.text)
            if link is not None:
                link = link.group("url")
                str(link)


       
            if (len(status.entities['urls']) > 0):
                
                #print(status.entities['urls'][0]['expanded_url'])
                link = status.entities['urls'][0]['expanded_url']
         
            dict = {'screen_name': status.user.screen_name, 'tweet': status.text, 'Location': status.user.location, 'Link': link, 'Date': (status.created_at).strftime('%m/%d/%Y'),'Time': (status.created_at).strftime('%H:%M:%S')}
        

        


            if self.num_tweets < 100:

                FILE.write(json.dumps(dict))
                FILE.write("\n")


            
                self.num_tweets += 1
                return True
            else:
                return False




        except urllib.error.HTTPError:
            print("There has been an error")
            return True

    def on_error(self,status_code):
        if status_code == 420:
            print("BIG BOI")
            return False



auth = OAuthHandler(credentials['CONSUMER_KEY'], credentials['CONSUMER_SECRET'])
auth.set_access_token(credentials['ACCESS_TOKEN'],credentials['ACCESS_SECRET'])
api = tweepy.API(auth)
a = listener()
twitterStream = Stream(auth, a)
TP = twitterStream.filter(languages = ["en"], track = ["the","a"])


emptyTitle = False
data = []
with open('file.json', 'r+') as f:

    for line in f:
        
        #print(json.loads(line))
        
        data.append(json.loads(line))
        

    



open('file.json', 'w').close()

for line in data:

    link = line['Link']
    #print(link)
    if (link is not None):
        if (len(link) > 23):
            text = parse(urllib.request.urlopen(str(link)))
            title = text.find(".//title").text
            if title is not None:

                line['title'] = title
                FILE.write(json.dumps(line))
                FILE.write("\n")












#with open('file.json', 'w') as g:





'''
    for line in f:
        data = json.loads(line)
        data['title'] = "goodboy"
        print(data)
        f.seek(0)
        f.write(json.dumps(data))
        f.truncate()
    
        
        print(json.loads(line))
        data = json.loads(line)       
        
        link = data['Link']
        print("HELLOOOOOOOO")
        print(link)
        print("HIIIIIIIIIII")
        if (link is not None):
            print(link)
            if (len(link) < 23):
                emptyTitle = True
            text = parse(urllib.request.urlopen(str(link)))

            title = text.find('.//title').text
            print("JJJJJJJJJJ")
            print(title)
            print("KKKKKKKKKKK")
            if emptyTitle == True:
                title = ""
                emptyTitle = False
                
                
            if title is not None:
                f.seek(0)
                data['title'] = title
                json.dump(data,f,indent = 4)
                f.truncate()
                                                                                                                    
'''





#if __name__ == "__main__":
#	main()
