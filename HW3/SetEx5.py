#Exercise 5: Remove items 10, 20, 30 from the following set at once
set1 = {10, 20, 30, 40, 50}
#Expected output:
#{40, 50}
#Note. Try to use “difference_update” method of “set” object.

set2 = {10, 20, 30}
set1.difference_update(set2)

print(set1)
