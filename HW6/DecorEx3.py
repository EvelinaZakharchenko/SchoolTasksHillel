# Task #3
# Generate 30 dates using time_machine function from previous home task
# and generate 30 date for the exact date 2001-02-12. Create list which contains dates
# between 2001 and 2010. Do not use for loops nor comprehensive lists.

from datetime import date
import random

inputted_date = "2001-02-01"


def time_machine(full_date):
    full_date = date.fromisoformat(full_date)
    year = full_date.year
    month = full_date.month
    day = full_date.day
    first_year = year // 100 * 100
    last_year = first_year + 100
    year_given_by_time_machine = random.randint(first_year, last_year)
    return date(year_given_by_time_machine, month, day)


counter = 0
list1 = []
while counter <= 30:
    current_date = time_machine(inputted_date)
    counter += 1
    if 2001 <= current_date.year <= 2010:
        list1.append(current_date.isoformat())
    counter += 1
print(list1)

