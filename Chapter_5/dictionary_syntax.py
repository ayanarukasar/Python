mydict={
    "Fast":"In a quick manner",
    "Ayana":"A Coder",
    "Marks":[80,90,70], #List
    "anotherdict":{"Aamir":"Waris","Ayana":"Rukasar"}
}
print(mydict)
print(mydict["Ayana"])

mydict["Marks"]=[100,60,50] #updating (mutable)

print(mydict["Marks"])
print(mydict["anotherdict"])
print(mydict['anotherdict']['Aamir']) #fetch the key value