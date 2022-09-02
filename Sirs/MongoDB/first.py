import pymongo
client = pymongo.MongoClient("mongodb+srv://vkpk2219:vivek123@cluster0.xd27wbj.mongodb.net/?retryWrites=true&w=majority")
DBNAME = "test"
#db = client.DBNAME  #process 1 in this db always DBNAME
db = client[DBNAME] #process 2  in this we can use the variable
data = {"firstname": "Vivek", "lastname": "Tiwari","mobileno":9098978675}
# connect with collection name
#db["firstcoll"].insert_one(data)


datalist = [{"firstname": "Vivek1", "lastname": "Tiwari1"},
            {"firstname": "Vivek2", "lastname": "Tiwari2"},
            ]
#
db["firstcoll"].insert_many(datalist)
#
# db["mycoll"].insert_many(datalist)



