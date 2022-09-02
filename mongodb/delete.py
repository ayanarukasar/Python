import pymongo
from pymongo import MongoClient

cluster=MongoClient("mongodb+srv://ayanark:Ruk5231@mongocluster.cjpjq1y.mongodb.net/?retryWrites=true&w=majority")
db=cluster["ayana2"]
collection=db["sample"]


# #Delete one
# rec={"name":"Aqib"}
# collection.delete_one(rec)

# #Delete many
# rec={"name":"Kaju"}
# collection.delete_many(rec)

#Delete count- How many records is delete
# rec={"name":"Kaju"}
# dt=collection.delete_many(rec)
# print(dt.deleted_count)

