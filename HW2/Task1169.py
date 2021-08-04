# Маса 300 жолудiв 1 кг. У лiсорозсаднику посадили 2 кг жолудiв.
# Не зiйшла десята частина жолудiв. Скiльки зiйшло сажанцiв дуба?

weight_of_1_kg_acorns = 300
kg_acrons_in_forest = 2
not_grow_acrons = 0.1


def find_total():
    total = weight_of_1_kg_acorns * kg_acrons_in_forest
    return total


def find_grown_oaks(total):
    grown = total * (1 - not_grow_acrons)
    return grown


total_acrons = find_total()
grown_oaks = find_grown_oaks(total_acrons)
print(f"""
Умова:
Маса 300 жолудiв 1 кг. У лiсорозсаднику посадили 2 кг жолудiв.
Не зiйшла десята частина жолудiв. Скiльки зiйшло сажанцiв дуба?
""")
print(f"1 дiя: {weight_of_1_kg_acorns} * {kg_acrons_in_forest} = {total_acrons} (в.) - всього жолудiв")
print(f"2 дiя: {total_acrons} * (1- {not_grow_acrons}) = {grown_oaks} (д.) - зiйшло")
print(f"Вiдповiдь: {grown_oaks} зiйшло сажанцiв дуба")
