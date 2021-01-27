def wow(start, end):
    for i in range(start, end):
        binary = bin(i)
        binary = binary.removeprefix('0b')
        if binary[::-1] == binary:
            print('Number is {} and its binary is {} and backwards is {}'.format(i, binary, binary[::-1]))

wow(1, 1000)
wow(2, 5)

# DONE!