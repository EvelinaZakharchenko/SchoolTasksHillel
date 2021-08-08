#Exercise 6: Delete set of keys from a dictionary
# Given:
sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}
keysToRemove = ["name", "salary"]
# Expected output:
# {'city': 'New york', 'age': 25}

del sampleDict[keysToRemove[0]]
del sampleDict[keysToRemove[1]]
print(sampleDict)
