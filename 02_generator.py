from random import randint

my_list = [el + randint(0, 10) for el in range(10)]
result_list = []

print(list(my_list))
for z in range(len(my_list)):
    try:
        if my_list[z+1] > my_list[z]:
            result_list.append(my_list[z+1])
    except:
        print(result_list)
