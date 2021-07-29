# Коли щодня витрачати на опалення 9 кг вугiлля, то його вистачить на 72 днi.
# На скiльки днiв вистачить вугiлля, коли щодня витрачати 8 кг

coal_1_case = 9
days_1_case = 72


def find_total_coals():
    total = coal_1_case * days_1_case
    return total


def find_days_2_case(total):
    days_2_case = total / 8
    return days_2_case


total_coals = find_total_coals()
days_2case = (find_days_2_case(total_coals))
print(f"""
Умова:
Коли щодня витрачати на опалення 9 кг вугiлля, то його вистачить на 72 днi.
На скiльки днiв вистачить вугiлля, коли щодня витрачати 8 кг?
""")
print(f"1 дiя: {coal_1_case} * {days_1_case} = {total_coals} (в.) - всього")
print(f"2 дiя: {total_coals} : 8 = {days_2case} (д.) - вистачить вугiлля")
print(f"Вiдповiдь: На {days_2case} днiв вистачить вугiлля, коли щодня витрачати 8 кг.")