strings = ['1', '2', '\n 44', 'bear', 'monka2']

for i in strings:
    try:
        print('{} is a number'.format(int(i)))
    except:
        print('{} is a string'.format(i))