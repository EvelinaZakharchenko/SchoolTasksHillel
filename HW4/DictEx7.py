#Exercise 7: Check if a value 200 exists in a dictionary
sampleDict = {'a': 100, 'b': 200, 'c': 300}
#Expected output:
#True
#Note: You can check if something is in collection using in statement. I.e.
#r = [1, 2, 3]
#print(1 in r)
#will print True

print(200 in sampleDict.values())
