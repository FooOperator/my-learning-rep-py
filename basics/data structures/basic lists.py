food = ['Pizza', 'Fish', 'Fish', 'Salad']
numbers = [1, 1, 6, 3, 4]
bools = [True, False, True, True, False]

print(numbers[2:])
print(numbers[0:3])
numbers.remove(1)
print(numbers)

food.insert(1, 'Rice')
print(food)
print(food.pop(0))
print(food.count('Fish'))

bools.append('lmao')
print(bools.index(True))
print(bools)
bools.clear()
print(bools)