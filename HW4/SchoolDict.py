#School Task
#Create dictionary which represents the school. School consists of:
#1.	Director
#2.	Wise-Director
#3.	Classes
#Class is also consisting of:
#1.	Teacher
#2.	List of students (list because we can exclude the student and add new)
#Student has:
#1.	First Name
#2.	Second Name
#3.	Average score of studying
#Task to do
#Calculate average score of all students in all classes in the school 

import names
from pprint import pprint
dictSchool = {
    "Director": "Mr. John Smith",
    "Wise-Director": "Mrs. Jane Air",
    "Classes": {
        1: {
            "Teacher": "Mrs. Liz Faxon",
            "Students": [
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 10
                },
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 11
                },
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 5
                },
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 10
                },
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 9
                },
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 12
                },
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 2
                }
            ]
        },
        2: {
            "Teacher": "Mr. John Snow",
            "Students": [
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 4
                },
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 5
                },
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 6
                },
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 7
                },
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 8
                },
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 9
                },
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 10
                }
            ],

        },
        3: {
            "Teacher": "Mrs. Jenny Pow",
            "Students": [
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 11
                },
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 2
                },
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 5
                },
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 8
                },
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 9
                },
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 12
                },
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 5
                }
            ],

        },
        4: {
            "Teacher": "Mr. Tom Watson",
            "Students": [
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 6
                },
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 11
                },
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 10
                },
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 11
                },
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 9
                },
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 8
                },
                {
                    "First name": names.get_first_name(),
                    "Second name": names.get_last_name(),
                    "Average": 7
                }
            ]
        }
    }
}
#pprint(dictSchool)
students_count = 0
sum_marks = 0
for i in range(1, len(dictSchool["Classes"])+1):
    students_count += len(dictSchool["Classes"][i]["Students"])
    students = dictSchool["Classes"][i]["Students"]
    for j in range(len(students)):
        sum_marks += students[j]["Average"]

average = sum_marks / students_count

print(f"Average score of all students in all classes in the school is {average}")
