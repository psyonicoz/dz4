from random import randint


my_list = [el + randint(0, 20) for el in range(10)]
result_list = []

for el in my_list:
    if my_list.count(el) == 1:
        result_list.append(el)
print(my_list)
print(result_list)
