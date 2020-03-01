'''
tweets_to_mongo.py

API keys and MongoDB (Atlas) connection string must be stored in .env file
'''

import sys
from decouple import config
import tweepy
import pymongo

CONSUMER_KEY = config('APP_KEY')
CONSUMER_SECRET = config('APP_SECRET')
ACCESS_TOKEN = config('OAUTH_TOKEN')
ACCESS_TOKEN_SECRET = config('OAUTH_TOKEN_SECRET')
CONNECTION_STRING = config('MONGO_CONNECTION_STRING')

MAX_TWEETS = 100


def insert_into_mongo(query: str):
    tweets = capture_tweets(query)
    if tweets:
        try:
            client = pymongo.MongoClient(CONNECTION_STRING)
            db = client.db
            coll = db["twitter"]
            coll.insert_many(tweets)
            print("%d tweets inserted matching query %s" % (len(tweets), query))
        # TODO more precise error checking
        except:
            print("Database error occurred")


def capture_tweets(query: str) -> list:
    auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    query = query + " -filter:retweets"
    tweets = []
    try:
        tweets = [t._json for t in tweepy.Cursor(api.search, q=query,
            lang='en', count=MAX_TWEETS).items(MAX_TWEETS)]
            # optional: result_type='recent'
            # entities attribute includes hashtag list (keep True)
    except tweepy.RateLimitError:
        print("Rate limit exceeded")
    except tweepy.TweepError as err:
        print("Error: %s" % err.reason)
    except:
        print("An error occurred")
    finally:
        return tweets


if __name__ == "__main__":
    try:
        query = sys.argv[1]
    except:
        print("Usage: %s '<query>'" % sys.argv[0])
        quit()

    if not CONSUMER_KEY or not CONSUMER_SECRET or not ACCESS_TOKEN or not ACCESS_TOKEN_SECRET:
        print("API authorization missing from .env")
        quit()

    if not MONGO_CONNECTION_STRING:
        print("MongoDB connection string missing from .env")
        quit()

    insert_into_mongo(query)
