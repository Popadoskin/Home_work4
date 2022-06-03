# Создать и заполнить файл случайными целыми значениями.
# Выполнить сортировку содержимого файла по возрастанию.

import random
i = 0
lst = []
while i < 10:
    number = random.randint(0, 100)
    lst = lst + [number]
    i = i+1
print("lst = ", lst)

lst_sort = sorted(lst)
print("lst_sort = ", lst_sort)


def write_sort_lst(lst_sort):
    file = open('file.txt', 'wt')
    for i in lst_sort:
        s = str(i)
        file.write(s + ' ')
    file.close()
write_sort_lst(lst_sort)