# Exercise regarding while loop and generator expression
# Create chronometry function which counts time back from
# given amount of the seconds to 0 and shows the seconds on
# the console. Use while loop rather than for. Also use generator
# object to calculate next second value rather than usual counter variable.
import time

total = int(input("Enter total amount of seconds: "))
generator_counter = (s for s in range(total, -1, -1))
while True:
    second = next(generator_counter)
    print(f"{second}")
    time.sleep(1)
    if second == 0:
        break
print("Finish!")
