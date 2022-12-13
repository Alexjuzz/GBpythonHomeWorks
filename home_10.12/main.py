# Задача 2
# Напишите функцию same_by(characteristic, objects),
# которая проверяет, все ли объекты имеют одинаковые значения некоторой
# характеристики, и возвращает True, если это так. Если значение характеристики
# для разных объектов отличается - то False. Для пустого набора объектов,
# функция должна возвращать True. Аргумент characteristic - это функция,
# которая принимает объект и вычисляет его характеристику.
# Пример:
# ввод: values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#   print("same")
# else:
#   print("different")
#   вывод: same
# Пример 2:
# ввод: values = [1, 2, 3, 4]
# if same_by(lambda x: x % 2, values):
#   print("same")
# else:
#   print("different")
#   вывод: different

# values = [0, 3, 10, 6]

# def same_by(func, val):
#     k = map(func, val)
#     return 1 not in k and val


# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')
# ___________________________________________________________________________________________________________________________________


# Дан список интов,повторяющихся элементов в списке нет.
# Нужно преобразовать этомножество в строку,сворачивая соседние по числовому ряду числа в диапазоны.
#  Примеры:[1,4,5,2,3,9,8,11,0] => "0-5,8-9,11" [1,4,3,2] => "1-4"[1,4] => "1,4"

# a = sorted(set([1,4,2,5,3,9,8,11,0,13,14,15]))
# print(a)
# count = 0
# [0, 1, 2, 3, 4, 5, 8, 9, 11, 14]
# for i in range(1,len(a)):
#     if a[i] == a[i-1]+1:
#         count +=1
#     else:
#         if count == 0:
#             print(f'({a[i-1]})', end='')
#         else:
#             print(f'({a[(i-1)-count]}-{a[i-1]})', end='')
#             count = 0
#     if i == len(a)-1:
#         if count == 0:
#             print(f'({a[i]})', end='')
#         else:
#             print(f'({a[i-count]}-{a[i]})')

# ___________________________________________________________________________________________________________________________________
# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение[1, 2, 2, 3] (порядок не важен)

# Первый вариант:
# def set_interseption(list_a, list_b):
    # list_c = []
    # for i in list_b:
    #     if i in list_a:
    #         list_c.append(i)
    # return sorted(list_c)   
# print(set_interseption([1, 2, 3, 2, 0],[5, 1, 2, 7, 3, 2]))

# Второй вариант:
# def set_interseption(list_a, list_b):
#     return sorted([i for i in list_a if i in list_b])
# print(set_interseption([1, 2, 3, 2, 0],[5, 1, 2, 7, 3, 2]))


# Третий вариант:
# def intersection_list(list1, list2): 
#    list3 = [list(filter(lambda x: x in list1, list2))] 
#    return list3 
# list1 = [10, 9, 17, 40, 23, 18, 56, 49, 58, 60] 
# list2 = [25, 17, 23, 40, 32, 1, 10, 13, 27, 28, 60, 55, 61, 78, 15, 76]
# print(intersection_list(list1, list2))
