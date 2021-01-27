def fill(original):
    m1 = [x[:] for x in original]
    m2 = [x[:] for x in original]
    for i in range(len(m1)):
        for j in range(len(m1)):
            if j == i:
                m1[i][j] = 1
    for i in range(len(m2)):
        for j in range(len(m2)):
            if j != i:
                m2[i][j] = 0
            
    print('Original:\n{}\nMatrix 1:\n{}\nMatrix 2:\n{}'.format(original, m1, m2))
   
   
fill([[300, 300, 300, 3000, 12313], ['picles', 'picles', 'picles', 'piclinho', 'p'], [True, False, True, True, False], [None, None, None, None, None], ['', '', '', '', '']])