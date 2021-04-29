"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.


"""
import random

size = 10
min_item = -200
max_item = -100
array = [random.randint(min_item, max_item) for _ in range(size)]

index = -1
max_negative_element = array[0]
for i in range(1, len(array)):
    if array[i] < 0 and index == -1:
        index = i
    elif 0 > array[i] > array[index]:
        index = i
    i += 1
if index != -1:
    print(f'{array[index]} and {index}')
