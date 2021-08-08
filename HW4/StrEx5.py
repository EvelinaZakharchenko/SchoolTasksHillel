#Exercise 5: Count all lower case, upper case, digits, and special symbols from a given string
#Given:
str1 = "P@#yn26at^&i5ve"
#Expected Outcome:
#Total counts of chars, digits,and symbols
#Chars = 8
#Digits = 3
#Symbol = 4

Chars = 0
Digits = 0
Symbol = 0
for s in range(len(str1)):
    if str1[s].isdigit():
        Digits += 1
    elif str1[s].isalpha():
        Chars += 1
    else:
        Symbol +=1

print(f"Chars = {Chars}\nDegits = {Digits}\nSymbol = {Symbol}")

