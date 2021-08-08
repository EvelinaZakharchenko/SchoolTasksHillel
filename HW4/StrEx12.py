#Exercise 12: Find the last position of a substring “Emma” in a given string
#Given:
str1 = "Emma is a data scientist who knows Python. Emma works at google."
#Expected Output:
#Last occurrence of Emma starts at index 43


for s in range(len(str1)-1, -1, -1):
    if str1[(s-4):s] == "Emma":
        index = s-4
        break

print(f"Last occurrence of Emma starts at index {index}")
