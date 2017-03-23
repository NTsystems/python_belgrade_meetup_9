# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import requests
import json
from weioLib.weio import *

def setup():
    # attach twitter function to main process
    attach.process(twitter)
    


# Variables that contains the user credentials to access Twitter API
consumer_key = 'djtfZtQfZXb2m8GwGn2NxO8vV'
consumer_secret = 'TsWO7KLdmWesem31NQaE6716mqlUH82BVHtG7Gr6uYBqMRcf6h'
access_token = '842027467024027650-uX3H2D1N4RFJ6NkDMeG9gyQH017w2yn'
access_token_secret = 'IZAxzBMJZr35AQld3htm4sYMFytC2zE11pcXx4euqv4Vt'
hashtags = ['#python', '#iot', '#bigdata']

# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        data = json.loads(data)
        tweet_hashtags = ["#"+x['text'].lower() for x in data.get('entities', {}).get('hashtags', [])]
        if tweet_hashtags:
            print tweet_hashtags
            if "#python" in tweet_hashtags:
                digitalWrite(18, LOW)
                digitalWrite(19, HIGH)
                digitalWrite(20, HIGH)
            elif "#iot" in tweet_hashtags:
                digitalWrite(18, HIGH)
                digitalWrite(19, LOW)
                digitalWrite(20, HIGH)
            elif "#bigdata" in tweet_hashtags:
                digitalWrite(18, HIGH)
                digitalWrite(19, HIGH)
                digitalWrite(20, LOW)
            received_hashtags = set(tweet_hashtags).intersection(set(hashtags))
            if received_hashtags:
                data['hashtags'] = list(received_hashtags)
                serverPush('tweet_arrived', json.dumps(data))
                try:
                    requests.post("http://192.168.1.160:8880/tweets/", json.dumps(data))
                except:
                    pass
        return True

    def on_error(self, status):
        print(status)


def twitter():

    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=hashtags)

