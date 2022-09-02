from http import client
import pymongo
from pymongo import MongoClient
import pprint

url="mongodb+srv://ayanark:Ruk5231@mongocluster.cjpjq1y.mongodb.net/?retryWrites=true&w=majority"
client=MongoClient(url)

db=client['emp_details']
collection=db['customer_information']


#<---------------INSERT------------->
# collection.insert_many(
#     [
#         {
#             "_id":101,
#             "name":"Ayana",
#             "designation":"Associate-I Engineer"
#         },
#         {
#             "_id":102,
#             "name":"Aqib",
#             "designation":"Software-Engineer"
#         },
#         {
#             "_id":103,
#             "name":"Aamir",
#             "designation":"Technology Analyst"
#         },
#         {
#             "_id":104,
#             "name":"Sanobar",
#             "designation":"Project Engineer"
#         }

#     ]
# )

#<----SEARCH------->

#SEARCH ONE
# pprint.pprint(collection.find_one())

#FIND ALL
# for i in collection.find({'name':'Aamir'}):
#     pprint.pprint(i)

#<--------UPDATE-------->
#update one
# prev={"name":"Aamir"}
# nextt={"$set":{"designation":"Engineer"}}
# pprint.pprint(collection.update_one(prev,nextt))

# #update many
# prev={"name":"Aamir"}
# nextt={"$set":{"designation":"RPA Technology"}}
#pprint.pprint(collection.update_many(prev,nextt))

#<----------DELETE---------->
# #Delete one
# rec={"name":"Aamir"}
# pprint.pprint(collection.delete_one(rec))

# #Delete many
# rec={"name":"Aqib"}
# pprint.pprint(collection.delete_many(rec))

