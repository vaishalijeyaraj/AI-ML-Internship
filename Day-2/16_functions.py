
def greet(name):
    print(f"Hello, {name}!")

def add(a, b):
    return a + b

def area_rectangle(length, width=1):  
    return length * width

greet("Anu")
result = add(4, 6)
print("Sum:", result)
print("Area:", area_rectangle(5, 3))
print("Area with default width:", area_rectangle(5))

