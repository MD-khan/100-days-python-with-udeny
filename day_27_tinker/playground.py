# unlimited positional arguments

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1,3,4,5))

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate(2, add=3, multiply=5)