names = ['Rey', 'Jordan', 
         'Phillip', 'Garcia', 'Stewie', 
         'Darius', 'Alex', 'Cheyenne', 
         'Billie', 'Claudia', 'Connor',
         'Davis', 'Bertha', 'Roberta',
         'Chloe', 'Maynard', 'Stu', 'Jo',
         'Dee', 'Hammond', 'Talion', 'K\'',
         'Donald', 'Ceasar', 'Vernon',
         'Gunther', 'Saoirse', 'Vincent'
         ]

print(list(filter(lambda x: x.startswith('C'), names)))
print(list(filter(lambda x: len(x) > 7, names)))
print(list(filter(lambda x: x.endswith('r'), names)))