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
    print(("*" * length + "\n") * width, end="")
    # for i in range(length):
    #     line = "*" * width
    #     print(line)


rectangle(5, 5)
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
