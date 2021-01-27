
def changepos(arr, pos1, pos2):
    temp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = temp
    return arr

print(changepos([1, 2, 3, 4], 0, 1))
print(changepos([9, 9, 9, 1, 9], 3, 0))