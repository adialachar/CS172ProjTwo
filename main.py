import json
import unicodedata
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import csv
import os
import re
from lxml.html import parse
from http.client import BadStatusLine
import urllib
from urllib.request import urlopen
from lxml import etree
from io import StringIO
from bs4 import BeautifulSoup
import requests
import sys
from django.utils.encoding import smart_str
credentials = {}
credentials['CONSUMER_KEY'] = 'vJsGsCMmiZapsIoEpYVahW76L'
credentials['CONSUMER_SECRET'] = 'SVHB6pHLVZPOoppBYywcsXlRkxDGBzdLufDwoingipDoEH66lX'
credentials['ACCESS_TOKEN'] = '3051117252-VLcksCEUJgk6kSRPjvkPqbZbT1jQC62cJHowgKq'
credentials['ACCESS_SECRET'] = '48VbkQrhuieXAVwQObdvVuIBGDT5rCYCKjuh7FhCdVbqC'



FILE = open('file.json','a')


class listener(StreamListener):


    def __init__(self, api=None):
        super(listener, self).__init__()
        self.num_tweets = 0


    def on_connect(self):
        print("Connection Established")    

    
    def on_status(self,status):
        if status.user.location is not None:
            
            dict = {'screen_name': status.user.screen_name, 'tweet': status.text, 'Location': status.user.location}
            link = re.search("(?P<url>https?://[^\s]+)", status.text)
            if link is not None:
                link = link.group("url")
            if (link is not None):
                    print(link)
                    text = parse(urllib.request.urlopen(smart_str(link)))
                    title = text.find('.//title').text
                    dict['title'] = title


            print(dict)
            if self.num_tweets < 500:

                FILE.write(json.dumps(dict))
                FILE.write("\n")


                self.num_tweets += 1
                print(self.num_tweets)
                return True
            else:
                return False


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








#if __name__ == "__main__":
#	main()
