import telebot

from lib import *
from data.json_work import read
from Bd.registration import Register


# bot configuration
token = '5311880278:AAHyAHNG3feWC-aQuj_N5zSOAeU-qOQIfRI'
bot: telebot.TeleBot = telebot.TeleBot(token)


# keyboards
help_keyboard = types.ReplyKeyboardMarkup(row_width=1).add(*[
    create_button('Бакалавриат', 'basic-bach'),
    create_button('Магистратура', 'basic-magi'),
    create_button('Доп. информация', 'basic-auxi')
])

bach_keyboard = types.InlineKeyboardMarkup(row_width=1).add(*[
    create_button('1. Какой срок обучения?', 'bach-ask_1'),
    create_button('2. Какая стоимость обучения?', 'bach-ask_2'),
    create_button('3. Есть ли бюджетные места?', 'bach-ask_3'),
    create_button('4. Какие вступительные экзамены необходимы для поступления?', 'bach-ask_4'),
    create_button('5. Какие документы необходимо подать в вуз?', 'bach-ask_5'),
    create_button('6. Какие экзамены нужны для поступления на ЦифрЭк?', 'bach-ask_6'),
    create_button('7. Предоставляется ли общежитие?', 'bach-ask_7'),
    create_button('8. Какой проходной бал при поступлении?', 'bach-ask_8'),
    create_button('9. Как и когда можно заключить договор?', 'bach-ask_9'),
    create_button('10. Есть ли военная кафедра и как на нее поступить?', 'bach-ask_10'),
    # create_button('Вернуться назад', 'return-menu')
])

magi_keyboard = types.InlineKeyboardMarkup(row_width=1).add(*[
    create_button('1. Какой срок обучения?', 'magi-ask_1'),
    create_button('2. Какая стоимость обучения?', 'magi-ask_2'),
    create_button('3. Есть ли бюджетные места?', 'magi-ask_3'),
    create_button('4. Есть ли военная кафедра?', 'magi-ask_4'),
    create_button('5. Какой проходной бал при поступлении', 'magi-ask_5'),
    create_button('6. Какие экзамены необходимы для сдачи?', 'magi-ask_6'),
    create_button('7. Предоставляется ли общежитие?', 'magi-ask_7'),
    create_button('8. Подробнее о программе', 'magi-ask_8'),
    create_button('9. Как и когда можно заключить договор?', 'magi-ask_9'),
    create_button('10. Другое. Напиши свой вопрос', 'magi-ask_10'),
    # create_button('Вернуться назад', 'return-menu')
])

auxi_keyboard = types.InlineKeyboardMarkup(row_width=1).add(*[
    create_button('1. International course (на английском языке)', 'auxi-ask_1'),
    create_button('2. ДПО ЦифрЭк в АПК (252 часа)', 'auxi-ask_2'),
    create_button('3. MBA Executive', 'auxi-ask_3'),
    create_button('4. Startup-студия', 'auxi-ask_4'),
    create_button('5. Консалтинг', 'auxi-ask_5'),
    create_button('6. Хочу стать партнёром ЦифрЭк', 'auxi-ask_6'),
    create_button('7. Контакты', 'auxi-ask_7'),
    create_button('8. Попасть на сайт ЦифрЭк', 'auxi-ask_8'),
    create_button('9. Как добраться в ЦифрЭк', 'auxi-ask_9'),
    create_button('10. Другое. Задать свой вопрос.', 'auxi-ask_10'),
    # create_button('Вернуться назад', 'return-menu')
])


spec_keyboard = {'bach': bach_keyboard, 'magi': magi_keyboard, 'auxi': auxi_keyboard}
answers = {'bach': read('bach'), 'magi': read('magi'), 'auxi': read('auxi')}

# shortcut texts
main_text = 'Нажми кнопку с цифрой интересующего тебя вопроса:\n' \
            'Eсли хочешь оставить заявку чтобы тебе перезвонили по данному вопросу напиши'
shortcut = {
    'Бакалавриат': 'bach',
    'Магистратура': 'magi',
    'Доп. информация': 'auxi'
}

shortcut_rev = {
    'bach': 'Бакалавриат',
    'magi': 'Магистратура',
    'auxi': 'Доп. информация'
}


@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    issued("callback", call.data)

    if 'ask' in call.data:
        spec, name = call.data.split('-')
        text = ''

        for j in spec_keyboard.values():
            for i in j.keyboard:
                if call.data == i[0].callback_data:
                    text = i[0].text

        bot.send_message(call.message.chat.id, f'<u><i><b>{text}</b></i></u>\n' + answers[spec][name],
                         reply_markup=types.InlineKeyboardMarkup(row_width=1).add(*[
                             create_button('Вернуться назад', f'return-{spec}')
                         ]),
                         parse_mode='HTML')

    elif 'return' in call.data:
        text = call.data.split('-')[1]

        if text in ['bach', 'magi', 'auxi']:
            bot.send_message(call.message.chat.id, f'<u><i><b>{shortcut_rev[text]}</b></i></u>\n' + main_text + f' /reg_{text}\n',
                             reply_markup=spec_keyboard[text], parse_mode='HTML')
        else:
            bot.send_message(call.message.chat.id, 'Простите, я вас не понимаю. Напишите /help')


@bot.message_handler(content_types=['text'])
def start(message):
    user = message.from_user.id
    text = message.text
    issued("command", message.text)

    if text in ['/help', '/start', 'Здравствуй', 'Здарова', 'Добрый день']:
        bot.send_message(user, 'Выбери одно из интересующих тебя направлений', reply_markup=help_keyboard)

    elif text in shortcut.keys():
        name = shortcut[text]
        if name in ['bach', 'magi', 'auxi']:
            bot.send_message(user, f'<u><i><b>{text}</b></i></u>\n' + main_text + f' /reg_{name}\n',
                             reply_markup=spec_keyboard[name], parse_mode='HTML')
        else:
            bot.send_message(user, 'Простите, я вас не понимаю. Напишите /help')

    elif '/reg' in text and len(text) > 5:
        dbname = text.split('_')[1]
        if dbname in ['bach', 'magi', 'auxi']:
            Register(bot, message, dbname)

    else:
        bot.send_message(user, 'Простите, я вас не понимаю. Напишите /help')


if __name__ == '__main__':
    print('> Bot started successfully!')
    bot.polling()
    # try:
    #
    # except Exception as e:
    #     print(f'> Exception caught "{e}"')
