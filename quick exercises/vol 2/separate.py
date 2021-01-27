posFromNeg = lambda x: [[i for i in x if i >= 0], [i for i in x if i < 0]]

print(posFromNeg([1, 2, 3 , 4 , -1, -5, 9, 0]))

strFromNum = lambda x: [[i for i in x if type(i) == str], [i for i in x if type(i) == int or type(i) == float]]

print(strFromNum([1, 2.4, '3', 'string']))
print(strFromNum(['fu', 4, (1, 2, 3)]))

