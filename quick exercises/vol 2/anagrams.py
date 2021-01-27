from collections import Counter
def anagrams(word, words):
    return [words[x] for x in range(len(words)) if Counter(words[x]) == Counter(word)]