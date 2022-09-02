import pymongo
from pymongo import MongoClient

cluster=MongoClient("mongodb+srv://ayanark:Ruk5231@mongocluster.cjpjq1y.mongodb.net/?retryWrites=true&w=majority")
db=cluster["ayana2"]
collection=db["sample"]

#Insert
# insertThese=[
#     {"_id":1,"name":"Ayana","location":"Bangalore"},
#     {"_id":2,"name":"Aamir","location":"Mysore"},
#     {"_id":3,"name":"Sanobar","location":"Delhi"},
#     {"_id":4,"name":"Aqib","location":"Gurgaon"},
#     {"_id":5,"name":"Kaju","location":"Lucknow"}    
# ]
# collection.insert_many(insertThese)


#update one
# prev={"name":"Kaju"}
# nextt={"$set":{"location":"Kheri"}}
# collection.update_one(prev,nextt)

#update many
prev={"name":"Kaju"}
nextt={"$set":{"location":"Lmp-Kheri"}}
collection.update_many(prev,nextt)

#Update count- How many records is updated
# prev={"name":"Kaju"}
# nextt={"$set":{"location":"Lmp-Kheri"}}
# up=collection.update_many(prev,nextt)
# print(up.modified_count)

