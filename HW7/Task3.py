# Завдання №3
# Створіть програму гри у кості (у нас 5 костей, кожна має від 1 до 6 точок).
# Щоразу гравець кидає кості та отримує очки. Комбінації наступні:
# 2 кості з однаковими очками - кількість точок * 2
# 3 кості з однаковми очками - кількість очків * 4
# 2 пари костей з однаковими очками - кількість очків * 6
# 4 кості з однаковими очками - кількість очків * 10
# всі кості з однаковими очками - кількість очків * 20
# В інших випадках - сума всіх очків кожної кості
# Очки записуються в текстовий файл. Кості повинні викидатися з об'єкта ґенератора, створеного через функцію.

# IMPLEMENTATION NOTE!
# 1. sum of all points are multiplied on multiplier,
# 2. for case where are 3 equal numbers and 2 another equal numbers sum is multiplied for both 2 and 4 multipliers

import random
import os


def throw_cubes():
    count = 0
    while count <= 5:
        result = random.randint(1, 6)
        count += 1
        yield result


def count_points():
    list_of_results = []
    for i in range(5):
        list_of_results.append(next(throw_cubes()))
    print(list_of_results)
    sum_of_points = sum(list_of_results)
    print(f"Sum of all points is {sum_of_points}")
    for j in range(5):
        if list_of_results.count(list_of_results[j]) == 5:
            print("There are 5 equal numbers")
            return sum_of_points*20
        elif list_of_results.count(list_of_results[j]) == 4:
            print("There are 4 equal numbers")
            return sum_of_points*10
        elif list_of_results.count(list_of_results[j]) == 3:
            list_of_results = [s for s in list_of_results if s != list_of_results[j]]
            print(list_of_results)
            for h in range(2):
                if list_of_results.count(list_of_results[h]) == 2:
                    print("There are 3 equal numbers and 2 another equal numbers")
                    return sum_of_points * 4 * 2
                else:
                    continue
            print("There are 3 equal numbers")
            return sum_of_points*4
        elif list_of_results.count(list_of_results[j]) == 2:
            list_of_results.pop(j)
            for h in range(4):
                if list_of_results.count(list_of_results[h]) == 3:
                    print("There are 2 equal numbers and 3 another equal numbers")
                    return sum_of_points * 4 * 2
                elif list_of_results.count(list_of_results[h]) == 2:
                    print("There are 2 equal numbers and 2 another equal numbers")
                    return sum_of_points * 6
                else:
                    continue
            print("There are 2 equal numbers")
            return sum_of_points * 2
        else:
            continue
    print("No equal numbers")
    return sum_of_points


with open(os.path.join(os.path.curdir, "points.txt"), "w") as points:
    points.write(str(count_points()))
