import random

# Sukurkite keturis kintamuosius ir ​random.randint(x,x)​ funkcija sugeneruokite jiems reikšmes nuo 0 iki 2. Suskaičiuokite kiek yra nulių, vienetų ir dvejetų. (sprendimui masyvo nenaudoti).

a = random.randint(0, 2)
b = random.randint(0, 2)
c = random.randint(0, 2)
d = random.randint(0, 2)
int1 = 0
int2 = 0
int3 = 0

if a == 1:
    int1 += 1
elif a == 2:
    int2 += 1
else:
    int3 += 1
if b == 1:
    int1 += 1
elif b == 2:
    int2 += 1
else:
    int3 += 1
if c == 1:
    int1 += 1
elif c == 2:
    int2 += 1
else:
    int3 += 1
if d == 1:
    int1 += 1
elif d == 2:
    int2 += 1
else:
    int3 += 1

print(f"Skaiciai: {a}, {b}, {c}, {d}. Vienetu skaicius: {int1}, dvejetu skaicius: {int2} ir nuliu skaicius: {int3}.")