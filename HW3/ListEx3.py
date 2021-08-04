#Exercise 3: Given a Python list of numbers. Turn every item of a list into its square
#Given:
#aList = [1, 2, 3, 4, 5, 6, 7]
#Expected output:
#[1, 4, 9, 16, 25, 36, 49]

aList = [1, 2, 3, 4, 5, 6, 7]

for i in range(len(aList)):
    aList[i] = aList[i] * aList[i]

print(aList)
