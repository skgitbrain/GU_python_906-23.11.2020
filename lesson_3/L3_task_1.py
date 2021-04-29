"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому
из чисел в диапазоне от 2 до 9.
"""

multiple_two = 0
multiple_free = 0
multiple_four = 0
multiple_five = 0
multiple_six = 0
multiple_seven = 0
multiple_eight = 0
multiple_nine = 0

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
