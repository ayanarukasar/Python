mylist = ["a", "b", "a", "c", "c","d","d"]  #A List with Duplicates

mylist = list(dict.fromkeys(mylist)) 
#dict.fromkeys(mylist)
#Create a dictionary, using the List items as keys.
# This will automatically remove any duplicates because dictionaries cannot have duplicate keys.

#convert the dictionary back into a list: mylist = list( )
#Now we have a List without any duplicates, and it has the same order as the original List.

print(mylist)