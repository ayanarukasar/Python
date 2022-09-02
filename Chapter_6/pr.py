num1=int(input("Enter num1\n"))
num2=int(input("Enter num2\n"))
num3=int(input("Enter num3\n"))
num4=int(input("Enter num4\n"))

if num1>num4:
    f1=num1
else:
    f1=num4
if(num2>num3):
    f2=num2
else:
    f2=num3

if(f1>f2):
    print(str(f1),"is greatest")
else:
    print(str(f2),"is greatest")