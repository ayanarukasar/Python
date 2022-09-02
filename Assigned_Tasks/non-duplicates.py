n=int(input("Enter the total number of element you want to insert: "))
list=[]
for i in range(n):
    element=input("Enter element")
    list.append(element)
print("My List :",list)

non_duplicate_value=set(list)
print("NonDuplicatesElement",non_duplicate_value)