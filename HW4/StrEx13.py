#Exercise 13: Split a given string on hyphens into several substrings and display each substring
#Given:
str1 = "Emma-is-a-data-scientist"
#Expected Output:
#Displaying each substring
#Emma
#is
#a
#data
#scientist

index = []
for s in range(len(str1)):
    if str1[s] == "-":
        index.append(s)
for i in range(len(index)):
    if i == 0:
        print(str1[:(index[i])])
        print(str1[(index[i]+1):index[i+1]])
    elif i == (len(index)-1):
        print(str1[(index[i]+1):])
    else:
        print(str1[(index[i]+1):index[i+1]])
