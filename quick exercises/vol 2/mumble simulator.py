def accum(s):
    return '-'.join([s[x] * (x + 1) for x in range(len(s))]).title()