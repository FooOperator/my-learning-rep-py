def abbrev_name(name):
    abb = []
    for i in name.split(' '):
        abb.append(i[0])
    return '.'.join(abb).upper()

print(abbrev_name('Phillip Jennings'))
print(abbrev_name('Oleg Igorevich Burov'))

twonames = lambda name: '{}.{}'.format(name.split(' ')[0][0], name.split(' ')[1][0]).upper()

print(twonames('Stan Beeman'))
print(twonames('Elizabeth Jennings'))
print(twonames('Nina Sergeevna Krilova')) # returns N.S instead of N.S.K



