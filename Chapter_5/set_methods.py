#Creating an empty set using below syntax
b=set()
print(type(b))

#Adding values to an empty set
b.add(4)#adding a value repeatedly does not change a set
b.add(4)

#you cannot add dict or list because its not hashable
b.add((1,2,3))
b.add(6)
print(b)

b.remove(6)

print(b)
print(len(b))

print(b.clear()) #empty the set