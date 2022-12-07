import math
import random
# 1. Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# print(round(math.pi,len(input('Введите число в формате "0.01"  : '))-2))


# ------------------------------------------------------------------------------
# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# a = int(input('Введите число: '))
# list_values = []
# for i in range(2,a//2 + 1):
#         if(a%i ==0 )  :
#             list_values.append(i)
#             a//=i
# print(f'Список простых множителей числа {a} -> {list_values}')


# ------------------------------------------------------------------------------

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

sizelist = int(input("Введите размер листа: "))
list_val = [random.randint(0, 10) for _ in range(sizelist)]
print(list_val)
# result_list = []
# for i in range(0,len(list_val)):
#     if list_val.count(list_val[i])== 1:
#         result_list.append(list_val[i])
# print(result_list)



# ------------------------------------------------------------------------------ 2e решение.
# result_val = []
# count = 0
# for i in range(len(list_val)):
#     count =0
#     for x in range(len(list_val)):
#         if list_val[i] == list_val[x]:
#          count+=1
#     print(count)
#     if count  ==1:
#         result_val.append(list_val[i])     
# print(result_val)
