import string

def findInAlphabet(ssstring):
    positions = []
    for i in ssstring:
        if i in string.ascii_letters:
            positions.append(string.ascii_letters.index(i))
    return [i + 1 for i in positions]
            
print(findInAlphabet('Soooooooooooooooooo'))
print(findInAlphabet('I\' not funny'))
print(findInAlphabet(string.ascii_letters))