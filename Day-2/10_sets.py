
numbers = {1, 2, 2, 3, 4}
print(numbers)  # duplicates are removed
numbers.add(5)
numbers.discard(3)
print(numbers)

first = {1, 2, 3, 4}
second = {3, 4, 5, 6}
print("Union:", first | second)
print("Intersection:", first & second)
print("Difference:", first - second)
print("Symmetric difference:", first ^ second)

