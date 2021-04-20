"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква

ссылка на графический алгоритм:
https://drive.google.com/file/d/1hSbGUmMIjkmNi09qeQk0sfDN0ocTQKyj/view?usp=sharing
"""
a = int(input("Введите порядковый номер буквы в алфавите: "))
a = 96 + a
print(chr(a))
