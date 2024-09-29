import telebot
from telebot import types

bot = telebot.TeleBot('#')


@bot.message_handler(commands=['start'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Переходи к нам в сообщество', url='https://vk.com/zoosalonpskov'))

    with open('./Screenshot 2024-09-26 174311.png', 'rb') as file:
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}', reply_markup=markup)
        bot.send_photo(message.chat.id, file)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "/start - Начало \n/help - Команды\n \n/services - Наши услуги")


@bot.message_handler(commands=['services'])
def services(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Для собак', callback_data='Dogs')
    button2 = types.InlineKeyboardButton('Для котов', callback_data='Cats')
    markup.add(button1, button2)

    bot.send_message(message.chat.id, f'{message.from_user.first_name}, вот наши услуги:', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'Dogs':
        bot.send_message(call.message.chat.id, "Вы выбрали услуги для собак.")

        files = ['./1.jpg', './2.jpg', './3.jpg']
        media = []

        for file_path in files:
            media.append(types.InputMediaPhoto(open(file_path, 'rb')))

        bot.send_media_group(call.message.chat.id, media)

    elif call.data == 'Cats':
        bot.send_message(call.message.chat.id, "Вы выбрали услуги для котов.")

        with open('./4.jpg', 'rb') as file:
            bot.send_photo(call.message.chat.id, file)


bot.infinity_polling()
