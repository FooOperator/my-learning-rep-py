weapons = ['Deagle', 'Ak-47', 'Mtar 21', 'Colt 1911']
food = ['Lasagna', 'Strogonoff', 'Pasta']

def listStuff(arr):
    print(arr)
    arr.reverse()
    print(arr)
    arr.sort()
    print(arr)
    arr.remove(arr[0])
    print(arr)

print(listStuff(weapons))
print(listStuff(food))
print(listStuff(['Justified', 'The Shield', 'The Americans', 'American Horror Story']))