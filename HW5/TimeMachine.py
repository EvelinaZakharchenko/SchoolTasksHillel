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


while True:
    date_from_time_machine = time_machine(inputted_date)
    print(date_from_time_machine)
    if date_from_time_machine.year == date.fromisoformat(inputted_date).year:
        print(f"You win")
        break


# Year in the proper decade printing task
# Using the time_machine function try to generate 30 date variants but print only those
# dates which pass to the desired year decade. I.e. for 1979 the decade will be between 1970 and 1980.

# Important note
# If you have the date object you can easily access each part of the date from it.
# Year – date_obj.year
# Month – date_obj.month
# Day – date_obj.day
