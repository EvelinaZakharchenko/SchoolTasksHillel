#У буртi було 600 кг кавунiв. Першого дня продали 1/6 всiх кавунiв,
#а другого - на 27 кг бiльше. Скiльки кг кавунiв залишилося?

total_watermelons = 600


def find_first_day_sales():
  sales_1st_day = total_watermelons / 6
  return sales_1st_day


def find_second_day_sales(first_day):
    sales_2nd_day = first_day + 27
    return sales_2nd_day


def find_remainder(first_day, second_day):
    remainder = total_watermelons - first_day - second_day
    return remainder


first_day = (find_first_day_sales())
second_day = (find_second_day_sales(first_day))
left = (find_remainder(first_day, second_day))
print(f"""
Умова:
У буртi було 600 кг кавунiв. Першого дня продали 1/6 всiх кавунiв,
а другого - на 27 кг бiльше. Скiльки кг кавунiв залишилося?
""")
print(f"1 дiя: 600 : 6 = {first_day} (к.) - продали першого дня")
print(f"2 дiя: {first_day} + 27 = {second_day} (к.) - продали другого дня")
print(f"3 дiя: {total_watermelons} - {first_day} - {second_day} = {left} (к.) - залишилося")
print(f"Вiдповiдь: {left} кг кавунiв залишилося.")