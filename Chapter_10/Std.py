class Student:
    # marks = []
    def getData(self, rn, name, m):
        Student.rn = rn
        Student.name = name
        Student.marks=m
        
        
    def displayData(self):
        print ("Roll Number is: ", Student.rn)
        print ("Name is: ", Student.name)
        print ("Marks are: ", Student.marks)


    
r = int (input("Enter the roll number: "))
name = input("Enter the name: ")
m = int (input("Enter the marks in subject: "))


s1 = Student()
s1.getData(r, name, m)
s1.displayData()

# n = int(input("Enter number to search: "))
# if n is Student:
#     print(n,"found at index",Student(n))
# else:
#     print(n,"not found")


