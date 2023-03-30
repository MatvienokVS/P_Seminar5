# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

number_A = int(input('Введите число возводимое в степень: '))
number_B = int(input('Введите степень: '))


def vzvst(a, b):
    if b == 1:
        return a
    return a * vzvst(a, b - 1)


print(vzvst(number_A, number_B))
