#Exercise 8: Find all occurrences of “USA” in a given string ignoring the case
#Given:
str1 = "Welcome to USA. usa awesome, isn't it?"
#Expected Outcome:
#The USA count is: 2

str2 = "usa"
low_str1 = str1.lower()
count = low_str1.count(str2)
print(f"The USA count is: {count}")
