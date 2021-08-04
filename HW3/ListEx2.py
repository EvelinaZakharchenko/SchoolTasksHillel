#Exercise 2: Concatenate two lists index-wise
#Given:
#list1 = ["M", "na", "i", "Ke"]
#list2 = ["y", "me", "s", "lly"]
#Expected output:
#['My', 'name', 'is', 'Kelly']

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
new_list = []
for i in range(len(list1)):
    new_list.append(list1[i] + list2[i])
print(new_list)
