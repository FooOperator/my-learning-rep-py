def zerospush(target):
    for i in target:
        if i == 0:
            target.pop(target.index(i))
            target.insert(len(target), i)
    return target

print(zerospush([1,2,0,1,0,1,0,3,0,1]))