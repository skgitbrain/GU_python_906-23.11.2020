import timeit
import cProfile
"""
def prime_number(number):
    list =[]
    for num in range(2,number*100):
          for i in range(2,num):
              if (num % i) == 0:
                  break
          else:
              list.append(num)
    return list[number-1]

prime_number(5)

print(timeit.timeit('prime_number(5)', number=100, globals=globals()))  # 0.1350275
print(timeit.timeit('prime_number(10)', number=100, globals=globals()))  # 0.5692921999999999
print(timeit.timeit('prime_number(20)', number=100, globals=globals()))  # 2.8501117
print(timeit.timeit('prime_number(30)', number=100, globals=globals()))  # 5.919471699999999
print(timeit.timeit('prime_number(40)', number=100, globals=globals()))  # 11.1550369
print("______________________________")
cProfile.run('prime_number(5)')

#Вывод: данный код плохо работает с большими числами, требуется оптимизация
"""

n = input("5")
a = range(n+1)
a[1] = 0
lst = []

i = 2
while i <= n:
    if a[i] != 0:
        lst.append(a[i])
        for j in range(i, n+1, i):
            a[j] = 0
    i += 1
print(lst)