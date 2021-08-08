#Exercise 15: Remove special symbols/Punctuation from a given string
#Given:
str1 = "/*Jon is @developer & musician"
#Expected Output:
#"Jon is developer musician"

str2 = []
for s in range(len(str1)):
    if str1[s].isalpha():
        str2.append(str1[s])
    elif str1[s] == " ":
        str2.append(str1[s])

print(''.join(str2))
