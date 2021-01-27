import re

def to_camel_case(text):
    if text == '':
        return text
    else:
        camelo = []
        for i in re.split('-|_', text):
            if text.index(i) > 0:
                camelo.append(i.capitalize())
            else:
                camelo.append(i)
        print(camelo)
        return ''.join(camelo)