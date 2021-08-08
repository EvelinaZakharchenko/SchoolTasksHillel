#Exercise 3: Given two strings, s1, and s2 return a new string made of the first,
# middle, and last characters each input string
#Given:
s1 = "America"
s2 = "Japan"
#Expected Output:
#AJrpan
middle1 = len(s1)//2
middle2 = len(s2)//2
print(s1[0] + s2[0] + s1[middle1] + s2[middle2] + s1[-1] + s2[-1])

