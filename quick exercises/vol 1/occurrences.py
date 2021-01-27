from collections import Counter
#print most common list occurrences
#counts ALL values without need of a loop
a = Counter([1, 2, 3, 4, 5, 6, 6, 6, 6, 6])
#top 3 most common occurrences
print(a.most_common(3))