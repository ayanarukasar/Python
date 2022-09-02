def div(a,b):
    # if a<b:
    #     a,b=b,a
    # imagine this whole file is not with you and you are trying to import it, but you didnt have any access or may be you dont want to change the existing code so i wanted to swap those two value without touching the existing code.
    # thats where deco comes into picture
    # using deco you can add extra features to the existing func
    print(a/b)

def smartdiv(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

# div=smartdiv(div) types of calling dec 

div(2,4)

# you can change the behavior of the existing func at  the compile time itself.
