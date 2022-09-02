import pymongo
from pymongo import MongoClient

cluster=MongoClient("mongodb+srv://ayanark:Ruk5231@mongocluster.cjpjq1y.mongodb.net/?retryWrites=true&w=majority")
db=cluster["test"]
collection=db["test"]

#Insert One
# post={"_id":101,"name":"ayana","marks":80}
# collection.insert_one(post)

#Insert many
insertThese=[
    {"_id":101,"name":"ayana","marks":80},
    {"_id":102,"name":"aamir","marks":90},
    {"_id":103,"name":"sanobar","marks":70},
    {"_id":104,"name":"aqib","marks":90},
    {"_id":105,"name":"kaju","marks":80}
]

collection.insert_many(insertThese)