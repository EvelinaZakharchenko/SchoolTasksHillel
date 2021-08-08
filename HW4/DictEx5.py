#Exercise 5: Create a new dictionary by extracting the following keys from a below dictionary
# Given dictionary:
sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}
# Keys to extract
keys = ["name", "salary"]
#Expected output:
#{'name': 'Kelly', 'salary': 8000}

dict1 = {
    keys[0]: sampleDict[keys[0]],
    keys[1]: sampleDict[keys[1]]
}
print(dict1)