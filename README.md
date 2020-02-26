Scripts to batch-download tweets (with complete metadata) matching a query, using Tweepy and the standard Search API.

### Setup
You will need API and OAUTH keys from Twitter. Store the keys in a `.env` file.

### Usage
`python tweets_to_json '<your_query>'`

To schedule regular downloads of a list of queries:
In `automate_tweets.py`, change the list of `queries` to suit your needs.
Be aware of rate limits: you may want to adjust the time interval or the `MAX_TWEETS` number in `tweets_to_json.py`.
`python automate_tweets.py`
