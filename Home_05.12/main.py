import random
# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


# text = 'Александр Пушкин начал писать свои первые произведения уже в семь лет. В годы учебы в Лицее он прославился, когда прочитал свое стихотворение Гавриилу Державину. Пушкин первым из русских писателей начал зарабатывать литературным трудом. Он создавал не только лирические стихи, но и сказки, историческую прозу и произведения в поддержку революционеров — за вольнодумство поэта даже отправляли в ссылки.'
# some_list = text.split()
# result_list = list(filter(lambda x : not 'а' in x  and not 'б' in x and  not 'в' in  x  ,some_list))
# print(result_list)

# ------------------------------------------------------------------------------
# Создайте программу для игры в ""Крестики-нолики"".

# step_list = ['', '', '', '', '', '', '', '', '']


# def print_place(coordination: list):
#     print(f'{step_list[0]}\t', '|\t',
#           f'{step_list[1]}\t', '|\t',
#           f'{step_list[2]}\t')
#     print('_\t', '|\t', '_\t', '|\t', '_\t')
#     print(f'{step_list[3]}\t', '|\t',
#           f'{step_list[4]}\t', '|\t',
#           f'{step_list[5]}\t')
#     print('_\t', '|\t', '_\t', '|\t', '_\t')
#     print(f'{step_list[6]}\t', '|\t',
#           f'{step_list[7]}\t', '|\t',
#           f'{step_list[8]}\t')


# def check_step(coordination: list, index):

#     if coordination[index] == '':
#         return True
#     else:
#         return False

# def check_win(winlist : list):
#         if winlist[0] + winlist[1] + winlist[2] == 'XXX' or winlist[0] + winlist[1] + winlist[2] == '000':
#             print(f'{winlist[0]} - победитель !')
#             return True
#         elif winlist[3] + winlist[4] + winlist[5] == 'XXX' or winlist[3] + winlist[4] + winlist[5] == '000':
#             print(f'{winlist[4]} - победитель !')
#             return True
#         elif winlist[6] + winlist[7] + winlist[8] == 'XXX' or winlist[6] + winlist[7] + winlist[8] == '000':
#             print(f'{winlist[7]} - победитель !')
#             return True
#         elif winlist[0] + winlist[4] + winlist[8] == 'XXX' or winlist[0] + winlist[4] + winlist[8] == '000':
#             print(f'{winlist[0]} - победитель !')
#             return True
#         elif winlist[2] + winlist[4] + winlist[6] == 'XXX' or winlist[2] + winlist[4] + winlist[6] == '000':
#             print(f'{winlist[2]} - победитель !')
#             return True
#         elif winlist[0] + winlist[3] + winlist[6] == 'XXX' or winlist[0] + winlist[3] + winlist[6] == '000':
#             print(f'{winlist[0]} - победитель !')
#             return True
#         elif winlist[1] + winlist[4] + winlist[7] == 'XXX' or winlist[1] + winlist[4] + winlist[7] == '000':
#             print(f'{winlist[1]} - победитель !')
#             return True
#         elif winlist[2] + winlist[5] + winlist[8] == 'XXX' or winlist[2] + winlist[5] + winlist[8] == '000':
#             print(f'{winlist[2]} - победитель !')
#             return True
#         else :
#             return False


# def start_game(mode):
#     if mode == 1:
#         print('Игра 1х1')
#         steps = 1
#         while steps < 10:
#             if check_win(step_list):
#                 break
#             else:
#                 try:
#                     index = int(input('Введите позицию от 1-9: ')) + -1
#                     if index == 51:
#                         break
#                     if check_step(step_list, index):
#                         if steps%2 == 0:
#                             step_list[index] = 'X'
#                         else:
#                             step_list[index] = '0'
#                         print_place(step_list)
#                     else:
#                         print('Позиция занята попробуй заного')
#                         steps -=1
#                     if steps == 9 : print("Draw!")
#                     steps +=1
#                     print(step_list)
#                 except:
#                     print("чтото поломалось")
#                     break
#     elif mode == 2:
#         print('Игра 1 Vs CPU')
#         steps = 1
#         whostrt = int(input('Кто начинает первый введите 1 или 2 - где 1 вы стартуете первый: '))
#         while steps < 10:
#             if check_win(step_list):
#                 break
#             else:
#                 try:
#                     # if whostrt == 1 :
#                     if steps % 2 != 0:
#                             index = int(input('Введите позицию от 1-9: ')) + -1
#                             symbPlayer1 = 'X'
#                             if check_step (step_list,index):
#                                 step_list[index] = symbPlayer1
#                                 # print_place(step_list)
#                             else:
#                                 print('Позиция занята попробуй заного')
#                                 steps -=1
#                     else :
#                             # bot = CPU_player()
#                             print(steps, " steps")
#                             symbPlayer2 = '0'
#                             bot = CPU_check_next_step(step_list,steps,symbPlayer2)

