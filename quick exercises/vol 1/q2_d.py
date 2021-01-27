# Q2d) Returns corresponding integer or floating-point number


def num(numba):
    try:
        if type(numba) is str:
            numba + '0'
            for i in numba:
                if i == '.':
                    return float(numba)
            return int(numba)
        numba + 0
        return numba
    except ValueError:
        return 'Couldn\'t convert "{}" into a number'.format(numba)
    except TypeError:
        return '"{}" is an invalid input'.format(numba)


print(num(3))
# 3
print(num(0x1f))
# 31
print(num(3.32))
# 3.32
# ----------------------------------------------- #
# string input
print(num('123'))
# 123
print(num('-78'))
# -78
print(num(" 42  \n "))
# 42
print(num('3.14'))
# 3.14
print(num('3.982e5'))
# 398200.0

s = '56'
print(num(s) + 44)
# 100
print(num('foo'))
print(num('bababooey 2'))
print(num(['skododsk', 2, 34]))
# DONE!