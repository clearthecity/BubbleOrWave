import pymongo
from decouple import config

connection_string = config('MONGO_CONNECTION_STRING')
client = pymongo.MongoClient(connection_string)
db = client.db
coll = db["twitter"]

coll.insert_many()
