# Q2a) Returns length of integer numbers

def len_int(thisint):
    thisstr = str(thisint)
    if type(thisint) is str:
        return ('This should be an int')
    elif thisstr[0] == '-' or thisstr[0] == '+': 
        return len(thisstr) - 1
    return len(thisstr)

print(len_int(962306349871524124750813401378124))
print(len_int(+42))
print(len_int(-42))
print(len_int('a'))

# Done!