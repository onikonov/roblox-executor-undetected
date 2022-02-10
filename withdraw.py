from SimpleQIWI import *
import telebot;
bot = telebot.TeleBot('5164566241:AAFMd0O_A1hARCuiTiwS2DL40Kw_kWf0s6Q');
def get_text_messages(message):
bot.polling(none_stop=True, interval=0)

name = '';
surname = '';
age = 0;

def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Введи Token:");
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg');
        
        def get_name(message): #получаем token
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Qiwi token: ');
    bot.register_next_step_handler(message, get_surnme);

def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message('Твой Киви с +7');
    bot.register_next_step_handler(message, get_age);


api = QApi(token=get_name,phone=get_surname)
(bot.send_message(message.from_user.id, api.balance))

summ = input('Введите сумму: ')
price = api.balance
api.pay(account= surname, amount=int(summ))

