#Exercise 2: Write a function func1() such that it can accept a variable length of
# argument and print all arguments value
#func1(20, 40, 60)
#func1(80, 100)
#Expected Output:
#func1(20, 40, 60)
#20
#40
#60

#func1(80, 100)
#80
#100

def func1(*args):
    for i in range(len(args)):
        print(args[i])

func1(20, 40, 60)
#func1(80, 100)