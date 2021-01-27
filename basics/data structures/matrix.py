<<<<<<< HEAD
def triangular_machine(matrix):
    lower_triangular = [x[:] for x in matrix]
    upper_triangular = [x[:] for x in matrix]
    for i in range(len(upper_triangular)):
        for j in range(len(upper_triangular)):
            if j < i:   
                upper_triangular[i][j] = 0
    for i in range(len(lower_triangular)):
        for j in range(len(lower_triangular)):
            if j > i:
                lower_triangular[i][j] = 0
    print('Old Matrix: {}\nUpper Triangular: {}\nLower Triangular: {}'.format(matrix, upper_triangular, lower_triangular))
            
triangular_machine([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
triangular_machine([[1, 2, 3], [20, 30, 50], [1, 1, 1]])
=======
def triangular_machine(matrix):
    lower_triangular = [x[:] for x in matrix]
    upper_triangular = [x[:] for x in matrix]
    for i in range(len(upper_triangular)):
        for j in range(len(upper_triangular)):
            if j < i:   
                upper_triangular[i][j] = 0
    for i in range(len(lower_triangular)):
        for j in range(len(lower_triangular)):
            if j > i:
                lower_triangular[i][j] = 0
    print('Old Matrix: {}\nUpper Triangular: {}\nLower Triangular: {}'.format(matrix, upper_triangular, lower_triangular))
            
triangular_machine([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
triangular_machine([[1, 2, 3], [20, 30, 50], [1, 1, 1]])
>>>>>>> 372027d6fc62809d6ade8a6398ab114116837e65
triangular_machine([[1, 1], [2, 2]])