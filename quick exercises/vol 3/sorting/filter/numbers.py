import random as r

numbers = [r.randint(-100, 100) for i in range(0, 10)]

print(numbers)
print(list(filter(lambda y: y > 0, numbers)))
print(list(filter(lambda x: x < 0, numbers)))