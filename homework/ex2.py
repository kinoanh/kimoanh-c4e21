from pymongo import MongoClient
from bson.objectid import ObjectId
uri ="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
Client=MongoClient(uri)
db=Client.get_default_database()
post_1 = db["posts"]
post_2 = db["customer"]
