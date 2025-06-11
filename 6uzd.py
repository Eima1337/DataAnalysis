import random

#Naudokite funkcija random.randint(x,x). Sukurkite ir atspausdinkite 3 skaičius nuo -10 iki 10. Skaičiai mažesni už 0 turi būti  laužtiniuose skliaustuose [], 0 -  (), didesni už 0 {}.   [-4],  (0)

a = random.randint(-10, 10)
b = random.randint(-10, 10)
c = random.randint(-10, 10)

if a < 0:
    print("[" + str(a) + "]")
elif a > 0:
    print("{" + str(a) + "}")
else:
    print("(" + str(a) + ")")

if b < 0:
    print("[" + str(b) + "]")
elif b > 0:
    print("{" + str(b) + "}")
else:
    print("(" + str(b) + ")")

if c < 0:
    print("[" + str(c) + "]")
elif c > 0:
    print("{" + str(c) + "}")
else:
    print("(" + str(c) + ")")
