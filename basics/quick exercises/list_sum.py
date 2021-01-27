thing = [-4, -5, 9]
# simple way: use sum() method
print('way 1: {}'.format(sum(thing)))

# customizable way: for loop over the list
def list_sum(subject):
    result = 0
    for i in subject:
        result += i
    return result
    
print('way 2: {}'.format(list_sum(thing)))
