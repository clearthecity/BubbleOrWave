Scripts to batch-download tweets (with complete metadata) matching a query, using Tweepy and the standard Search API.

### Setup
You will need API and OAUTH keys from Twitter. Store the keys in a `.env` file.

In `automate_tweet_download.py` and/or `automate_mongo_insert.py`, change the list of `queries` to suit your needs.
Be aware of rate limits: you may want to adjust the time interval or the `MAX_TWEETS` number in `tweets_to_json.py` and/or `tweets_to_mongo.py`.

### Local download (JSON files)
`python tweets_to_json.py '<your_query>'`

To schedule regular downloads of a list of queries:
`python automate_tweet_download.py`

### Insert tweets directly into MongoDB
You will need a Mongo connection string in `.env`. (I've been using Atlas; other servers may work differently.)
`python tweets_to_mongo.py '<your_query>'`

To schedule regular insertion from a list of queries:
`python automate_mongo_insert.py`
