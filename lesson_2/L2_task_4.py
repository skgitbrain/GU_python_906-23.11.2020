"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125
 ...Количество элементов (n) вводится с клавиатуры.

Ссылка на блок схему:
https://clck.ru/UPNSq
"""
n = int(input('Введите кол-во элементов: '))


def sum_n(n: int, digit: int = 1, n_sum: int = 0):
    if n == 0:
        return n_sum
    else:
        n_sum += digit
        n -= 1
        return sum_n(n, digit / (-2), n_sum)


summ = sum_n(n)
print(summ)
