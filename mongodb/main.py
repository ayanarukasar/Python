
# import pymongo

# if __name__=='__main__':
#     print("welcome to pymongo")
#     client=pymongo.MongoClient("mongodb+srv://ayanark:Ruk5231@mongocluster.cjpjq1y.mongodb.net/?retryWrites=true&w=majority")
#     print(client)
#     db=client['ayana']
#     collection=db['mySampleCollectionForayana']
#     dictionary={'name':'Ayana','marks':80}
#     collection.insert_one(dictionary)

# from pymongo import MongoClient
# client=MongoClient("mongodb+srv://ayanark:Ruk5231@mongocluster.cjpjq1y.mongodb.net/?retryWrites=true&w=majority")
# db=client.get_database('MongoPy')
# records=db.users

import pymongo
from pymongo import MongoClient

cluster=MongoClient("mongodb+srv://ayanark:Ruk5231@mongocluster.cjpjq1y.mongodb.net/?retryWrites=true&w=majority")
db=cluster["test"]
collection=db["test"]

# post={"_id":101,"name":"ayana","marks":80}
# collection.insert_one(post)

insertThese=[
    {"_id":101,"name":"ayana","marks":80},
    {"_id":102,"name":"aamir","marks":90},
    {"_id":103,"name":"sanobar","marks":70},
    {"_id":104,"name":"aqib","marks":90},
    {"_id":105,"name":"kaju","marks":80}
    
]

collection.insert_many(insertThese)