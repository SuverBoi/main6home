# Напишіть функцію, яка приймає два числа як параметр і відображає всі парні числа між ними.
def numrange():
    print("Choose the first number?")
    a = int(input())
    print("Choose the second number?")
    b = int(input())


    even_numbers = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            even_numbers.append(i)

    return even_numbers
print(numrange())







