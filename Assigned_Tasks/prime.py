#A prime number is a number which is divisible by 1 or itself

#How to check a given number is prime number or not

num=7

for i in range(2,num):
    if num % i == 0:
        print("Not prime")
        break
else:
    print("Prime")