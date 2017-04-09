import json
tweets = []

for lines in open('d:\\tester.txt'):
  try: 
    tweets.append(json.loads(lines))
  except:
    pass
print(len(tweets))
tweet = tweets[0]
print(tweet['user'].keys())
print('========================')
tweet = tweets[3]
print(tweet['user'].values())
print("=========================")
screen_names = [tweet['user']['screen_name'] for tweet in tweets]
names = [tweet['user']['name'] for tweet in tweets]
print(screen_names)
print(names)
print(tweet['created_at'])
print('========================================')
d = dict(tweet)
i = iter(d)
for x in iter(d.items()):
  print("==========================================")
  print(x)
print(json.dumps(tweet,indent=4,sort_keys=True,ensure_ascii=False,skipkeys=True))
print("===============================================")
piko = json.dumps(tweet,indent=4,sort_keys=True,ensure_ascii=False,skipkeys=True)
print(piko)
print("===============================================")
