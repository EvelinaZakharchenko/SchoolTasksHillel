# З урожаю льону на дослiднiй дiлянцi одержали 244 кг волокна льону,
# а насiння - в 2 рази менше. Скiльки кг насiння одержали?

linen = 244

def find_seed():
    seeds = linen / 2
    return seeds

print(f"""
Умова:
З урожаю льону на дослiднiй дiлянцi одержали 244 кг волокна льону,
а насiння - в 2 рази менше. Скiльки кг насiння одержали?
""")
print(f"1 дiя: {linen} : 2 = {find_seed()} (н.) - одержали")
print(f"Вiдповiдь: {find_seed()} кг насiння одержали.")