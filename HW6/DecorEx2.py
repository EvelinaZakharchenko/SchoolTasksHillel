# Task #2
# Consider you have a list [2, 4, 5, 6, 7].
# Return a new set where all numbers became a strings (can be perform by str(34)).
# No for loop nor comprehensive lists should be used

list1 = [2, 4, 5, 6, 7]
set1 = set(map(lambda s: str(s), list1))
print(set1)
