#Exercise 2: Print multiplication table of a given number
#For example, num = 2 so the output should be
#2
#4
#6
#8
#10
#12
#14
#16
#18

num = int(input("Input num:"))

for i in range(1, 11):
    print(num * i)

