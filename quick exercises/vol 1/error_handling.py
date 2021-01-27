a = 1

try: #catches AttributeError
    a.reverse()
except:
    print('can\'t reverse a {}'.format(type(a)))

try: #catches NameError
    print(b)
except:
    print('undeclared variable')

try: #catches TypeError
    a += '1'
except:
    print('can\'t add a string to an int')
    
try: 
    print('' + a)
    a+= '1'
except TypeError:
    print('nah')