#Exercise 2: Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1
#Given:
s1 = "Ault"
s2 = "Kelly"
#Expected Output:
#AuKellylt
middle = len(s1)//2
s3 = s1[:middle] + s2 + s1[middle+1:]
print(s3)
