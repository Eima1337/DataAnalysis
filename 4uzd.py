import random

# Įvedami skaičiai - a, b, c –kraštinių ilgiai, trys kintamieji (naudokite ​random.randint(x,x)​ funkciją nuo 1 iki 10). Parašykite Python programą, kuri nustatytų, ar galima sudaryti trikampį ir atsakymą atspausdintų.

a = random.randint(1, 10)
b = random.randint(1, 10)
c = random.randint(1, 10)

if (a + b) > c and (a + c) > b and (b + c) > a:
    print(f"Trikampis gaunasi! Krastiniu ilgiai: a = {a}, b = {b} ir c = {c}")
else:
    print(f"Trikampis nesigauna! Krastiniu ilgiai: a = {a}, b = {b} ir c = {c}")


