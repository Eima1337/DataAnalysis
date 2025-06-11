import random

# Naudokite funkcija random.randint(x,x). Sukurkite tris kintamuosius su atsitiktinėm reikšmėm nuo 0 iki 100. Paskaičiuokite jų aritmetinį vidurkį. Ir aritmetinį vidurkį atmetus tas reikšmes, kurios yra mažesnės nei 10 arba didesnės nei 90. Abu vidurkius atspausdinkite. Rezultatus apvalinkite iki sveiko skaičiaus.

a = random.randint(0, 100)
b = random.randint( 0, 100)
c = random.randint( 0, 100)

average = (a + b + c) / 3
print(f"Skaiciai: {a}, {b} ir {c}. Vidurkis: {round(average)}")

if a < 10 or a > 90:
    if b < 10 or b > 90:
        average = c
        print(f"Skaiciai: {a}, {b} ir {c}. Atmetus skaicius < 10 ir > 90 Vidurkis: {round(average)}")
    elif b >= 10 or b <= 90:
        if c < 10 or c > 90:
            average = b
            print(f"Skaiciai: {a}, {b} ir {c}. Atmetus skaicius < 10 ir > 90 Vidurkis: {round(average)}")
        else:
            average = (b + c) / 2
            print(f"Skaiciai: {a}, {b} ir {c}. Atmetus skaicius < 10 ir > 90 Vidurkis: {round(average)}")
    else:
        average = (b + c) / 2
        print(f"Skaiciai: {a}, {b} ir {c}. Atmetus skaicius < 10 ir > 90 Vidurkis: {round(average)}")
elif b < 10 or b > 90:
    if c < 10 or c < 90:
        average = a
        print(f"Skaiciai: {a}, {b} ir {c}. Atmetus skaicius < 10 ir > 90 Vidurkis: {round(average)}")
else:
    if c < 10 or c > 90:
        average = (a + b) / 2
        print(f"Skaiciai: {a}, {b} ir {c}. Atmetus skaicius < 10 ir > 90 Vidurkis: {round(average)}")
    else:
        print(f"Skaiciai: {a}, {b} ir {c}. Atmetus skaicius < 10 ir > 90 Vidurkis: {round(average)}")

