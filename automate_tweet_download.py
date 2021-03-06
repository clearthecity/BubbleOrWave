'''
automate_tweet_download.py

Runs tweet extraction program once an hour with pre-defined queries
'''

import time
import tweets_to_json

ONE_HOUR = 60*60

# API limit with app authentication: 450 every 15 minutes
queries = ['#WetsuwetenStrong', '#WetsuwetenSolidarity', '#ShutDownCanada', '#AllEyesOnTyendinaga']

if __name__ == "__main__":
    try:
        while True:
            for q in queries:
                tweets_to_json.capture_tweets(q)
            print("Ctrl-C to stop")
            time.sleep(ONE_HOUR)
    except KeyboardInterrupt:
        print("Automated tweet extraction stopped")
