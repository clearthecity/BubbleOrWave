'''
automate_mongo_insert.py

Runs tweet extraction/upload program once an hour with pre-defined queries
'''

import time
import tweets_to_mongo

ONE_HOUR = 60*60

# API limit with app authentication: 450 every 15 minutes
queries = ['#WetsuwetenStrong', '#Wetsuweten', '#ShutDownCanada']

if __name__ == "__main__":
    try:
        while True:
            for q in queries:
                tweets_to_mongo.insert_into_mongo(q)
            print("Ctrl-C to stop")
            time.sleep(ONE_HOUR)
    except KeyboardInterrupt:
        print("Tweet insertion stopped")
