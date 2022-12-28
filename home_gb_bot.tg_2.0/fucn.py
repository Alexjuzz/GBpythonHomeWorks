import requests 
import json
from random import choice as ch


def get_answer_yes_or_no(input_text):
    
    r = requests.get(f'https://yesno.wtf/api?force={input_text}').text
    di = r.replace("{","").replace("}","").replace('":', ': ').replace('":"','": "').replace('"','').split(',')
    di2  = dict([i.split(': ') for i in di])
    return di2['image']


'''''Использование API: http://numbersapi.com/<number>/<type>, где number — число, 
а type — тип факта (trivia — факт из жизни, math — математический факт, date и year 
— вопрос про дату (в формате MM/DD) и год). Например, получить факт о 25 октября можно по
запросу http://numbersapi.com/10/25/date: October 25th is the day in 1760 that George III becomes King of Great Britain.'''


def get_numb_API(numb_math_or_month = None,type_val = None, day_val = None,random_val = None):
    try:
        if random_val == 'random':                                                                      # Вызов рандомной функции
            r = requests.get(f'http://numbersapi.com/{random_val}/{type_val}').text 


        if day_val != None and numb_math_or_month != None and type_val == 'date':                     # Вызов по дню месяцу - дата
            r = requests.get(f'http://numbersapi.com/{numb_math_or_month}/{day_val}/{type_val}').text
        if numb_math_or_month != None and type_val == 'math':
            r = requests.get(f'http://numbersapi.com/{numb_math_or_month}/{type_val}').text
        
        if type_val == 'trivia' and numb_math_or_month != None:    
            r = requests.get(f'http://numbersapi.com/{numb_math_or_month}/{type_val}').text

        return r
    except ValueError:
            print("Ou. Try again")
     
# print(get_numb_API(2,'date',5))
# print(get_numb_API(5,'math'))
# print(get_numb_API(5,'trivia'))
