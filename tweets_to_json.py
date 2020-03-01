'''
tweets_to_json.py

Downloads 100 tweets containing input text
API keys must be stored in .env file
Some code adapted from Tweepy documentation (http://docs.tweepy.org)
'''

import sys
import datetime
import json
from decouple import config
import tweepy

CONSUMER_KEY = config('APP_KEY')
CONSUMER_SECRET = config('APP_SECRET')
ACCESS_TOKEN = config('OAUTH_TOKEN')
ACCESS_TOKEN_SECRET = config('OAUTH_TOKEN_SECRET')

MAX_TWEETS = 100

def capture_tweets(query: str) -> None:
    auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    date_str = datetime.datetime.now()
    date_str = date_str.strftime("%m_%d_%H_%M_%S") # mm, dd, hh24, mi, ss
    filename = query + date_str + ".json"

    query = query + " -filter:retweets"

    try:
        tweets = [t._json for t in tweepy.Cursor(api.search, q=query,
            lang='en', count=MAX_TWEETS).items(MAX_TWEETS)]
            # optional: result_type='recent'
            # entities attribute includes hashtag list (keep True)

        with open(filename, 'w') as output:
            output.write('[')
            for i in range(len(tweets)):
                json.dump(tweets[i], output)
                if i != len(tweets)-1:
                    output.write(',\n')
                else:
                    output.write('\n')
            output.write(']')

        print("%s created" % filename)
    except tweepy.RateLimitError:
        print("Rate limit exceeded")
    except tweepy.TweepError as err:
        print("Error: %s" % err.reason)
    except:
        print("An error occurred")


if __name__ == "__main__":
    try:
        query = sys.argv[1]
    except:
        print("Usage: %s '<query>'" % sys.argv[0])
        quit()

    if not CONSUMER_KEY or not CONSUMER_SECRET or not ACCESS_TOKEN or not ACCESS_TOKEN_SECRET:
        print("API authorization missing from .env")
        quit()

    capture_tweets(query)
