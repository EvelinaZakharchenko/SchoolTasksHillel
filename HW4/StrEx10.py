#Exercise 10: Given an input string, count occurrences of all characters within a string
#Given:
str1 = "Apple"
#Expected Outcome:
#{'A': 1, 'p': 2, 'l': 1, 'e': 1}

dict1 = {}
for s in range(len(str1)):
    dict1[str1[s]] = str1.count(str1[s])

print(dict1)
