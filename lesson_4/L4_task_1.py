"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому
из чисел в диапазоне от 2 до 9.
"""
import timeit
import cProfile


# VER_1
def play(n):
    multiple_two = 0
    multiple_three = 0
    multiple_four = 0
    multiple_five = 0
    multiple_six = 0
    multiple_seven = 0
    multiple_eight = 0
    multiple_nine = 0

    for i in range(2, n + 1):
        if i % 2 == 0:
            multiple_two += 1
        if i % 3 == 0:
            multiple_three += 1
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

    return f'Кол-во кратное 2: {multiple_two}\nКол-во кратное 3: {multiple_three}\nКол-во кратное 4: {multiple_four}\n\
Кол-во кратное 5: {multiple_five}\nКол-во кратное 6: {multiple_six}\nКол-во кратное 7: {multiple_seven}\n\
Кол-во кратное 8: {multiple_eight}\nКол-во кратное 9: {multiple_nine}'


print(timeit.timeit('play(10)', number=100, globals=globals()))  # 0.00046670000000000045
print(timeit.timeit('play(100)', number=100, globals=globals()))  # 0.0038700000000000054
print(timeit.timeit('play(1000)', number=100, globals=globals()))  # 0.040012799999999994
print(timeit.timeit('play(10000)', number=100, globals=globals()))  # 0.4062557
print(timeit.timeit('play(100000)', number=100, globals=globals()))  # 4.5678013
print("______________________________")

cProfile.run('play(10000000)')
print("______________________________")


# VER_2

def play_2(n):
    for i in range(2, 9 + 1):
        multiple = 0
        for j in range(2, n + 1):
            if j % i == 0:
                multiple += 1
        return f'Кол-во кратное {i}: {multiple}'


print(timeit.timeit('play_2(10)', number=100, globals=globals()))  # 0.00015030000000000251
print(timeit.timeit('play_2(100)', number=100, globals=globals()))  # 0.0006286
print(timeit.timeit('play_2(1000)', number=100, globals=globals()))  # 0.0070098
print(timeit.timeit('play_2(10000)', number=100, globals=globals()))  # 0.1152173
print(timeit.timeit('play_2(100000)', number=100, globals=globals()))  # 0.9539030000000001
print("______________________________")

cProfile.run('play_2(10000000)')
print("______________________________")


# VER_3
def play_3(n):
    multiple = [0] * 8
    for i in range(2, n + 1):
        for j in range(2, 9 + 1):
            if i % j == 0:
                multiple[j - 2] += 1
    for i, item in enumerate(multiple, start=2):
        return (f'Кол-во кратное {i}: {item}')


print(timeit.timeit('play_3(10)', number=100, globals=globals()))  # 0.0008206000000000012
print(timeit.timeit('play_3(100)', number=100, globals=globals()))  # 0.010804400000000002
print(timeit.timeit('play_3(1000)', number=100, globals=globals()))  # 0.08329639999999999
print(timeit.timeit('play_3(10000)', number=100, globals=globals()))  # 0.8615165
print(timeit.timeit('play_3(100000)', number=100, globals=globals()))  # 12.4981098
print("______________________________")
cProfile.run('play_3(10000000)')

# Вариант 2 лучше, так как он быстрее обрабатывает большие числа.
