"""
 В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не
 более чем за 10 попыток.   После каждой неудачной попытки должно сообщаться больше или меньше введенное
 пользователем число, чем то, что загадано.
 Если за 10 попыток число не отгадано, то вывести загаданное число.

 Ссылка на блок схему:
https://clck.ru/UPNSq
"""

from random import randint

attemp = 10
digit = randint(0, 100)

while True:
    attemp -= 1
    if attemp < 0:
        print(f'Все попытки закончились, загадданое число - {digit}')
        break
    dig_input = int(input('Введите число: '))
    if dig_input == digit:
        print(f"Поздравляем! Вы угадали число {digit}")
        break
    elif digit > dig_input:
        print("Ваше число меньше")
    else:
        print("Ваше число больше")
