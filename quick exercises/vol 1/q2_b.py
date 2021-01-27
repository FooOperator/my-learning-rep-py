'''
Q2b) Returns True/False - two strings are same
irrespective of lowercase/uppercase
'''

str_cmp = lambda str1, str2: str1.lower() == str2.lower()

print(str_cmp('nice', 'nice'))
print(str_cmp('Hi there', 'hi there'))
print(str_cmp('GoOd DaY', 'gOOd dAy'))
print(str_cmp('foo', 'food'))

# DONE!