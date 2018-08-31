from pymongo import MongoClient
from bson.objectid import ObjectId
uri ="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
Client=MongoClient(uri)
db=Client.get_default_database()
posts= db["posts"]
customers = db["customers"]
post={
    "title": "chưa bao giờ",
    "author": "việt anh",
    "content": " trong cơn mưa đêm nhẹ như gió , trôi qua không gian vào nguôi lãng dần , những điều anh chưa nói với em , hôm chia tay cây vừa trút lá, hôm chia tay ô cửa vẫn  sáng đèn , hát gì lên đi đêm quá yên ..." ,}
posts.insert_one(post)
print("done")