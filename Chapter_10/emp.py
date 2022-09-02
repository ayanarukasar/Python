#class att
class Employee:
    company="Capgemini"

ayana=Employee()
aamir=Employee()

print(ayana.company)
print(aamir.company)

Employee.company="Infosys"
print(ayana.company)
print(aamir.company)