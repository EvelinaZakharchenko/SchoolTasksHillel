#Exercise 9: Given a string, return the sum and average of the digits that appear in the string, ignoring all other characters
#Given:
str1 = "English = 78 Science = 83 Math = 68 History = 65"
#Expected Outcome:
#sum is 294
#average is 73.5
digits = []


for s in range(len(str1)):
    if str1[s].isdigit() and str1[s-1].isdigit():
        digits.append(int(str1[s-1]+str1[s]))
sum1 = sum(digits)
average = sum1 / len(digits)
print(f"sum is {sum1}\naverage is {average}")

