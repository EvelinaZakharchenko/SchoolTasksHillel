#Exercise 4: Arrange string characters such that lowercase letters should come first
#Given an input string with the combination of the lower and upper case
# arrange characters in such a way that all lowercase letters should come first.
#Given:
str1 = "PyNaTive"
#Expected Output:
#yaivePNT

low = []
up = []
for char in str1:
    if char.islower():
        low.append(char)
    else:
        up.append(char)
str2 = ''.join(low + up)
print(str2)
