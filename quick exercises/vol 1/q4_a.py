# Q4a) Write a function that returns product of all numbers of a list

def product(*args):
    prod = 1
    for i in args[0]:
        prod *= i
    print(prod) 
        

product([1, 4, 21])
product(range(2, 6))

# DONE!