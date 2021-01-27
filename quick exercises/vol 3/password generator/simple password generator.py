import random

chars = {
    'upper': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'lower': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower(),
    'digits': '1234567890',
    'symbols': '{}[](),;:.-_/\\?+*#'
}

upper, lower, nums, syms = True, True, True, True

all = ''

length = 20
amount = 10

if upper:
    all += chars['upper']
if lower:
    all += chars['lower']
if nums:
    all += chars['digits']
if syms:
    all += chars['symbols']

for x in range(amount):
    password = ''.join(random.sample(all, length))
    print(password)