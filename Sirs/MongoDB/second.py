from dbbase import DBBase
from my_csv_reader import readCSV
DBNAME = "test2"
MONGOURL = "mongodb+srv://vkpk2219:vivek123@cluster0.xd27wbj.mongodb.net/?retryWrites=true&w=majority"


dbobj = DBBase(MONGOURL)
db = dbobj.getDB(DBNAME)
csvobj = readCSV('student1.csv')

datalist = csvobj.process()
#
collobj = db["firstcoll"]

ot = collobj.find_one({"mobile": "9867895649"})

alldata = collobj.find()
for data in alldata:
    print(data)
print("--------------------")
print(ot)

#dbobj.my_insert_many(collobj, datalist)

#
# step 1 - we have csv file
# step 2 - in python read the csv file - how to
# step 3 - we make one datalist obj from that csv

