# Q2c) Returns True/False - two strings are anagrams


def str_anagram(str1, str2):
    new_list = ''.join([str1, str2].copy())
    for i in new_list.lower():
        if i not in str1.lower() or i not in str2.lower():
            return False
    return True

print(str_anagram('god', 'Dog'))
print(str_anagram('beat', 'table'))
print(str_anagram('Tap', 'paT'))
print(str_anagram('beat', 'abet'))

# DONE!