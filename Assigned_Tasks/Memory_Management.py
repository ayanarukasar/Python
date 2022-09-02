x=10
print(type(x))

y=x
if(id(x)==id(y)):
    print(" x and y refer to the same object")

x=x+1
if(id(x)!=id(y)):
    print("x and y refer to the different object")

z=10
if(id(y)==id(z)):
    print("y and z point to the same memory!!")
else:
    print("y and z point to the different object")



