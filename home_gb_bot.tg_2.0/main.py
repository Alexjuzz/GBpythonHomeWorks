
import telebot as t
import fucn as f
from random import choice as ch


def read_ini():
    with open('D:\\GBPython\\GBpythonHomeWorks\\GBpythonHomeWorks\\home_gb_bot.tg_2.0\\token.ini','r', encoding='utf-8') as file:
        bot = file.read()
        return bot
bot = t.TeleBot(read_ini())
@bot.message_handler(commands=['start'])
def button(message):
    markup = t.types.ReplyKeyboardMarkup(resize_keyboard=True)
    it = t.types.KeyboardButton('Получить гиф это сюда')
    it2 = t.types.KeyboardButton('Получить факт о числах')
    markup.add(it,it2)
    bot.send_message(message.chat.id,"hi",reply_markup=markup)

   


@bot.message_handler(content_types=['text'])
def takes(message):
    print(message.text)
    if message.text == 'Получить гиф это сюда':
        markup = t.types.InlineKeyboardMarkup(row_width=2)
        it1 = t.types.InlineKeyboardButton('GIF - да',callback_data='yes')
        it2 = t.types.InlineKeyboardButton('GIF - не',callback_data='no')
        markup.add(it1,it2)
        bot.send_message(message.chat.id,"Какую хочешь получить ? да или нет",reply_markup=markup)
    elif message.text == 'Получить факт о числах':
        markup = t.types.InlineKeyboardMarkup(row_width=2)
        it1 = t.types.InlineKeyboardButton('Метематический факт',callback_data='1')
        it2 = t.types.InlineKeyboardButton('Факт по дате',callback_data='2')
        it3 = t.types.InlineKeyboardButton('Факт из жизни',callback_data='3')
        it4 = t.types.InlineKeyboardButton('Случайный факт',callback_data='4')
        markup.add(it1,it2,it3,it4)
        bot.send_message(message.chat.id,"Выбери категорию",reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def send_fact(call):
    if call.data == '1':
        mesg = bot.send_message(call.message.chat.id,'Введи число о котором хочещь узнать факт')
        par = 'math'
        bot.register_next_step_handler(mesg,sen_category,par)
     
    if call.data == '2':
        mesg = bot.send_message(call.message.chat.id,'Введи меняц и день через пробел о котором хочещь узнать факт')
        par = 'date'
        bot.register_next_step_handler(mesg,sen_category,par)

    if call.data == '3':
        mesg = bot.send_message(call.message.chat.id,'Введи число чтобы получить факт из жизни')
        par = 'trivia'
        bot.register_next_step_handler(mesg,sen_category,par)
    if call.data == '4':
        bot.send_message(call.message.chat.id,f.get_numb_API(None,random_val(),None,'random'))
    if call.data == 'yes':
        bot.send_animation(call.message.chat.id,animation=f.get_answer_yes_or_no(call.data))
    elif call.data == 'no':
        bot.send_animation(call.message.chat.id,animation=f.get_answer_yes_or_no(call.data))


def random_val():
     return ch(['math','trivia','date'])
   

def  sen_category(message,par):
    try:
        if par == 'math':
            bot.send_message(message.chat.id,f.get_numb_API(message.text,par))        
        if par == 'date':
            mess = message.text.split()
           
            bot.send_message(message.chat.id,f.get_numb_API(mess[0],par,mess[1]))
        if par == 'trivia':
               bot.send_message(message.chat.id,f.get_numb_API(message.text,par))
    except Exception:
        bot.send_message(message.chat.id,"чтото пошло не так")




bot.infinity_polling()

