from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
consumer_key="kedTDGuu20EEGg20ieL6pOKcJ"
consumer_secret="NQsAo4ZRna9N3Ay4sXZBwCWklUUbchePnH47TDOuHRHRkJuobO"
access_token="270168256-Mt3nATmgodszjP3nUq7eDLFhVUpiJOgWtWdXy2sb"
access_token_secret="1g78Gflo1c6E2oQTvG6zYrqVzvAE7y9q0YTuXf3AsNWRe"
class StdOutListener(StreamListener):    
    def on_data(self, data):
        try:            
            print(data)
            savefile=open("d:\\twitter.txt","a")
            savefile.write(data)
            savefile.write('\n')
            savefile.close()
            return True
        except BaseException as e:
            print("Failed on Data"),str(e)
            time.sleep(5)

    def on_error(self,status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['salesforce', 'javascript', 'python'])
    
        


