#Exercise 1: Given a string of odd length greater than 7, return a new string made of the middle three characters of a given String
#Given:
#Case 1
str1 = "JhonDipPeta"
#Output
#Dip
#Case 2
str2 = "JaSonAy"
#Output
#Son


def get3chars(str):
    middle = len(str) // 2
    middle3chars = str[middle - 1:middle + 2]
    return middle3chars


print(get3chars(str1))
print(get3chars(str2))
