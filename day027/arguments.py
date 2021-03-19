
# unlimited positional arguments
def add(*args):
    return sum([arg for arg in args])

print(add(1, 2))
print(add(1, 2, 3))
print(add())

# unlimited keyword arguments
def calculate(n, **kwargs):
    print(type(kwargs)) #it's a dict
    print(kwargs)

    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    print(kwargs.keys())

calculate(2, add=3, multiply=5)