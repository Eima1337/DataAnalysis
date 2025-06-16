import random
import re
print("----------------1 uzduotis----------------")

name = "Ryan"
last_name = "Reynolds"

if len(name) > len(last_name):
    print(last_name)
else:
    print(name)

print("----------------1 uzduotis----------------")

print("----------------2 uzduotis----------------")

print(name.upper(), last_name.lower())

print("----------------2 uzduotis----------------")

print("----------------3 uzduotis----------------")

initials = name[0] + last_name[0]
print(initials)

print("----------------3 uzduotis----------------")

print("----------------4 uzduotis----------------")

new_name = name[-3:] + last_name[-3:]
print(new_name)

print("----------------4 uzduotis----------------")

print("----------------5 uzduotis----------------")

string1 = "An American in Paris"
print(re.sub("[aA]", "*", string1))

print("----------------5 uzduotis----------------")

print("----------------6 uzduotis----------------")

string2 = "Breakfast at Tiffany's"
string3 = "2001: A Space Odyssey"
string4 = "It's a Wonderful Life"
print(re.sub("[aAeEiIoOuUyY]", "", string1))
print(re.sub("[aAeEiIoOuUyY]", "", string2))
print(re.sub("[aAeEiIoOuUyY]", "", string3))
print(re.sub("[aAeEiIoOuUyY]", "", string4))

print("----------------6 uzduotis----------------")

print("----------------7 uzduotis----------------")

starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"
number_in_string = re.findall(r"\d+", starWars)
print(starWars)
print(number_in_string[0])

print("----------------7 uzduotis----------------")

print("----------------8 uzduotis----------------")

menace = "Don't Be a Menace to South Central While Drinking Your Juice in the Hood"
siaubas = "Tik nereikia gąsdinti Pietų Centro, geriant sultis pas save kvartale"
menace = menace.split(" ")
siaubas = siaubas.split(" ")
count = 0

for word in menace:
    if len(word) <= 5:
        count += 1

print(f"Zodziai trumpesni arba lygus 5: {count}")

print(menace)

count = 0

for word in siaubas:
    if len(word) <= 5:
        count += 1

print(f"Zodziai trumpesni arba lygus 5: {count}")

print(siaubas)

print("----------------8 uzduotis----------------")

print("----------------9 uzduotis----------------")

latin = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

symbol1 = random.randint(0, len(latin) - 1)
symbol2 = random.randint(0, len(latin) - 1)
symbol3 = random.randint(0, len(latin) - 1)

random_string = latin[symbol1] + latin[symbol2] + latin[symbol3]
print(random_string)

print("----------------9 uzduotis----------------")

print("----------------10 uzduotis----------------")

menace = "Don't Be a Menace to South Central While Drinking Your Juice in the Hood"
siaubas = "Tik nereikia gąsdinti Pietų Centro, geriant sultis pas save kvartale"
menace = menace.split(" ")
siaubas = siaubas.split(" ")

menace_siaubas = menace + siaubas
ilgis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

random_words = []

while len(random_words) < 10:
    random_word = menace_siaubas[random.randint(0, len(menace_siaubas) - 1)]
    if random_word not in random_words:
        random_words.append(random_word)

print(random_words)
print("----------------10 uzduotis----------------")



