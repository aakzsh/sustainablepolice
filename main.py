from datetime import datetime
import time
import tweepy as twitter
import keys
from profane import is_abusive
from language import checklang
from dotenv import load_dotenv
import os #provides ways to access the Operating System and allows us to read the environment variables

load_dotenv()

# fetch api keys
API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
SECRET_ACCESS_TOKEN = os.getenv("SECRET_ACCESS_TOKEN")

auth = twitter.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, SECRET_ACCESS_TOKEN)

api = twitter.API(auth)

def twitter_bot(tags, delay):
    
    while True:
        print("time is"+str(datetime.now))
        # str()
        for tag in tags:
            for tweet in twitter.Cursor(api.search_tweets, q=tag).items(2):
                try:
                    tweet_id = dict(tweet._json)['id']
                    tweet_text = dict(tweet._json)["text"]

                    print(tweet_id, tweet_text)
                    if not is_abusive(tweet_text) and checklang(tweet_text):
                        api.retweet(tweet_id)
                    else:
                        print("contains abusive words")

                except twitter.TwitterServerError as error:
                    print("some error occured", error)

            time.sleep(delay)


twitter_bot(["sustainablepolice", "deforestation", "sustainability", "climatechange", "sustainable"], 10)