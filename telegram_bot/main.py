import telebot
from telebot import types
import random

token = '6153252829:AAF6imzT4MTB77OQeEubOCRcvWfwuzojjhA'

bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('Играть')
btn2 = types.KeyboardButton('Нет, я пас')
keyboard.add(btn1, btn2)


@bot.message_handler(commands=['start', 'game'])
def start_message(message):
    bot_message = bot.send_message(message.chat.id, 'Калайсын, Майкл, начнем игру?', reply_markup=keyboard)
    bot.register_next_step_handler(bot_message, check_answer)

def check_answer(message):
    if message.text == 'Играть':
        bot.send_message(message.chat.id, 'Ок, тогда лови правила игры:\Нужео угадать 1-3 из!')
        number = random.randint(1,10)
        print(number)
        game(message, 3, number)
    elif message.text == 'Нет, я пас':
        bot.send_message(message.chat.id, 'Нет, так нет')
    else:
        bot_message = bot.send_message(message.chat.id, 'вы ввели неправильную команду!\n введите новую', reply_markup=keyboard)
        bot.register_next_step_handler(bot_message, check_answer)

def game(message, attempts, number):
    message_bot = bot.send_message(message.chat.id, 'выбери число')
    bot.register_next_step_handler(message_bot, check_number, attempts-1, number)

def check_number(message, attempts, number):
    if message.text == str(number):
        bot.send_message(message.chat.id, 'Вы победили, хорооооош!')
    elif attempts == 0:
        bot.send_message(message.chat.id, 'Ты проиграл')
    else:
        bot.send_message(message.chat.id, 'нет, ты не угадал число, попробуй еще раз')
        game(message, attempts, number)

bot.polling()









