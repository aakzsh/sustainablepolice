from datetime import datetime
from time import time
import tweepy as twitter
import keys
from profane import is_abusive


auth = twitter.OAuthHandler(keys.API_KEY, keys.API_SECRET_KEY)
auth.set_access_token(keys.ACCESS_TOKEN, keys.SECRET_ACCESS_TOKEN)

api = twitter.API(auth)

def twitter_bot(tag, delay):
    while True:
        print("time is"+str(datetime.now))
        # str()
        for tweet in twitter.Cursor(api.search_tweets, q=tag, rpp=10).items(5):
            try:
                tweet_id = dict(tweet._json)['id']
                tweet_text = dict(tweet._json)["text"]

                print(tweet_id, tweet_text)
                if not is_abusive(tweet_text):
                    api.retweet(tweet_id)
                else:
                    print("contains abusive words")

            except twitter.TwitterServerError as error:
                print("some error occured", error)

        time.sleep(delay)


twitter_bot("hehe", 10)