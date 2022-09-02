import pymongo
from pymongo import MongoClient

cluster=MongoClient("mongodb+srv://ayanark:Ruk5231@mongocluster.cjpjq1y.mongodb.net/?retryWrites=true&w=majority")
db=cluster["test"]
collection=db["test"]

#SEARCHING - one docs
#Search those in which we have name aamir if yes print name else none

# one=collection.find_one() #fetch random data
# one=collection.find_one({'name':'aamir'})
# print(one)

# #SEARCH many docs
# alldocs=collection.find({'name':'aamir'})
# for items in alldocs:
#     print(items)

# #SEARCH many docs with only names display
# alldocs=collection.find({'name':'aamir'},{'name':1,'_id':0})
# for items in alldocs:
#     print(items)

#SEARCH many docs except names display
alldocs=collection.find({'name':'aamir'},{'name':0,'_id':0})
for items in alldocs:
    print(items)
