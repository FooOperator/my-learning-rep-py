# time must be equal to 10, pos x and pos y should be equal to 0
# each step is a minute, so, each direction on the array walk is a minute

def is_valid_walk(walk):
    posy = walk.count('n') - walk.count('s')
    posx = walk.count('w') - walk.count('e')
    if len(walk) == 10 and posx == 0 and posy == 0:
        return True
    else:
        return False
    
print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])) # True
print(is_valid_walk(['n'])) # False
print(is_valid_walk(['n', 's'])) # False
print(is_valid_walk(['n','s','n','s','n','s','n','s','n','w'])) # False
