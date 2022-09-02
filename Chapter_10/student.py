#10 students info roll no. name add marks
#if i enter roll no. which is valid it should fetch the data based on roll no
#Creating a class

class Student():
    def __init__(self,rollno,name,address,marks): #self reference of an obj which is called in this func
        self.rollno = rollno
        self.name = name
        self.address = address
        self.marks=marks
    
    def Display(self):
        print('Roll No.:',self.rollno)
        print('Name:',self.name)
        print('Address:',self.address)
        print('Marks:',self.marks)
 

    
#Create an object
#Creating two objects that belongs to particular class Student()

Student1=Student(101,'Ayana','ABC',70)
Student2=Student(102,'Aamir','xyz',80)
Student3=Student(103,'Ruby','ABC',70)
Student4=Student(104,'Vivek','ABC',70)
Student5=Student(105,'Anju','ABC',70)
Student6=Student(106,'John','ABC',70)
Student7=Student(107,'Bobby','ABC',70)
Student8=Student(108,'Kaju','ABC',70)
Student9=Student(109,'Simran','ABC',70)
Student10=Student(110,'Juhi','ABC',70)

# print(Student1)
print(Student1.__dict__)
Student2.Display()


# n = int(input("Enter rollno_number to search: "))
# if n is Student:
#     print(n,"found at index",Student.index(n))
# else:
#     print(n,"not found")



# name=["Ayana","Aamir","Amaya","Tuba","Juhi","Karan","Ajeet","Surbhi","Priyanka","Kajal"]
# rollno=[1,2,3,4,5,6,7,8,9,10]
# address=['abc','xyz','tyt','opk','htth','sdsa','ds','sfdsa','Scx','fdsf']
# marks=[70,80,80,40,50,70,40,50,60,20]
# obj=[]

# for i in range(0,10):
#     obj.append(Student(rollno[i],name[i],address[i],marks[i]))
    

# obj[3].Display()




 