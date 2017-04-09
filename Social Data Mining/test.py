import json
tweets = []

for line in open('d:\\twitter.txt'):
  try: 
    tweets.append(json.loads(line))
  except:
    continue
print(len(tweets))
tweet = tweets[47]
print(tweet)
print(tweet.keys())
print("===========================================================================")

ids = [60]
for tweet in tweets:
  ids.append(tweet['id_str'])
ids = [tweet['id_str'] for tweet in tweets]
texts = [tweet['text'] for tweet in tweets]
times = [tweet['created_at'] for tweet in tweets]
screen_names = [tweet['user']['screen_name'] for tweet in tweets]
names = [tweet['user']['name'] for tweet in tweets]
print(tweet['entities'])
print("===========================================================================")
for tweet in tweets:
  if tweet['entities']['user_mentions']:
    print(tweet['entities']['user_mentions'])
    break
print("===========================================================================")
print(tweet['geo'])
print("===========================================================================")
place_names = [(T['place']['full_name'] if T['place'] else None) for T in tweets]
place_types = [(T['place']['place_type'] if T['place'] else None) for T in tweets]
print(place_names)
print("===========================================================================")
print(place_types)
