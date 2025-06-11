import random

# Įmonė parduoda žvakes po 1 EUR. Perkant daugiau kaip 1000 vienetų taikoma 3 % nuolaida, daugiau kaip 2000 vienetų- 4 % nuolaida. Parašykite programą, kuri skaičiuos žvakių kainą ir atspausdintų atsakymą kiek žvakių ir kokia kaina perkama. Žvakių kiekį generuokite ​random.randint(x,x)​ funkcija nuo 5 iki 3000.

candle_count = random.randint(5, 3000)
price = 1
total = 0
discount_1000 = 0.03
discount_2000 = 0.04

if candle_count < 1000:
    total = price * candle_count
    print(f"Jus pirkote: {candle_count} zvakiu ir turite sumoketi: {total} eur.")
elif candle_count < 2000:
    price = price - (price * discount_1000)
    total = price * candle_count
    print(f"Jus pirkote: {candle_count} zvakiu ir turite sumoketi: {round(total, 2)} eur.")
else:
    price = price - (price * discount_2000)
    total = price * candle_count
    print(f"Jus pirkote: {candle_count} zvakiu ir turite sumoketi: {round(total, 2)} eur.")

