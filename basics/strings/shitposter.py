import string

def shitpostString(target):
    for digit in target:
        target = target.replace(digit, digit.swapcase())
    print(target)
        
shitpostString('This party is getting crazy! Let\'s Rock!')
shitpostString('Sweet Home, Alabama')
shitpostString('Bro u good?')