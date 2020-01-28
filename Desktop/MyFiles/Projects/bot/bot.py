import credentials as credentials
import telebot
import config
import random

from telebot import types


bot = telebot.TeleBot(config.token)

markup = types.ReplyKeyboardMarkup(resize_keyboard = True)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('C:/Users/Виктор/Desktop/MyFiles/stickers/zelenskiy.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Твой балл на ЗНО по укр.мове 😏')
    item2 = types.KeyboardButton('Как дела, Никита-бот? 😂')
    item3 = types.KeyboardButton('Instagram создателя ⚡')
    item4 = types.KeyboardButton('Пока ✋')
    item5 = types.KeyboardButton('В смысле?')
    markup.add(item1,item2, item3, item4, item5)

    bot.send_message(message.chat.id, 'Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный ради хайпа (by Nikita Silakov)'.format(message.from_user, bot.get_me()),
                     parse_mode = 'html', reply_markup=markup)
    bot.send_message(message.chat.id, 'Привет, хохлыш, дай сало на хлебчик 🍞'.format(message.from_user, bot.get_me()),
                     parse_mode = 'html')
    bot.send_message(message.chat.id, 'Ладно, жадюга, не надо 😢. Выбери лучше что-то на клавиатуре ⬇'.format(message.from_user, bot.get_me()),
                     parse_mode='html')


@bot.message_handler(content_types = ['text'])
def keyboard(message):
    if message.chat.type == 'private':
        if message.text == 'Твой балл на ЗНО по укр.мове 😏':
            bot.send_message(message.chat.id, str(random.randint(100,200)))
        elif message.text == 'Как дела, Никита-бот? 😂':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        elif message.text == 'Instagram создателя ⚡':
            bot.send_message(message.chat.id, '@silakov_228')
        elif message.text == 'Пока ✋':
            bot.send_message(message.chat.id, 'До новых встреч, мой дорогой друг! И помни, я Силан 😏')
        elif message.text == 'В смысле?':
            bot.send_message(message.chat.id, 'В СМЫСЛЕ?')
        else:
            bot.send_message(message.chat.id, 'Я только учу человеческий язык, пока не понимаю это 😢')

    @bot.callback_query_handler(func=lambda call: True)
    def callback_inline(call):
        try:
            if call.message:
                if call.data == 'good':
                    bot.send_message(call.message.chat.id, 'Это хорошо 😊')
                elif call.data == 'bad':
                    bot.send_message(call.message.chat.id, 'Бывает, съешь сальца 😢')

                # remove inline buttons
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="😊 Как дела?",
                                      reply_markup=None)

        except Exception as e:
            print(repr(e))




bot.polling(none_stop = True)
