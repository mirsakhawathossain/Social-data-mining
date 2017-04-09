try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API


CONSUMER_KEY = '7pWHWtYlXM9ayJfUKv2F8v84B'
CONSUMER_SECRET = 'Dfcx10Px77Ggn0qGbCHc4TZC7M2IHsXpqk9CaGiCLzcr9VMX5n'
ACCESS_TOKEN = '245080367-zuLrIbxblOnocashgku9dsmDKgy3R7uU0VCTIRDx'
ACCESS_SECRET = 'wCx5ufD9Zft46hVjieLdv0af7p9DxUTsPgge9Zm2qelR9'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
#iterator = twitter_stream.statuses.sample()

iterator = twitter_stream.statuses.filter(track="India", language="en") 

tweet_count = 10000 
for tweet in iterator:
    tweet_count -= 1


    print(tweet['created_at'],"\t",tweet['user']['screen_name'],"\t",tweet['geo'], "\t",tweet['text'])


    if tweet_count <= 0:
        break
