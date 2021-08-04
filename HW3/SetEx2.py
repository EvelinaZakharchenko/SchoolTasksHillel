#Exercise 2: Return a new set of identical items from a given two set
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
#Expected output:
#{40, 50, 30}
#Note. Try “intersection” method of “set” object

new = set2.intersection(set1)
print(new)
