# Завдання №1
# Переробити домашню вправу на декоратори (минуле заняття) таким чином,
# щоб вихідні заяви записувались у файл, шлях до якого вказує користувач :)
import os

request_type = input("Enter type of vacation request, one of Vacation, Sick leave, Day off: ")
first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
from_date = input(f"Enter date from which your {request_type} starts: ")
to_date = input(f"Enter date when your {request_type} ends: ")


def run_logger(func):
    def wrapper(*args, **kwargs):
        with open(os.path.join(os.path.curdir, "request.txt"), "w") as request:
            request.write(f"Title: \nCEO Red Bull Inc. \nMr. John Bigbull\nVacation type: {request_type} Pattern\nHi "
                          f"John,\nI need the paid {request_type} from {from_date} to {to_date}.\n{first_name} "
                          f"{surname}")
        return func(*args, **kwargs)

    return wrapper


@run_logger
def func():
    return None


func()
