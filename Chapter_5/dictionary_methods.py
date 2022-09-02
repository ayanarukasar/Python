mydict={
    "fast":"In a quick manner", #make key lower case always
    "ayana":"A Coder",
    "marks":[80,90,70], #List
    "anotherdict":{"Aamir":"Waris","Ayana":"Rukasar"},
    15:19
}

print(mydict.keys()) #dict_keys(['fast', 'ayana', 'marks', 'anotherdict',15])

print(type(mydict)) #<class 'dict'>

#convert it into a list
print(list(mydict.keys()))

print(mydict.values()) #dict_values(['In a quick manner', 'A Coder', [80, 90, 70], {'Aamir': 'Waris', 'Ayana': 'Rukasar'}, 19])

print(mydict.items()) #returns tuple

#Updating
print(mydict)
updateDict={
    "Lovish":"Family",
    "MA":"Love",
    "ayana":"An Engineer" #if the value is already present in previos dict then it will auto update the key value pair
}
mydict.update(updateDict)
print(mydict)

#the df bw get and [] syntax
print(mydict.get["fast"]) #if the value is not present it throws "none"
print(mydict["fast"]) #if the value is not present it throws "err"

#3,40
