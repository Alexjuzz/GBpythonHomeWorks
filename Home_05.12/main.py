import random
# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


# text = 'Александр Пушкин начал писать свои первые произведения уже в семь лет. В годы учебы в Лицее он прославился, когда прочитал свое стихотворение Гавриилу Державину. Пушкин первым из русских писателей начал зарабатывать литературным трудом. Он создавал не только лирические стихи, но и сказки, историческую прозу и произведения в поддержку революционеров — за вольнодумство поэта даже отправляли в ссылки.'
# some_list = text.split()
# result_list = list(filter(lambda x : not 'а' in x  and not 'б' in x and  not 'в' in  x  ,some_list))
# print(result_list)


# Создайте программу для игры в ""Крестики-нолики"".

step_list = ['', '', '', '', '', '', '', '', '']


def print_place(coordination: list):
    print(f'{step_list[0]}\t', '|\t',
          f'{step_list[1]}\t', '|\t',
          f'{step_list[2]}\t')
    print('_\t', '|\t', '_\t', '|\t', '_\t')
    print(f'{step_list[3]}\t', '|\t',
          f'{step_list[4]}\t', '|\t',
          f'{step_list[5]}\t')
    print('_\t', '|\t', '_\t', '|\t', '_\t')
    print(f'{step_list[6]}\t', '|\t',
          f'{step_list[7]}\t', '|\t',
          f'{step_list[8]}\t')




def check_step(coordination: list, index):

    if coordination[index] == '':
        return True
    else:
        return False

def check_win(winlist : list):
        if winlist[0] + winlist[1] + winlist[2] == 'XXX' or winlist[0] + winlist[1] + winlist[2] == '000':
            print(f'{winlist[0]} - победитель !')
            return True
        elif winlist[3] + winlist[4] + winlist[5] == 'XXX' or winlist[3] + winlist[4] + winlist[5] == '000':
            print(f'{winlist[4]} - победитель !')
            return True
        elif winlist[6] + winlist[7] + winlist[8] == 'XXX' or winlist[6] + winlist[7] + winlist[8] == '000':
            print(f'{winlist[7]} - победитель !')
            return True
        elif winlist[0] + winlist[4] + winlist[8] == 'XXX' or winlist[0] + winlist[4] + winlist[8] == '000':
            print(f'{winlist[4]} - победитель !')
            return True
        elif winlist[2] + winlist[4] + winlist[6] == 'XXX' or winlist[2] + winlist[4] + winlist[6] == '000':
            print(f'{winlist[4]} - победитель !')
            return True
        elif winlist[0] + winlist[3] + winlist[6] == 'XXX' or winlist[0] + winlist[3] + winlist[6] == '000':
            print(f'{winlist[4]} - победитель !')
            return True 
        elif winlist[1] + winlist[4] + winlist[7] == 'XXX' or winlist[1] + winlist[4] + winlist[7] == '000':
            print(f'{winlist[4]} - победитель !')
            return True       
        elif winlist[2] + winlist[5] + winlist[8] == 'XXX' or winlist[2] + winlist[5] + winlist[8] == '000':
            print(f'{winlist[4]} - победитель !')
            return True    
        else :
            return False


def start_game(mode):
    if mode == 1:
        print('Игра 1х1')
        steps = 1
        while steps < 10:
            if check_win(step_list):
                break
            else:
                try:
                    index = int(input('Введите позицию от 1-9: ')) + -1
                    if index == 51:
                        break
                    if check_step(step_list, index):
                        if steps%2 == 0:
                            step_list[index] = 'X'
                        else:
                            step_list[index] = '0'
                        print_place(step_list)    
                    else:
                        print('Позиция занята попробуй заного')
                        steps -=1
                    if steps == 9 : print("Draw!")
                    steps +=1
                    print(step_list)
                except:
                    print("чтото поломалось")
                    break
    elif mode == 2:
        print('Игра 1 Vs CPU')
        steps = 1
        whostrt = int(input('Кто начинает первый введите 1 или 2 - где 1 вы стартуете первый: '))
        while steps < 10:
            if check_win(step_list):
                break
            else:
                try:
                    if whostrt == 1 :
                        if steps % 2 == 0:
                            index = int(input('Введите позицию от 1-9: ')) + -1
                            if check_step (step_list,index):
                                step_list[index] = 'X'
                                print_place(step_list)
                            else:
                                print('Позиция занята попробуй заного')
                                steps -=1
                        else :
                            bot = CPU_player()
                            print(bot)
                            if (check_step(step_list,bot)):
                                step_list[bot] = '0'
                                print_place(step_list)
                            else :
                                print('Позиция занята БОТ СЛЕПОЙ')
                                steps -=1                   
                    if steps == 9 : print("Draw!")
                    steps +=1
                except:
                    print("чтото поломалось")
                    break
def CPU_player():
    bot_step = random.randint(0,8)
    return  bot_step


start_game(2)
        # Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
        # Входные и выходные данные хранятся в отдельных текстовых файлах.
