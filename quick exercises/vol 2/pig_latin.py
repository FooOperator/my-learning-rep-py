def pig_it(text):
    pigged = []
    for i in text.split(' '):
        if i not in '?!.':
            pigged.append(i[1::] + i[0] + 'ay')
        else:
            pigged.append(i)
    return ' '.join(pigged)