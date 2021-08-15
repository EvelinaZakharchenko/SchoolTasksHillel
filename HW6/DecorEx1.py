# We have 3 vacation requests types:
# 1. Vacation
# 2. Sick leave
# 3. Day off
# Write a program, which will propose you to choose one of the vacation types,
# enter First Name, Surname, from_date and to_date.
# As a result, on the console should be displayed vacation request.
# Each vacation type consists from 2 parts:
# • Title (1 for all types. CEO Red Bull Inc. Mr. John Bigbull)
# Vacation Request pattern (1 for each type. Listed below)
# Request should contain entered First Name and Surname.

request_type = input("Enter type of vacation request, one of Vacation, Sick leave, Day off: ")
first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
from_date = input(f"Enter date from which your {request_type} starts: ")
to_date = input(f"Enter date when your {request_type} ends: ")


def run_logger(func):
    def wrapper(*args, **kwargs):
        print("Title: \nCEO Red Bull Inc. \nMr. John Bigbull")
        print(f"Vacation type: {request_type} Pattern")
        print(f"Hi John,\nI need the paid {request_type} from {from_date} to {to_date}.\n{first_name} {surname}")
        return func(*args, **kwargs)

    return wrapper


@run_logger
def func():
    return None


func()
