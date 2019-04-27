import json
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener



credentials = {}



class listener(StreamListener):


    def on_connect(self):
        print("SUCCESS, A NEW RECORD")

    def on_data(self,data):
            #jsond = json.loads(data)
            #print(jsond)
            print(data)
            return(True)

    def on_status(self,status):
        print("HI") 
        print(status.text)

    def on_error(self,status_code):
        if status_code == 420:
            print("BIG BOI")
            return False



print("Hello World")
auth = OAuthHandler(credentials['CONSUMER_KEY'], credentials['CONSUMER_SECRET'])
auth.set_access_token(credentials['ACCESS_TOKEN'],credentials['ACCESS_SECRET'])
api = tweepy.API(auth)
a = listener()
twitterStream = Stream(auth, a)
TP = twitterStream.sample()
#print(TP)
#print("HIIIII")


#auth = OAuthHandler(credentials['CONSUMER_KEY'], credentials['CONSUMER_SECRET'])
#auth.set_access_token(credentials['ACCESS_TOKEN'],credentials['ACCESS_SECRET'])

#twitterStream = Stream(auth, listener())


'''

def main():
    print("Hello World")
    auth = OAuthHandler(credentials['CONSUMER_KEY'], credentials['CONSUMER_SECRET'])
    auth.set_access_token(credentials['ACCESS_TOKEN'],credentials['ACCESS_SECRET'])
    a = listener()
    twitterStream = Stream(auth, a)
    TP = twitterStream.userstream()
    #twitterStream.filter(track=["car"]) 
'''

#if __name__ == "__main__":
#	main()
