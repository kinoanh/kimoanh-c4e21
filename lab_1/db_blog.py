#1.connect to database
from pymongo import MongoClient
from bson.objectid import ObjectId
uri="mongodb://vukimoanh:oanh1234@dbh62.mlab.com:27627/c4e21"
client=MongoClient(uri)
db=client.get_default_database()

#2. select collection
posts= db["posts"]
#3.creat document
post = {
    "title":"hôm nay trời nắng ",
    "content":"tôi vẫn đi học code ",
}
#4.insert document
posts.insert_one(post)
#print("done")
post_list=posts.find() # post_list dùng như list
#print(post_list[2])  
#for post in post_list:
#    print(post) #post ~ document~dictionary
cond={
    "title" :{
        '$regex':'Nắng',
        '$options': 'i', #cách search gần đúng 
    }    
}
post=posts.find_one(cond)
print(post)