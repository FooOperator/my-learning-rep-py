def century(year):
    century = 1
    ndred = 0
    for i in range(year):
        if ndred + 100 == i:
            century += 1
            ndred = i
    print(century)
    return century