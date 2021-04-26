"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random

size = 10
min_item = 0
max_item = 100
array = [random.randint(min_item, max_item) for _ in range(size)]

min_num = array[0]
max_num = array[0]

for i in range(len(array)):
    if min_num > array[i]:
        min_num = array[i]

    if max_num < array[i]:
        max_num = array[i]

array[array.index(min_num)] = max_num
array[array.index(max_num)] = min_num

if min_num > max_num:
    min_num, max_num = max_num, min_num

print(min_num, max_num)
sum_ = 0
for i in range(array.index(min_num) + 1, array.index(max_num)):
    sum_ += array[i]
print(f'Сумма элементов равна = {sum_}')
print(array)
