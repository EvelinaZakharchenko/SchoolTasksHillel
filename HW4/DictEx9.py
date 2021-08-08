#Exercise 9: Get the key of a minimum value from the following dictionary
sampleDict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
#Expected output:
#Math
#Note. You can easily count the minimum number in collection using min function. I.e.
#t = [1, 2, 3]
#print(min(t))
#1
print(min(sampleDict.values()))
