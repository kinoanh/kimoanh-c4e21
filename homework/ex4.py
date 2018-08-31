from pymongo import MongoClient
from matplotlib import pyplot
uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e' 
client = MongoClient(uri)
db = client.get_default_database()

customers = db["customers"]

cond1 = {"ref": 'events'}
customers_list1 = customers.find(cond1)
count1 = 0
for items in customers_list1:
    count1 += 1
print('events',count1)

cond2 = {"ref":"ads"}
customers_list2 = customers.find(cond2)
count2 = 0
for item in customers_list2:
    count2 += 1
print(' ads',count2)


cond3 = {"ref":'wom'}
customers_list3 = customers.find(cond3)
count3 = 0
for item in customers_list3:
    count3 += 1
print(' wom',count3)

per=[count1 , count2 , count3 ]
name=["ads","wom","events"]
pyplot.pie(per , labels=name, autopct='%.1f%%', shadow=True)
pyplot.axis('equal')

pyplot.show()