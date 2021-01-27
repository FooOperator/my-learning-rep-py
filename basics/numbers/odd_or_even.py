arr = [0, 1, 2, 3, 4, 5]

odd = []
even = []

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        even.append(arr[i])
    else:
        odd.append(arr[i])

print(even)
print(odd)