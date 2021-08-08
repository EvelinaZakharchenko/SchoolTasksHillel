#Exercise 6: Given two strings, s1 and s2, create a mixed String using the following rules
#Note: create a third-string made of the first char of s1 then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
#Given:
s1 = "Abc"
s2 = "Xyz"
#Expected Output:
#AzbycX


s3 = ""
for i in range(len(s1)):
    if i == 0:
        s3 += (s1[i] + s2[-i-1])
    elif i == (len(s1) - 1):
        s3 += (s1[i] + s2[0])
    else:
        s3 += (s1[i] + s2[-i-1])
print(s3)

