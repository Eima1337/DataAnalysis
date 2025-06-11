import random

# Sukurkite du kintamuosius ir naudodamiesi funkcija random.randint(x,x) jiems priskirkite atsitiktines reikšmes nuo 0 iki 4. Didesnę reikšmę padalinkite iš mažesnės. Atspausdinkite rezultatą jį suapvalinę iki 2 skaičių po kablelio.

rand_int1 = random.randint(0, 4)
rand_int2 = random.randint(0, 4)
result = 0

if rand_int1 > rand_int2:
    if rand_int2 != 0:
        result = rand_int1 / rand_int2
        print(f"Dalybos {rand_int1} / {rand_int2} rezultatas: {round(result, 2)}")
    else:
        print("Dalyba is 0 negalima!")
elif rand_int1 < rand_int2:
    if rand_int1 != 0:
        result = rand_int2 / rand_int1
        print(f"Dalybos {rand_int2} / {rand_int1} rezultatas: {round(result, 2)}")
    else:
        print("Dalyba is 0 negalima!")
else:
    print("Abu skaiciai vienodi, rezultatas yra 1.")

try:
    if rand_int1 > rand_int2:
        result = rand_int1 / rand_int2
        print(f"Dalybos {rand_int1} / {rand_int2} rezultatas: {round(result, 2)}")
    elif rand_int1 < rand_int2:
        result = rand_int2 / rand_int1
        print(f"Dalybos {rand_int2} / {rand_int1} rezultatas: {round(result, 2)}")
    else:
        result = 1
        print(f"{result}")
except ZeroDivisionError:
    print("Dalyba is 0 negalima.")

