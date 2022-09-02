import datetime
import pymongo
from pymongo import MongoClient

cluster=MongoClient("mongodb+srv://ayanark:Ruk5231@mongocluster.cjpjq1y.mongodb.net/?retryWrites=true&w=majority")

db=cluster['Student_Management_System']

students=db['students']

def add_student(_id,name,rollno,address,marks):
    document={
        '_id':_id,
        'Name':name,
        'Roll No.':rollno,
        'Address':address,
        'Marks':marks,
        'Date Added':datetime.datetime.now()
    }

    return students.insert_one(document)

#Insertion
# car=add_student(101,'Ayana',1,'aakashwadi',80)
# car=add_student(102,'Aamir',2,'rawatpur',90)
# car=add_student(103,'Aqib',3,'atiya colony',72)
# car=add_student(104,'Sanobar',4,'hinjewadi',92)
# car=add_student(106,'Aadil',5,'epip',78)

# #Searching
findd=students.find_one() #fetch random data
findd=students.find_one({'name':'Aamir'})
print(findd)

# #update 
# prev={"name":"Kaju"}
# nextt={"$set":{"location":"Kheri"}}
# students.update_one(prev,nextt)

# # #Delete one
# rec={"name":"Aqib"}
# students.delete_one(rec)

