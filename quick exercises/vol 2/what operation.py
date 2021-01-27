def what_operation(a, b, res):
    if a + b == res:
        return 'addition'
    elif a - b == res:
        return 'subtraction'
    elif a * b == res:
        return 'multiplication'
    else:
        return 'division'

print(what_operation(2, 1, 3))
print(what_operation(5, 25, 5))
print(what_operation(4, 2, 8))
print(what_operation(4, 2, 2))