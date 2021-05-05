"""
Пользователь вводит данные о количестве предприятий, их
и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

"""

from collections import deque

number_of_enterprises = int(input("Введите кол-во предприятий: "))
quarters = 4
all_companies = {}
total_profit = 0

for i in range(1, number_of_enterprises + 1):
    enterprises = input(f"Введите название предприятия {i}: ")

    summ_quarters = 0
    for y in range(1, quarters + 1):
        quarter = int(input(f"Введите прибыль за {y} квартал: "))
        summ_quarters += quarter
    total_profit += summ_quarters
    all_companies[enterprises] = summ_quarters

avarage_total_profit = total_profit / number_of_enterprises
print(all_companies)
print(total_profit)
print(avarage_total_profit)

list = []
for key, value in all_companies.items():
    list.append([key, value])
print(list)

sort_ = deque([None])
for key, value in all_companies.items():
    if value > avarage_total_profit:
        sort_.append([key, value])
    elif value < avarage_total_profit:
        sort_.appendleft([key, value])

text = "Меньше"
for x in sort_:
    if x is None:
        text = "Больше"
    else:
        print(f"Компания {x[0]} заработала {text}, чем средняя прибыль, а именно: {x[1]}")
