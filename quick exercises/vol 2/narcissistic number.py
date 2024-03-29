'''
A Narcissistic Number is a positive number which is the sum 
of its own digits, each raised to the power of the number of digits in a given base. 
In this Kata, we will restrict ourselves to decimal (base 10).
For example, take 153 (3 digits), which is narcisstic:
1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
'''
def narcissistic(num):
    res = 0
    for i in num:
        res += pow(int(i), len(num))
    return res == int(num)

print(narcissistic('153'))
print(narcissistic('1938'))
print(narcissistic('2'))
print(narcissistic('152'))
