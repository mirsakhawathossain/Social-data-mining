import json
import pandas as pd
import matplotlib.pyplot as plt

tweets_data_path="d:\\twitter.txt"
tweets_data=[]

tweets_file=open(tweets_data_path,"r")

for line in tweets_file:
    try:
        tweet=json.loads(line)
        tweets_data.append(tweet)
        return true
    except BaseException as e:
            print("Failed on Data"),str(e)
            time.sleep(5)
tweets=pd.DataFrame()
tweets["text"]=map(lambda tweet:tweet["text"],tweets_data
tweets["lang"]=map(lambda tweet:tweet["lang"],tweets_data
tweets["country"]=map(lambda tweet:tweet["place"]["country"] if[place['place']!=None else None,tweets_data                   

tweets_by_lang=tweets['lang'].value_counts()

fig.ax=plt.subplots()
ax tick_params(axis='x',labelsize=15)
ax tick_params(axis='y',labelsize=10)                                                               
ax.set_xlabel('Language',fontsize=15)
ax.set_ylabel('Number Of Tweets',fontsize=15)
ax.set_title('Top 5 Languages',fontsize=15,fontweight='bold')
tweets_by_lang[:5].plot(ax=ax,kind='bar',color='red')
plt.show()                                                                
