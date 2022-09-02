greetings="Good Morning, "
name="Aamir"

print(type(name))
print(greetings+name) #Concatenation can be done in the strings using + operator

#Concatenating two strings
c=greetings+name
print(c)

#Str indexing
print(name[0])

# name[3]="d" #does not work you cannot change

#Slicing
print(name[0:3]) # [index_start:index_end]
print(name[0:])
print(name[:3])

#Slicing with negative indexing
NewName =name[-4:-1]
print(NewName)


name="ayanacapgemini" #Overriding
print(name[0::2])  # [index_start:index_end:skipvalue]


