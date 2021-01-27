def extract(target):
    nums = []
    for word in target:
        try: 
            nums.append(int(word))
        except:
            continue
    if len(nums) == 0:
        return print('No numbers on that string')
    return print(nums)

extract('The boring brown monka jumped over his financial responsabilities')
extract('12345')
extract('monka2')