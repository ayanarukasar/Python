def log_computation(func):
    def wrapper(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return wrapper

@log_computation
def div_up(a, b):
    return a / b

a,b=2,4
print("Division = ",div_up(a,b))

