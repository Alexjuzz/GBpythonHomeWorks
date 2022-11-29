import math
# 1.  Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# a =  [2, 3, 5, 9, 3]
# result = 0
# for _ in range(1,len(a),2):
#         result+=a[_]
# print(result)

# ___________________________________________________________________________________________________________________________________

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# # - [2, 3, 4, 5, 6] => [12, 15, 16];
# # - [2, 3, 5, 6] => [12, 15]

# def multarray(x):
#     result = []
#     index = 0

#     for _ in range(int(math.ceil(len(x)/2))):
#         result.append(x[index] * x[len(x)-index-1])
#         index += 1
#     return result


# a = [2, 3, 4, 5, 6]
# print(multarray(a))

# a = [2, 3, 5, 6]
# print(multarray(a))


# ___________________________________________________________________________________________________________________________________

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# def funDeduction(x):
#     result = []
#     for  _ in x:
#         if type(_) != int:
#             result.append(round(_%1,3))

#     result.sort()
#     DeducMinValues = result[len(result)-1] - result[0]

#     return DeducMinValues

# print(funDeduction(a))


# a = [1.1, 1.2, 3.1, 5, 10.11,0.412414, 0.045]


# def stMinMax(x):
#     b = ' '.join(str(x) for x in a).split()
#     c = ''
#     e = ''
   
#     for _ in b:
#         if '.' in _:
#             c += (' ' + _[_.index('.'):len(_)])
#             e = c.split()
   
#     for _ in range(0, len(e)):
#         min = float(e[_])
#         max = float(e[_])
#         for o in range(0, len(e)):
#             if min > float(e[o]):
#                 min = float(e[o])
#             if max < float(e[o]):
#                 max = float(e[o])

#     return max - min
# print(stMinMax(a))

# ___________________________________________________________________________________________________________________________________

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


# def translateAnotherToSystem(number,system):
#     code_list = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
#     s  = ''
#     while number > 0:
#         s += str(code_list[number%system])
#         number//=system
#     return  s[::-1]


# print(translateAnotherToSystem(46,2))