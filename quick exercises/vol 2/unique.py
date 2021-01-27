def unique_in_order(arr):
    prev = None # compares with current, if equal, i does not append to new_arr
    new_arr = [] # only accepts subsequent, unique entries
    for i in arr:
        if prev != i:
            new_arr.append(i)
            prev = i
    return new_arr
    

print(unique_in_order(['a', '1', '1', 'b']))
print(unique_in_order(['y', 'Y', 'y', 'Y']))
