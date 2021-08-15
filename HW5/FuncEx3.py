#Exercise 3: Write a function calculation() such that it can accept two variables
# and calculate the addition and subtraction of them. And also it must return both
# addition and subtraction in a single return call
#Given:
def calculation(a, b):
# Your Code
    return (a+b), (a-b)


res = calculation(40, 10)
print(res)
#Expected Output
#50, 30
