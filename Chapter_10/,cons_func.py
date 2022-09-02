#Creating a class
class Car():
    def __init__(self,modelname,yearofmanufacturing,price): #self reference of an obj which is called in this func
        self.modelname = modelname
        self.yearofmanufacturing = yearofmanufacturing
        self.price = price
    def price_inc(self):
        self.price=int(self.price*1.15)

#Create an object
#Creating two objects that belongs to particular class Car()

BMW=Car('BMW',2017,7000000)
Audi=Car('Audi',2019,6000000)

print("Price before increment")
print(BMW.price)
BMW.price_inc()
print("Price after increment")
print(BMW.price)
print(BMW.__dict__)
