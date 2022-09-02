import pymongo
from pymongo import MongoClient
print("Welcome to MongoDB")
cluster=MongoClient("mongodb+srv://ayanark:Ruk5231@mongocluster.cjpjq1y.mongodb.net/?retryWrites=true&w=majority")
print(cluster)
