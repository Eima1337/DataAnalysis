import random
import string
print("----------------1 uzduotis----------------")

numbers = []
new_numbers = []
index = 0

for i in range(30):
    numbers.append(random.randint(5, 25))

print(numbers)

print("----------------2 uzduotis----------------")

count = 0

for number in numbers:
    if number > 10:
        count += 1

print(f"Skaiciai didesni uz 10: {count}")

print(f"Maksimali reiksme: {max(numbers)}")

print(f"Skaiciu suma: {sum(numbers)}")

for number in numbers:
    new_numbers.append(number - index)
    index += 1

print(new_numbers)

for i in range(10):
    numbers.append(random.randint(5, 25))

print(numbers)

index = 0
even_indexes = []
odd_indexes = []

for number in numbers:
    if index % 2 == 0:
        even_indexes.append(numbers[index])
    else:
        odd_indexes.append(numbers[index])
    index += 1

print(even_indexes)
print(odd_indexes)

for i in range(len(even_indexes)):
    if even_indexes[i] > 15:
        even_indexes[i] = 0

print(even_indexes)

for i in range(len(numbers)):
    if numbers[i] > 10:
        print(i)
        break

for i, value in enumerate(numbers):
    if value > 10:
        print(i)
        break

print("----------------3 uzduotis----------------")

letters = []
random_letters = "ABCD"
sorted_letters = []
a_count = 0
b_count = 0
c_count = 0
d_count = 0

while len(letters) < 200:
    letters.append(random.choice(random_letters))

for letter in letters:
    if letter == "A":
        a_count += 1
    elif letter == "B":
        b_count += 1
    elif letter == "C":
        c_count += 1
    else:
        d_count += 1

print(letters)
print(f"A raidziu: {a_count}, B raidziu {b_count}, C raidziu {c_count} ir D raidziu {d_count}")

print("----------------4 uzduotis----------------")

for letter in sorted(letters):
    sorted_letters.append(letter)

print(sorted_letters)

print("----------------5 uzduotis----------------")

letters1 = []
letters2 = []
letters3 = []
letters4 = []
unique_combinations = []

while len(letters1) < 200 and len(letters2) < 200 and len(letters3) < 200:
    letters1.append(random.choice(random_letters))
    letters2.append(random.choice(random_letters))
    letters3.append(random.choice(random_letters))

for i in range(200):
    letters4.append(letters1[i] + letters2[i] + letters3[i])

for combination in letters4:
    if combination not in unique_combinations:
        unique_combinations.append(combination)

print(letters4)
print(f"Unikaliu reiksmiu skaicius: {len(unique_combinations)}")

print("----------------6 uzduotis----------------")

numbs1 = []
numbs2 = []

while len(numbs1) < 200:
    number = random.randint(100,999)
    if number not in numbs1:
        numbs1.append(number)

while len(numbs2) < 200:
    number = random.randint(100,999)
    if number not in numbs2:
        numbs2.append(number)

print(numbs1)
print(numbs2)
print(sorted(numbs1))
print(sorted(numbs2))
print("----------------7 uzduotis----------------")

numbs3 = []

for n1, n2 in zip(numbs1, numbs2):
    if n1 not in numbs2:
        numbs3.append(n1)

print(sorted(numbs3))

print("----------------8 uzduotis----------------")

numbs3 = []

for i, n1 in enumerate(numbs1):
    # print(f"i: {i}, n1: {n1}")
    for j, n2 in enumerate(numbs2):
        # print(f"j: {j}, n2: {n2}")
        if n1 == n2:
            numbs3.append(n1)

print(sorted(numbs3))

print("----------------9 uzduotis----------------")

crazy_ints = []

for i in range(10):
    number = random.randint(5, 25)
    if i < 2:
        crazy_ints.append(number)
    else:
        crazy_ints.append(crazy_ints[i - 2] + crazy_ints[i - 1])

print(crazy_ints)

print("----------------10 uzduotis----------------")

max_diff = 30
listas = []

while len(listas) < 101:
    number = random.randint(0, 300)
    if number not in listas:
        listas.append(number)

listas.sort(reverse=True)
result = [0] * 101
center_index = len(listas) // 2
result[center_index] = listas[0]
left = center_index - 1
right = center_index + 1
index = 1

while index < len(listas):
    if right < len(result):
        result[right] = listas[index]
        index += 1
        right += 1
    if index < len(listas) and left >= 0:
        result[left] = listas[index]
        index += 1
        left -= 1
sum_left = sum(result[:center_index])
sum_right = sum(result[center_index:])

print(sum_left)
print(sum_right)
print(abs(sum_left - sum_right))
print(result)

# while True:
#     listas.sort(reverse=True)
#     result = [0] * 101
#     center_index = len(result) // 2
#     result[center_index] = listas[0]
#     left = center_index - 1
#     right = center_index + 1
#     index = 1
#     sum_left = sum(result[:center_index])
#     sum_right = sum(result[center_index:])
#     if abs(sum_left - sum_right) >= 30:
#         while index < len(listas):
#             if right < len(result):
#                 result[right] = listas[index]
#                 index += 1
#                 right += 1
#             if index < len(listas) and left >= 0:
#                 result[left] = listas[index]
#                 index += 1
#                 left -= 1
#     else:
#         break

print(result)

# print(listas)
# listas.sort()
# max_value = listas.pop()
# center_index = len(listas) // 2
# left = listas[:center_index]
# right = listas[center_index:][::-1]
# print(left + [max_value] + right)
#
# while True:
#     listas.sort()
#     max_value = listas.pop()
#     center_index = len(listas) // 2
#     left = listas[:center_index]
#     right = listas[center_index:][::-1]
#     if left[-1] < max_value and right[-1] < max_value:
#         sum_left = sum(left)
#         sum_right = sum(right)
#         if abs(sum_left - sum_right) <= 30:
#             break
#
# print(left + [max_value] + right)

# print(listas)
# print(sorted(listas))
#
# listas.sort()
# max_value = listas.pop()
# # print(max_value)
# left = listas[:50]
# right = listas[50:][::-1]
#
# sum_left = sum(left)
# sum_right = sum(right)
# print(f"Skirtumas {abs(sum_left - sum_right)}")
#
#
# # print(sum(left))
# # print(sum(right))
# print(left + [max_value] + right)



