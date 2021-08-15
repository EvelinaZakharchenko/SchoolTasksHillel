# Year in the proper decade printing task
# Using the time_machine function try to generate 30 date variants but print only those
# dates which pass to the desired year decade. I.e. for 1979 the decade will be between 1970 and 1980.

from datetime import date
import random

inputted_date = input("Input date in format YYYY-MM-DD: ")


def time_machine(full_date):
    full_date = date.fromisoformat(full_date)
    year = full_date.year
    month = full_date.month
    day = full_date.day
    first_year = year // 100 * 100
    last_year = first_year + 100
    year_given_by_time_machine = random.randint(first_year, last_year)
    return date(year_given_by_time_machine, month, day)


for _ in range(30):
    current_date = time_machine(inputted_date)
    first_decade_year = date.fromisoformat(inputted_date).year // 10 * 10
    last_decade_year = first_decade_year +10
    if first_decade_year <= current_date.year <= last_decade_year:
        print(current_date)