#                             print(bot,  " bot")
#                             # if (check_step(step_list,bot)):
#                             if (check_step(step_list,bot)):
#                                 step_list[bot] = symbPlayer2
#                                 # print_place(step_list)
#                             else :
#                                 print('Позиция занята БОТ СЛЕПОЙ')
#                                 steps -=1
#                             print_place(step_list)
#                     if steps == 9 : print("Draw!")
#                     steps +=1
#                 except:
#                     print("чтото поломалось")
#                     break
# def CPU_player():


#     bot_step = random.randint(0,8)
#     return  bot_step

# def CPU_check_next_step(check_steps : list,step,symbol):
#         if step == 2 :
#             return 4
#         if step == 1:
#             return 4

#         if step > 1:
#             if check_steps[0] + check_steps[1] == 'XX' and check_steps[2] != symbol:
#                 return 2
#             elif check_steps[1] + check_steps[2] == 'XX' and check_steps[0] != symbol:
#                 return 0
#             elif check_steps[0] + check_steps[2] == 'XX' and check_steps[1] != symbol:
#                 return 1
#             elif check_steps[0] + check_steps[3] == 'XX' and check_steps[6] != symbol:
#                 return 6
#             elif check_steps[3] + check_steps[6] == 'XX' and check_steps[0] != symbol:
#                 return 0
#             elif check_steps[0] + check_steps[6] == 'XX' and check_steps[3] != symbol:
#                 return 3
#             elif check_steps[1] + check_steps[4] == 'XX' and check_steps[7] != symbol:
#                 return 7
#             elif check_steps[1] + check_steps[7] == 'XX' and check_steps[4] != symbol:
#                 return 4
#             elif check_steps[4] + check_steps[7] == 'XX' and check_steps[1] != symbol:
#                 return 1
#             elif check_steps[2] + check_steps[5] == 'XX' and check_steps[8] != symbol:
#                 return 8
#             elif check_steps[5] + check_steps[8] == 'XX' and check_steps[2] != symbol:
#                 return 2
#             elif check_steps[2] + check_steps[8] == 'XX' and check_steps[5] != symbol:
#                 return 5
#             elif check_steps[2] + check_steps[4] == 'XX' and check_steps[6] != symbol:
#                 return 6
#             elif check_steps[2] + check_steps[6] == 'XX' and check_steps[4] != symbol:
#                 return 4
#             elif check_steps[4] + check_steps[6] == 'XX' and check_steps[2] != symbol:
#                 return 2
#             elif check_steps[0] + check_steps[4] == 'XX' and check_steps[8] != symbol:
#                 return 8
#             elif check_steps[4] + check_steps[8] == 'XX' and check_steps[0] != symbol:
#                 return 0
#             elif check_steps[0] + check_steps[8] == 'XX' and check_steps[4] != symbol:
#                 return 4
#             else : return random.randint(0,8)
#         else:
#             return random.randint(0,8)
# start_game(2)

# ------------------------------------------------------------------------------

# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#    Входные и выходные данные хранятся в отдельных текстовых файлах.
def is_a_num(value):
    try:
        if int(value):
            return True
    except:
            return False

def read_file(path, type_read):
    result_str = ''
    with open(path, type_read, encoding='UTF-8') as inputdate:
        date = inputdate.read()
        for i in date:
            result_str +=i
    return result_str


def to_RLE(str_set:str):
    print(str_set)
    result_str = ''
    count = 1 
    for i in range(1,len(str_set)):
        if  str_set[i-1] == str_set[i]:
            count +=1
        else:
            if count == 1:
                result_str += str_set[i-1]
            else:
                result_str += str(count) + str_set[i-1]
            count=1 
        if i == len(str_set)-1:
            result_str += str(count) + str_set[i-1]
    return result_str
   
def to_String(path,str_value):    
        result_str = ''
        count = 0
        for i in  range(len(str_value)):
            if is_a_num(str_value[i]):
                count = int(str_value[i])
            else :
                if count != 0:
                    result_str += str_value[i] * count
                    count = 0
                else :
                    result_str += str_value[i]
        with open(path,'w', encoding='UTF-8') as str_value:
            str_value.write(result_str)       
            


print(to_RLE(read_file('input.txt', 'r')))
to_String('output.txt',to_RLE(read_file('input.txt', 'r')))