#Exercise 14: Remove empty strings from a list of strings
#Given:
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
#Expected Output:
#Original list of sting
#['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']

#After removing empty strings
#['Emma', 'Jon', 'Kelly', 'Eric']
#Note. Use comprehensive list expression!

new_list = [str_list[s] for s in range(len(str_list)) if bool(str_list[s])]
print(new_list)
