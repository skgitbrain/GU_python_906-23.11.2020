import random

size = 10
start = -100
end = 99
array = [random.randint(start, end) for i in range(size)]

print(array)


# добавлен метод, который проверяет менялся элемент местами или нет в списке.
def sort_bubble(array):
    n = True
    while n:
        n = False
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                print(array)
                n = True
    return array


print(sort_bubble(array))
