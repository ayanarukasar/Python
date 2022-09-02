story="once upon a time, there was a Greek King, Midas.He was very rich and had lots of Gold. He had a daughter, who he loved a lot."
print(story[0:8])

#String Func
print(len(story))
print(story.endswith("ayana")) 
print(story.endswith("lot."))

#Count
print(story.count("a"))
print(story.count("King"))

#Capatalized
print(story.capitalize()) #starting will capatalize

#Find
print(story.find("King")) #if the char is present it will print distance from starting 
print(story.find("ayana")) #if the char is not present it will print -1

#Replace
print(story.replace("Midas","Aamir"))


