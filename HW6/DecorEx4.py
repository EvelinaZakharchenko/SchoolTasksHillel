# Task #4
# Consider we have list of numbers from 1 to 100.
# Sum all items which can be devided by 3, which is devided by 3
# (if a can be devided by 3, + a/3). Use functools.reduce for that.
from functools import reduce

list1 = [s for s in range(1, 101)]
list2 = []
for i in range(len(list1)):
    if i % 3 == 0:
        list2.append(i)
result = reduce(lambda a, b: a + b, list2)
print(result)
