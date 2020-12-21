from functools import reduce

def my_func(el, n_el):
    return el * n_el

my_list = [el for el in range(100, 1001) if el % 2 == 0]

print(reduce(my_func, my_list))
print(my_list)
