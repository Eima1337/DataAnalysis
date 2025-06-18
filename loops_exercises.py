import random

print("----------------1 uzduotis----------------")

for i in range(10):
    print(f"Labas {i + 1}")

print("----------------1 uzduotis----------------")

print("----------------2 uzduotis----------------")

for i in range(10):
    print(i)

print("----------------2 uzduotis----------------")

print("----------------3 uzduotis----------------")

plants = ["oak", "willow", "maple", "yew", "redwood", "pineapple", "banana", "apple", "strawberry", "watermelon"]

print("----------------3 uzduotis----------------")
print("----------------4 uzduotis----------------")

for plant in plants:
    print(plant)

print("----------------4 uzduotis----------------")
print("----------------5 uzduotis----------------")

reversed_plants = plants[::-1]

for plant in reversed_plants:
    print(plant)

print("----------------5 uzduotis----------------")
print("----------------6 uzduotis----------------")

for i in range(10, 51):
    if i % 2 == 0:
        print(i)

print("----------------6 uzduotis----------------")
print("----------------7 uzduotis----------------")

for i in range(10, 51):
    if i % 2 == 0 and i % 10 != 0:
        print(i)

print("----------------7 uzduotis----------------")
print("----------------8 uzduotis----------------")

count = 0
for i in range(0, 20):
    if i % 2 == 0:
        count += 1
print(count)

print("----------------8 uzduotis----------------")
print("----------------9 uzduotis----------------")
count1 = 0
count2 = 0
for plant in plants:
    if len(plant) < 5:
        count1 += 1
    elif len(plant) > 7:
        count2 += 1
print(f"Augalu liste yra zodziai trumpesni nei 5 simboliai: {count1} ir ilgesni nei 7 simboliai: {count2}")
print("----------------9 uzduotis----------------")
print("----------------10 uzduotis----------------")
count = 0
for plant in plants:
    if 5 < len(plant) < 10:
        count += 1

print(f"Augalu liste yra {count} zodziai, kurie trumpesni nei 10, bet ilgesni nei 5 simboliai.")

print("----------------10 uzduotis----------------")

# Sunkesni uzdaviniai

print("----------------1 uzduotis----------------")

# random_nums = []
#
# while len(random_nums) != 300:
#     random_num = random.randint(0, 300)
#     random_nums.append(random_num)
#
# print(random_nums)
#
# for num in random_nums:
#     if num > 275:
#         print(f"[{num}]", end=" ")
#         continue
#     print(num, end=" ")
#
# print()

stringas = ""

for i in range(1, 301):
    rand_int = random.randint(0, 300)
    if rand_int > 275:
        stringas += "[" + str(rand_int) + "] "
    else:
        stringas += str(rand_int) + " "

print()
print(stringas)

print()
print("----------------1 uzduotis----------------")
print("----------------2 uzduotis----------------")

string = ""

for i in range(1, 3001):
    if i % 77 == 0:
        string += str(i) + ","

if string.endswith(","):
    string = string[:-1]

print(string)
print("----------------2 uzduotis----------------")
print("----------------3 uzduotis----------------")
square_size = 25

for i in range(square_size):
    print("*" * 25)

print("----------------3 uzduotis----------------")
print("----------------4 uzduotis----------------")

for i in range(square_size):
    line = ""
    for j in range(square_size):
        if i == j or j == square_size - i - 1:
            line += "3"
        else:
            line += "*"
    print(line)

print()

print("----------------4 uzduotis----------------")
print("----------------5 uzduotis----------------")

h_count = 0

# Iskrito herbas
print("Iskrito herbas")

while True:
    coin = random.randint(0, 1)
    if coin == 0:
        print("H")
        break
    else:
        print("S")

# Tris kartus iskrito herbas

print("Iskrito herbas tris kartus")

while True:
    coin = random.randint(0, 1)
    if coin == 0:
        print("H")
        h_count += 1
        if h_count == 3:
            break
    else:
        print("S")

# Tris kartus is eiles iskrito herbas

print("Tris kartus is eiles iskrito herbas")

h_in_a_row = 0

while h_in_a_row < 3:
    coin = random.randint(0, 1)
    if coin == 0:
        print("H")
        h_in_a_row += 1
    else:
        print("S")
        h_in_a_row = 0


print("----------------5 uzduotis----------------")
print("----------------6 uzduotis----------------")

petras_total = 0
kazys_total = 0

while True:
    petras_points = random.randint(10, 20)
    kazys_points = random.randint(5, 25)
    petras_total = petras_total + petras_points
    kazys_total = kazys_total + kazys_points
    if petras_total >= 222 or kazys_total >= 222:
        break

if petras_total > kazys_total:
    print(f"Partija laimejo Petras, jo taskai: {petras_total}, pralaimejo Kazys, jo taskai: {kazys_total}")
elif petras_total < kazys_total:
    print(f"Partija laimejo Kazys, jo taskai: {kazys_total}, pralaimejo Petras, jo taskai: {petras_total}")
else:
    print(f"LYGIOSIOS. Petro taskai: {petras_total}, Kazio taskai: {kazys_total}")

print("----------------6 uzduotis----------------")
print("----------------7 uzduotis----------------")

height = 21
mid = height // 2

for i in range(height):
    if i <= mid:
        #Skaiciuoju kiek eiluteje zvaigzduciu iki vidurines eilutes (iskaitant vidurine)
        stars = 2 * i + 1
    else:
        #Skaiciuoju kiek eiluteje zvaigzduciu po vidurines eilutes
        stars = 2 * (height - i - 1) + 1
    #skaiciuoju tarpu skaiciu pries zvaigzdutes
    spaces = (height - stars) // 2
    print(" " * spaces + "*" * stars)

print("----------------7 uzduotis----------------")
print("----------------8 uzduotis----------------")

vinis = 85
mazu_kalimu_skaicius = 0
dideliu_kalimu_skaicius = 0

while True:
    mazas_smugis = random.randint(5, 20)
    vinis = vinis - mazas_smugis
    mazu_kalimu_skaicius += 1
    if vinis <= 0:
        print(f"\nMazu kalimu skaicius: {mazu_kalimu_skaicius}")
        break

vinis = 85

while True:
    didelis_smugis = random.randint(20, 30)
    ikalimo_tikimybe = random.randint(0, 1)
    if ikalimo_tikimybe > 0:
        vinis = vinis - didelis_smugis
        dideliu_kalimu_skaicius += 1
    if vinis <= 0:
        print(f"\nDideliu kalimu skaicius: {dideliu_kalimu_skaicius}")
        break

print("----------------8 uzduotis----------------")
print("----------------9 uzduotis----------------")

num_list = []
num_string1 = ""
prime_list = []
num_string2 = ""
while len(num_list) < 50:
    random_number = random.randint(1,200)
    if random_number not in num_list:
        num_list.append(random_number)

num_list.sort()

for number in num_list:
    num_string1 += str(number) + " "

for number in num_list:
    if number < 2:
        continue
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_list.append(number)

prime_list.sort()

for number in prime_list:
    num_string2 += str(number) + " "

print(f"50 Unikaliu skaiciu: {num_string1}")
print(f"Pirminiai skaiciai: {num_string2}")

print("----------------9 uzduotis----------------")



