import datetime
from http import client
from xml.dom.minidom import Document
import pymongo
from pymongo import MongoClient

cluster=MongoClient("mongodb+srv://ayanark:Ruk5231@mongocluster.cjpjq1y.mongodb.net/?retryWrites=true&w=majority")



db=cluster['dealership']

cars=db['cars']
customers=db['customers']
purchases=db['purchases']

def add_car(model,year,mrp):
    document={
        'Model':model,
        'Year':year,
        'MSRP':mrp,
        'Date Added':datetime.datetime.now()
    }

    return cars.insert_one(document)

def add_customer(first_name,last_name,dob):
    document={
        'First Name':first_name,
        'Last Name':last_name,
        'DOB':dob,
        'Date Added':datetime.datetime.now()
    }
    return customers.insert_one(document)

def add_purchase(car_id,customer_id,methods):
    document={
        'Car _id':car_id,
        'Customer _id':customer_id,
        'Methods':methods,
        'Date Added':datetime.datetime.now()
    }
    return purchases.insert_one(document)

#Insertion

car=add_car('BMW',2008,700000)
customer=add_customer('Ayana','Rukasar','15-03-2000')
purchase=add_purchase(car.inserted_id,customer.inserted_id,'Cash')
