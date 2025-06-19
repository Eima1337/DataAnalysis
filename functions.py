import random

print("----------------1 uzduotis----------------")


def comp(n1=0, n2=0):
    return n1 + n2


print(comp(1, 2))
print("----------------2 uzduotis----------------")


def PISq():
    return 9.8596


print(PISq())
print("----------------3 uzduotis----------------")


def multiply(n1=0, n2=0):
    return n1 * n2


print(multiply(5, 5))
print("----------------4 uzduotis----------------")


def print_array_values(array):
    for value in array:
        print(value)


arr = [1, 2, 3, 4, 5]

print_array_values(arr)
print("----------------5 uzduotis----------------")


def rand_int(min=0, max=0):
    return random.randint(min, max)


print(rand_int(5, 100))
print("----------------6 uzduotis----------------")


def rand_array(min=0, max=0, length=0):
    array = []
    while len(array) != length:
        array.append(random.randint(min, max))
    return array


print(rand_array(1, 50, 50))
print("----------------7 uzduotis----------------")

arr1 = rand_array(1, 50, 100)


def my_function_7(array):
    return sum(array)


print(my_function_7(arr1))
print("----------------8 uzduotis----------------")


def my_array_avg(array):
    return round(sum(array) / len(array), 2)


print(my_array_avg(arr1))
print("----------------9 uzduotis----------------")


def rectangle(length=0, width=0):
    # print(("*" * length + "\n") * width, end="")
    for i in range(length):
        for j in range(width):
            print("*", end=" ")
        print()


rectangle(6, 5)
print("----------------10 uzduotis----------------")


def symbol_calc(string):
    length = len(string)
    spaces_count = len(string.split()) - 1
    letter_count = length - spaces_count
    return letter_count, spaces_count


str1 = "Šiandien labai graži diena"

print(symbol_calc(str1))
print("----------------11 uzduotis----------------")


def reversed_string(string):
    return string[::-1]


print(reversed_string(str1))

print("------------ Sunkesnes uzduotys-----------")
print("----------------1 uzduotis----------------")


def weird_string(text):
    print("---" + text + "---")


weird_string("aha")
print("----------------2 uzduotis----------------")


def password_generator(length):
    symbols = "0123456789ABCDEFGHIJKLMNOQRSTUVWXYZ"
    text = ""
    for i in range(length):
        random_symbol = random.choice(symbols)
        text += random_symbol
    return text


# print(password_generator(10))
password = password_generator(10)
print(password)


def password_printer(text):
    i = 0
    while i < len(text):
        if text[i].isdigit():
            start = i
            while i < len(text) and text[i].isdigit():
                i += 1
            print(f"[{text[start:i]}]")
        else:
            print(text[i])
            i += 1


password_printer(password)
print("----------------3 uzduotis----------------")


def division(number):
    count = 0
    for i in range(2, number):
        if number % i == 0:
            count += 1
    return count


print(division(16))
print("----------------4 uzduotis----------------")

arr2 = rand_array(33, 77, 100)


def sorting_by_division(array):
    return sorted(array, key=lambda x: (-division(x), x))


print(sorting_by_division(arr2))
# sorted_arr2 = sorting_by_division(arr2)
# for number in sorted_arr2:
#     print(f"{number} (dalikliu skaicius: {division(number)}")
print("----------------5 uzduotis----------------")

arr3 = rand_array(333, 777, 100)


def prime_count(array):
    count = 0
    for number in array:
        if number < 2:
            continue
        prime = True
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                prime = False
                break
        if prime:
            count += 1
    return count


print(arr3)
print(prime_count(arr3))
print("----------------6 uzduotis----------------")


def random_array_generator():
    def generate_array(depth):
        if depth == 0:
            return 0
        length = random.randint(10, 20)
        arr = [random.randint(0, 10) for _ in range(length - 1)]
        arr.append(generate_array(depth - 1))
        return arr

    depth = random.randint(10, 30)
    return generate_array(depth)


result = random_array_generator()
print(result)
print("----------------7 uzduotis----------------")


def sum_elements(arr):
    if isinstance(arr, int):
        return arr
    elif isinstance(arr, list):
        return sum(sum_elements(item) for item in arr)
    return 0


print(sum_elements(result))
print("----------------8 uzduotis----------------")


def generate_array():
    arr = [random.randint(1, 33) for _ in range(3)]
    while prime_count(arr[-3:]) != 3:
        arr.append(random.randint(1, 33))
    return arr


prime_array = generate_array()
print(prime_array)

print("----------------9 uzduotis----------------")


def generate_matrix_with_prime_average():
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    while True:
        matrix = []
        for _ in range(10):
            row = [random.randint(1, 100) for _ in range(10)]
            matrix.append(row)
        while True:
            prime_numbers = []
            for row in matrix:
                for num in row:
                    if is_prime(num):
                        prime_numbers.append(num)
            if len(prime_numbers) > 0:
                average = sum(prime_numbers) / len(prime_numbers)
                print(f"Average primes: {average}")
            else:
                average = 0

            if average >= 70:
                return matrix

            smallest = matrix[0][0]
            smallest_row = 0
            smallest_col = 0
            for i in range(10):
                for j in range(10):
                    if matrix[i][j] < smallest:
                        smallest = matrix[i][j]
                        smallest_row = i
                        smallest_col = j
            matrix[smallest_row][smallest_col] += 3


print(generate_matrix_with_prime_average())