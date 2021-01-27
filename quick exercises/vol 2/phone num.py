test = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3]

def create_phone_number(n):
    phone_string = ['(']
    for i in range(3):
        phone_string.append(str(n[i]))
    phone_string.extend([')', ' '])
    for i in range(3):
        phone_string.append(str(n[3 + i]))
    phone_string.append('-')
    for i in range(4):
        phone_string.append(str(n[6 + i]))
    return ''.join(phone_string)

phone_num = lambda n: '({}{}{}) {}{}{}-{}{}{}{}'.format(*n)

print(create_phone_number(test))
print(phone_num(test))
