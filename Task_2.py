# Дан список чисел. Создать список в который попадают числа,
# описывающие возрастающую последовательность и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]


list = [1, 5, 2, 3, 4, 6, 1, 7]
list2 = []
for i in list:
  if i not in list2:
    list2.append(i)
print(list2)



new_list = []
k = list2[0]
i = 0
for i in list2:
    if i == k:
        new_list = new_list + [i]
        k = i + 1
    elif k < i < (list[i+1]):
        new_list = new_list + [i]
        k = i + 1
    i = i + 1
print(new_list)




