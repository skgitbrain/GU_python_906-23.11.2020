"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
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

print(array)
