a=[10,23,2,1,4,80]
a.sort() #sort the list
print(a)

a.reverse() #reverse the list
print(a)

a.append(19) #adds element at the end of the list
print(a)
 

print("Update the indexing values")
a.insert(0,5) #(index_num,updated_value to be inserted)
              #insert 5 at index 0
print(a)

a.pop(2) #delete the index 2 value from the list
print(a)

a.remove(2) #remove element
print(a)

#https://docs.python.org/3/tutorial/datastructures.html 