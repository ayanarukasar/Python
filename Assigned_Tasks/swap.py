#1st method

list=[12, 35, 9, 56, 24,40] 
print(list)
list[0],list[-1]=list[-1],list[0]
print("after interchange",list)

#2nd method

list1=[12, 35, 9, 56, 24,40] 

temp=list1[-1]
list1[-1]=list1[0]
list1[0]=temp

print("after interchange",list1)


#python supports negative indexing