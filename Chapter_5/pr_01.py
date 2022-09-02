myDict={
    "Pankha":"Fan",
    "Dabba":"Box",
    "Vastu":"item"
}

print("Options are :",myDict.keys())
a=input("Enter the Hindi Word\n")
# print("The meaning of you word is: ",myDict[a])

#Below line will not throw an err if the key is not present in the dict
print("The meaning of you word is: ",myDict.get(a))