#Exercise 1: Reverse the following tuple
aTuple = (10, 20, 30, 40, 50)
#Expected output:
#(50, 40, 30, 20, 10)
#Note: You can’t reverse tuple, but list you can.

list1 = list(aTuple)
list1.reverse()
bTuple = tuple(list1)
print(bTuple)
