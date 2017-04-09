import tweepy
consumer_key="kedTDGuu20EEGg20ieL6pOKcJ"
consumer_secret="NQsAo4ZRna9N3Ay4sXZBwCWklUUbchePnH47TDOuHRHRkJuobO"
access_token="270168256-Mt3nATmgodszjP3nUq7eDLFhVUpiJOgWtWdXy2sb"
access_token_secret="1g78Gflo1c6E2oQTvG6zYrqVzvAE7y9q0YTuXf3AsNWRe"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet, sep='|')
user = 's_hossain18'    
print(user.screen_name)
