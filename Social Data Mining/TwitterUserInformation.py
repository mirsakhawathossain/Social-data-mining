import tweepy

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'kedTDGuu20EEGg20ieL6pOKcJ'
consumer_secret = 'NQsAo4ZRna9N3Ay4sXZBwCWklUUbchePnH47TDOuHRHRkJuobO'
access_token = '270168256-Mt3nATmgodszjP3nUq7eDLFhVUpiJOgWtWdXy2sb'
access_token_secret = '1g78Gflo1c6E2oQTvG6zYrqVzvAE7y9q0YTuXf3AsNWRe'

if __name__ == '__main__':
    # Create authentication token
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    print('Getting statistics for @BarackObama:')

    # Get information about the user
    data = api.get_user('BarackObama')

    print('Followers: ' + str(data.followers_count))
    print('Tweets: ' + str(data.statuses_count))
    print('Favouries: ' + str(data.favourites_count))
    print('Friends: ' + str(data.friends_count))
    print('Appears on ' + str(data.listed_count) + ' lists')
    stuff = api.user_timeline(screen_name = 'danieltosh', count = 1, include_rts = True)

    print(stuff)
