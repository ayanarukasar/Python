# This is simplest Student data management program in python
# Create class "Student"
class Student:
    # Constructor
    def __init__(self, rollno,name, marks,address):
        self.rollno = rollno
        self.name = name
        
        self.marks = marks
        self.address= address

    def accept(self, name, rollno,marks,address):
        ob = Student(name, rollno,marks,address)
        ls.append(ob)
        

# Function to display student details     
    def display(self,ob):
            print('Roll No.:',ob.rollno)
            print('Name:',ob.name)
            print('Address:',ob.address)
            print('Marks:',ob.marks)
            print("\n") 

   

# Search Function    
    def search(self, rn):
        for i in range(ls.__len__()):
            if(ls[i].rollno == rn):
                return i 
                
ls=[]
obj = Student(0, '', '', 0)

obj.accept(101,'Ayana','ABC',70)
obj.accept(102,'Aamir','xyz',80)
obj.accept(103,'Ruby','ABC',70)
obj.accept(104,'Vivek','ABC',70)
obj.accept(105,'Anju','ABC',70)
obj.accept(106,'John','ABC',70)
obj.accept(107,'Bobby','ABC',70)
obj.accept(108,'Kaju','ABC',70)
obj.accept(109,'Simran','ABC',70)
obj.accept(110,'Juhi','ABC',70)

print("\nStudent Data, ")
s = obj.search(102)
obj.display(ls[s])
