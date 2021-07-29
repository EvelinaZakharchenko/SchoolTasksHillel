# Зiбрали 322 кг плодiв шипшини. Пiсля сушiння маса плодiв зменшилась удвiчi.
# Скiльки вийшло кiлограмiв сухих плодiв шипшини?

collected_dog_rose = 322
reduced_times = 2


def find_after_dry():
    after_dry = collected_dog_rose / reduced_times
    return after_dry


dog_roses_after_dry = find_after_dry()
print(f"""
Умова:
Зiбрали 322 кг плодiв шипшини. Пiсля сушiння маса плодiв зменшилась удвiчi.
Скiльки вийшло кiлограмiв сухих плодiв шипшини?
""")
print(f"1 дiя: {collected_dog_rose} / {reduced_times} = {dog_roses_after_dry} (кг.) - сухих плодiв")
print(f"Вiдповiдь: {dog_roses_after_dry} зiйшло сажанцiв дуба")
