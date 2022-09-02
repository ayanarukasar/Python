# import csv
# from pymongo import MongoClient

# cluster = MongoClient("mongodb+srv://ayanark:Ruk5231@mongocluster.cjpjq1y.mongodb.net/?retryWrites=true&w=majority") 

# header = [ "rollno","name","address","marks"]
# csvfile = open("mongodb/student.csv")
# reader = csv.DictReader( csvfile )

# for each in reader:
#     row={}
#     for field in header:
#         row[field]=each[field]
        
#     print (row)

from http import client
import pandas as pd
import csv
from pymongo import MongoClient
import json

cluster = MongoClient("mongodb+srv://ayanark:Ruk5231@mongocluster.cjpjq1y.mongodb.net/?retryWrites=true&w=majority") 

df=pd.read_csv("mongodb/student.csv")
df.head()

data=df.to_dict(orient="records")
data

db=cluster["New"]
stud=db['sample']
db.Iris.insert_many(data)

