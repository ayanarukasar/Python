#class att
class Employee:
    company="Capgemini"
    salary="3000000"

ayana=Employee()
aamir=Employee()

#instance att
aamir.salary=10000000
ayana.salary=2000000

print(ayana.company)
print(aamir.company)

Employee.company="Infosys"
print(ayana.company)
print(aamir.company)
print(ayana.salary)
print(aamir.salary)