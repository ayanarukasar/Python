import pymongo
from pymongo import MongoClient
import csv
import pprint
import pandas as pd

student_fields = ['rollno','name','address','marks']
student_database = 'students.csv'

# with open('mongodb/student.csv', 'r') as file:
#     my_reader = csv.reader(file)
#     for row in my_reader:
#         print(row)

# url="mongodb+srv://ayanark:Ruk5231@mongocluster.cjpjq1y.mongodb.net/?retryWrites=true&w=majority"
# client=MongoClient(url)
cluster=MongoClient("mongodb+srv://ayanark:Ruk5231@mongocluster.cjpjq1y.mongodb.net/?retryWrites=true&w=majority")

#Reading csv

df=pd.read_csv("mongodb/student.csv")
# df.head()

# data=df.to_dict(orient="records")
data=df.to_dict()
data

db=cluster['python_test']
collection=db['test_collection']

#<--------------INSERT-------------->
# db.Iris.insert_many(data)

#<-------------SEARCH-------------->
# x=db.Iris.find_one({"name":"'Ayana'"})
# print(x)

#FIND ALL
# for i in db.Iris.find({'name':"'Aamir'"}):
#     pprint.pprint(i)


#<---------------------UPDATE--------------->
#update one
# prev={"name":"'Aqib'"}
# nextt={"$set":{"marks":100}}
# pprint.pprint(db.Iris.update_one(prev,nextt))

# #update many
# prev={"name":"'Aqib'"}
# nextt={"$set":{"marks":90}}
#pprint.pprint(db.Iris.update_many(prev,nextt))


#<----------DELETE---------->
# #Delete one
# rec={"name":"'Aamir'"}
# pprint.pprint(db.Iris.delete_one(rec))

# #Delete many
# rec={"name":"Aqib"}
# pprint.pprint(db.Iris.delete_many(rec))