def sortby_firstletter(names):
    first_letters = list(set(map(lambda x: names[x][0], range(len(names)))))
    for i in first_letters:
        print('Starts with {}: '.format(i))
        for j in range(len(names)):
            if names[j].startswith(i):
                print(names[j])

def sortby_len(names):
    name_length = list(set(map(lambda x: len(names[x]), range(len(names)))))
    for i in name_length:
        print('Length of {}: '.format(i))
        for j in range(len(names)):
            if len(names[j]) == i:
                print(names[j])

example1 = ['Mason', 'Mustard', 'Maria']
example2 = ['Artamis', 'Seju']

sortby_firstletter(example1)
sortby_len(example1)

sortby_firstletter(example2)
sortby_len(example2)
