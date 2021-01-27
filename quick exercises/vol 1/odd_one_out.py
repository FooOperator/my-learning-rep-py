def odd_one_out(param):
    popped = []
    for i in param:
        if i % 2 == 1:
            popped.append(i)
    print(popped)
    
odd_one_out([1, 2, 3, 4, 5])