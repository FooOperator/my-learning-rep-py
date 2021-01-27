target = 4

def equalTo():
    entry = 0
    while entry != target:
        try:
            entry = int(input('Type 4, please: '))
        except:
            print('A number, please')
    return 'equal'

print(equalTo())