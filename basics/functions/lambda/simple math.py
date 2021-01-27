add = (lambda x, y: x + y)
sub = (lambda x, y: x - y)
times = (lambda x, y: x * y)
div = (lambda x, y: x / y)

num1 = 2
num2 = 4

print(add(num1, num2), add(num1, num1), add(num2, num1))
print(sub(num1, num1), sub(num2, num1), sub(num1, num2))
print(times(num1, num2))
print(div(num1, num2), div(num2, num1))
