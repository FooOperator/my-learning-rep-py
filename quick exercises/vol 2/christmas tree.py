def xmas_tree(height):
    tree = ''
    width, gap = 0, 0
    for i in range(height):
        if i == 0:
            width = 1
        else:    
            width += 2
        gap = height - (i + 1)
        tree += ' ' * gap + '*' * width + ' ' * gap + '\n'
    return tree.rstrip()

print(xmas_tree(5))
