import random as r
# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

                                             # Математический метод 
# def summValues():
#     a = float(input())
#     while a % 1 != 0:
#         a = round(a * 10,6)
#     b = a
#     result = 0
#     while b != 0:
#         result += b % 10
#         b//=10
#     return int(result)
# print(summValues())    


#                                                 # Метод через строку
# def sumValuesStr():
#     someVal = input().replace(',','').replace('.','')
#     result = 0
#     for _ in someVal:
#         result += int(_)
#     return result   
# print(sumValuesStr())

# ___________________________________________________________________________________________________________________________________

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# def multiplyValues():
#     a = int(input())
#     res =1
#     print('[',end = '')
#     for _ in range(1,a):
#         res *= _
#         print(f'{res}, ', end = '')
#     print(f'{res *a}]')
# multiplyValues()

# ___________________________________________________________________________________________________________________________________

# Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


# a = int(input())
# res = 0
# summ = 0
# list =[]
# for i in range(1,a+1):
#         res = (1+(1/i))**i
#         list.append(round(res,2))
#         summ+=round(res,2)
# print(list)
# print(summ)

# # ___________________________________________________________________________________________________________________________________
# Задайте список из N элементов заполненых из промежутка от -N До N найдите произведение 
# элементов на указанных позициях. Позиции ханятся в файле file.txt в одной строке одно число




                                                    # Задаем  список  от -N до N
# list = int(input())
# Resultlist = [i for i in range(-list,list+1)]

#                                                     #  Записываем позиции в файл
# date = open('D:\\GBPython\\GBpythonHomeWorks\\GBpythonHomeWorks\\Home_24.11\\file2.txt','w')
# for _ in range(len(Resultlist)):
#     date.write(f'{_} \n')
# date.close()

#                                                     # Считываем позиции из файла и создаем список с позициями
# date = open('D:\\GBPython\\GBpythonHomeWorks\\GBpythonHomeWorks\\Home_24.11\\file2.txt','r')
# PositioVal = []
# for _ in date:
#        PositioVal.append((int(str(_).replace('\n',''))))

# print((PositioVal))
# print(Resultlist)

#                                                     # Умножаем числа из списка по позициям из файла
# l =  len(Resultlist) - 1
# i = 0
# while i < l:
#         print(f'Число {Resultlist[PositioVal[i]] }  { Resultlist[PositioVal[i+1]]} = {Resultlist[PositioVal[i]] * Resultlist[PositioVal[i+1]]}')
#         i+=2

# # ___________________________________________________________________________________________________________________________________

# Реализуйте алгоритм перемешивания списка

# list = ['eqw','321',123,False,True,2.31,0.0,2,1,3,5,51,6,1,21313,5,'dawadawda']
# print(list)
# lisr = [3,2,3,4,5,6,7,8]
# def randomIndex(y,x):
#     if x == 0:
#         a = r.randint(y,x)
#     a = r.randint(y,x)
#     while x == a:
#         a= r.randint(y,x)
#     return a

# index = len(list)-1
# a = len(list)-1
# while a != 0:
#     e  = randomIndex(0,index)
#     tmp = list[e]
#     list[e] = list[index]
#     list[index] = tmp
#     a-=1
   
# print(list)

