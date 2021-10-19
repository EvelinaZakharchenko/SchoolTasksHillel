# Завдання №1
# Переробити завдання зі школою зі словника у клас!
# Та мусимо зважити на те, що все дії та обчислення я хочу бачити через виклик методів.
# Жодних вільних функцій.
import names

dictSch = {
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


class DictSchool:
    @classmethod
    def find_sum(cls, dict1, students_count, sum_marks):
        for i in range(1, len(dict1["Classes"]) + 1):
            students_count += len(dict1["Classes"][i]["Students"])
            students = dict1["Classes"][i]["Students"]
            for j in range(len(students)):
                sum_marks += students[j]["Average"]

        average = sum_marks / students_count

        print(f"Average score of all students in all classes in the school is {average}")


if __name__ == "__main__":
    DictSchool.find_sum(dictSch, 0, 0)
