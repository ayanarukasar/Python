#Creating a class
class Car():
    def __init__(self,modelname,yearofmanufacturing,price): #self reference of an obj which is called in this func
        self.modelname = modelname
        self.yearofmanufacturing = yearofmanufacturing
        self.price = price

#Create an object
#Creating two objects that belongs to particular class Car()

BMW=Car('BMW',2017,'70 lakh')
Audi=Car('Audi',2019,'60 lakh')


print(BMW.price)
print(BMW.__dict__)
