# Завдання №2
# Створіть текстовий файл зі списком учнів, де кожна лінійка є у форматі: П.І.Б учня, середня оцінка
# Створіть прогаму, що на основі даних з файлу, обрахує середню оцінку по класу
import os
import names
import random

count_of_students = 30
with open(os.path.join(os.path.curdir, "students_list.txt"), "w") as students_list:
    for _ in range(count_of_students):
        students_list.write(f"{names.get_first_name()} {names.get_last_name()} {random.randint(1, 12)}\n")


def find_average():
    with open(os.path.join(os.path.curdir, "students_list.txt"), "r") as students_list:
        list1 = []
        lines = students_list.read()
        for s in range(len(lines)):
            if lines[s].isdigit() and lines[s - 1].isdigit():
                list1.append(int(lines[s - 1] + lines[s]))
    sum1 = sum(list1)
    average = sum1 / count_of_students
    return average


print(find_average())
