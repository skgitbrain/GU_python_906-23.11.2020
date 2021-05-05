"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому
из чисел в диапазоне от 2 до 9.
"""
import sys

# VER_1

import sys

multiple_two = 0
multiple_free = 0
multiple_four = 0
multiple_five = 0
multiple_six = 0
multiple_seven = 0
multiple_eight = 0
multiple_nine = 0
summ = 0

for i in range(2, 99 + 1):
    if i % 2 == 0:
        multiple_two += 1
    if i % 3 == 0:
        multiple_free += 1
    if i % 4 == 0:
        multiple_four += 1
    if i % 5 == 0:
        multiple_five += 1
    if i % 6 == 0:
        multiple_six += 1
    if i % 7 == 0:
        multiple_seven += 1
    if i % 8 == 0:
        multiple_eight += 1
    if i % 9 == 0:
        multiple_nine += 1

print(f'Кол-во кратное 2: {multiple_two}')
print(f'Кол-во кратное 3: {multiple_free}')
print(f'Кол-во кратное 4: {multiple_four}')
print(f'Кол-во кратное 5: {multiple_five}')
print(f'Кол-во кратное 6: {multiple_six}')
print(f'Кол-во кратное 7: {multiple_seven}')
print(f'Кол-во кратное 8: {multiple_eight}')
print(f'Кол-во кратное 9: {multiple_nine}')

summ += sys.getsizeof(multiple_two)
summ += sys.getsizeof(multiple_free)
summ += sys.getsizeof(multiple_four)
summ += sys.getsizeof(multiple_five)
summ += sys.getsizeof(multiple_six)
summ += sys.getsizeof(multiple_seven)
summ += sys.getsizeof(multiple_eight)
summ += sys.getsizeof(multiple_nine)
summ += sys.getsizeof(i)
summ += sys.getsizeof(range(2, 99 + 1))
print(f'Вариант 1 переменные заняли в сумме {summ} байт')
print("*" * 30)

# VER_2
sum_ = 0
for i in range(2, 9 + 1):
    multiple = 0
    for j in range(2, 99 + 1):
        if j % i == 0:
            multiple += 1
    print(f'Кол-во кратное {i}: {multiple}')

sum_ += sys.getsizeof(i)
sum_ += sys.getsizeof(range(2, 9 + 1))
sum_ += sys.getsizeof(range(2, 99 + 1))
sum_ += sys.getsizeof(j)
sum_ += sys.getsizeof(multiple)
print(f'Вариант 2 переменные заняли в сумме {sum_} байт')
print("*" * 30)

# VER_3
sumk_ = 0
multiple = [0] * 8
for i in range(2, 99 + 1):
    for j in range(2, 9 + 1):
        if i % j == 0:
            multiple[j - 2] += 1
for i, item in enumerate(multiple, start=2):
    print(f'Кол-во кратное {i}: {item}')
sumk_ += sys.getsizeof(multiple)
sumk_ += sys.getsizeof(i)
sumk_ += sys.getsizeof(range(2, 99 + 1))
sumk_ += sys.getsizeof(j)
sumk_ += sys.getsizeof(range(2, 9 + 1))
sumk_ += sys.getsizeof(item)
sumk_ += sys.getsizeof(enumerate(multiple, start=2))
print(f'Вариант 3 переменные заняли в сумме {sumk_} байт')

# Вывод: Самый экономичный вариант 2
