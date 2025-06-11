import random

# Antra uzduotis

rand_int1 = random.randint(0, 4)
rand_int2 = random.randint(0, 4)
result = 0
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

