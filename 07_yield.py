from math import factorial

n = int(input('Введите конечный элемент последовательности факториалов 0!-n! '))

# def factorial(n):
#     if n == 0:
#         return 1
#     return factorial(n-1) * n


def factorial_gen(n):
    for el in range(n+1):
        yield factorial(el)


for el in factorial_gen(n):
    print(el)
