import random

#Naudokite funkcija random.randint(x,x). Sukurkite tris kintamuosius ir naudodamiesi funkcija random.randint(x,x) jiems priskirkite atsitiktines reikšmes nuo 0 iki 25. Raskite ir atspausdinkite kintąmąjį turintį vidurinę reikšmę.

rand_int1 = random.randint(0, 25)
rand_int2 = random.randint(0, 25)
rand_int3 = random.randint(0, 25)
sum = rand_int1 + rand_int2 + rand_int3

print(f"Skaiciu: {rand_int1}, {rand_int2} ir {rand_int3} vidurkis yra: {round((sum / 3), 2)}")