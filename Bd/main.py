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
    create_button('International course (на английском языке)', 'basic-inter'),
    create_button('ДПО ЦифрЭк в АПК (252 часа)', 'basic-dpo'),
    create_button('MBA Executive', 'basic-mba'),
    create_button('Startup-студия', 'basic-startup'),
    create_button('Консалтинг', 'basic-kasal'),
    create_button('Другое. Задать свой вопрос.', 'basic-drugoe'),
])

bach_keyboard = types.InlineKeyboardMarkup(row_width=1).add(*[
    create_button('1. Какой срок обучения?', 'bach-ask_1'),
    create_button('2. Какая стоимость обучения?', 'bach-ask_2'),
    create_button('3. Есть ли бюджетные места?', 'bach-ask_3'),
    create_button('4. Какие экзамены необходимы для поступления?', 'bach-ask_4'),
    create_button('5. Какие документы необходимо подать в вуз?', 'bach-ask_5'),
    create_button('6. Предоставляется ли общежитие?', 'bach-ask_6'),
    create_button('7. Какой проходной бал при поступлении?', 'bach-ask_7'),
    create_button('8. Как и когда можно заключить договор?', 'bach-ask_8'),
    create_button('9. Есть ли военная кафедра и как на нее поступить?', 'bach-ask_9'),
    # create_button('Вернуться назад', 'return-menu')
])

magi_keyboard = types.InlineKeyboardMarkup(row_width=1).add(*[
    create_button('1. Какой срок обучения?', 'magi-ask_1'),
    create_button('2. Какая стоимость обучения?', 'magi-ask_2'),
    create_button('3. Есть ли бюджетные места?', 'magi-ask_3'),
    create_button('4. Есть ли военная кафедра?', 'magi-ask_4'),
    create_button('5. Какой проходной бал при поступлении?', 'magi-ask_5'),
    create_button('6. Какие экзамены необходимы для сдачи?', 'magi-ask_6'),
    create_button('7. Предоставляется ли общежитие?', 'magi-ask_7'),
    create_button('8. Как и когда можно заключить договор?', 'magi-ask_8'),
    create_button('9. Подробнее о программе', 'magi-ask_9'),
    create_button('10. Другое. Напиши свой вопрос', 'magi-ask_10'),
    # create_button('Вернуться назад', 'return-menu')
])

inter_keyboard = types.InlineKeyboardMarkup(row_width=1).add(*[
    create_button('1. Duration of training', 'inter-ask_1'),
    create_button('2. Tuition fees', 'inter-ask_2'),
    create_button('3. Budget places', 'inter-ask_3'),
    create_button('4. Military Department', 'inter-ask_4'),
    create_button('5. Entrance tests', 'inter-ask_5'),
    create_button('6. Hostel', 'inter-ask_6'),
    create_button('7. More about the program', 'inter-ask_7'),
    create_button('8. How and when to conclude a contract?', 'inter-ask_8'),
    create_button('9. Other. Write your question.', 'inter-ask_9'),
    # create_button('Вернуться назад', 'return-menu')
])

dpo_keyboard = types.InlineKeyboardMarkup(row_width=1).add(*[
    create_button('1. Срок обучения?', 'dpo-ask_1'),
    create_button('2. Блоки преподаваемых дисциплин', 'dpo-ask_2'),
    create_button('3. Стоимость обучения', 'dpo-ask_3'),
    create_button('4. Подробнее о программе. Ригистрация', 'dpo-ask_4'),
    # create_button('Вернуться назад', 'return-menu')
])

mba_keyboard = types.InlineKeyboardMarkup(row_width=1).add(*[
    create_button('1. Программа для продвинутых', 'mba-ask_1'),
    # create_button('Вернуться назад', 'return-menu')
])

startup_keyboard = types.InlineKeyboardMarkup(row_width=1).add(*[
    create_button('1. Преврати свою идею в прибыльный бизнес!', 'startup-ask_1'),
    create_button('2. Подробнее. Регистрация', 'startup-ask_2'),
    # create_button('Вернуться назад', 'return-menu')
])

kasal_keyboard = types.InlineKeyboardMarkup(row_width=1).add(*[
    create_button('1. ЦифрЭк КубГАУ кроме образования предоставляет консалтинговые услуги?', 'kasal-ask_1'),
    create_button('2. Оставьте контакты, мы обязательно с вами свяжемся', 'kasal-ask_2'),
    # create_button('Вернуться назад', 'return-menu')
])

drugoe_keyboard = types.InlineKeyboardMarkup(row_width=1).add(*[
    create_button('1. Наш сайт', 'drugoe-ask_1'),
    create_button('2. Как добраться в ЦифрЭк?', 'drugoe-ask_2'),
    create_button('3. Хочу стать партнёром ЦифрЭк', 'drugoe-ask_3'),
    create_button('4. Наши контакы', 'drugoe-ask_4'),

    # create_button('Вернуться назад', 'return-menu')
])

spec_keyboard = {'bach': bach_keyboard, 'magi': magi_keyboard, 'inter': inter_keyboard, 'dpo': dpo_keyboard, 'mba': mba_keyboard, 'startup': startup_keyboard, 'kasal': kasal_keyboard, 'drugoe': drugoe_keyboard}
answers = {'bach': read('bach'), 'magi': read('magi'), 'inter': read('inter'),  'dpo': read('dpo'),  'mba': read('mba'),  'startup': read('startup'),  'kasal': read('kasal'), 'drugoe': read('drugoe')}

# shortcut texts
main_text = 'Нажми кнопку с цифрой интересующего тебя вопроса:\n' \
            'Eсли хочешь оставить заявку чтобы тебе перезвонили по данному вопросу напиши'
shortcut = {
    'Бакалавриат': 'bach',
    'Магистратура': 'magi',
    'International course (на английском языке)': 'inter',
    'ДПО ЦифрЭк в АПК (252 часа)': 'dpo',
    'MBA Executive': 'mba',
    'Startup-студия': 'startup',
    'Консалтинг': 'kasal',
    'Хочу стать партнёром ЦифрЭк': 'popas',
    'Как добраться в ЦифрЭк': 'dobav',
    'Другое. Задать свой вопрос.': 'drugoe',
}

shortcut_rev = {
    'bach': 'Бакалавриат',
    'magi': 'Магистратура',
    'inter': 'International course (на английском языке)',
    'dpo': 'ДПО ЦифрЭк в АПК (252 часа)',
    'mba': 'MBA Executive',
    'startup': 'Startup-студия',
    'kasal': 'Консалтинг',
    'popas': 'Хочу стать партнёром ЦифрЭк',
    'dobav': 'Как добраться в ЦифрЭк',
    'drugoe': 'Другое. Задать свой вопрос.',
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

        if text in ['bach', 'magi', 'inter', 'startup', 'dpo', 'mba', 'kasal', 'drugoe']:
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
        if name in ['bach', 'magi', 'inter', 'dpo', 'mba', 'startup', 'kasal', 'popas', 'dobav', 'drugoe']:
            bot.send_message(user, f'<u><i><b>{text}</b></i></u>\n' + main_text + f' /reg_{name}\n',
                             reply_markup=spec_keyboard[name], parse_mode='HTML')
        else:
            bot.send_message(user, 'Простите, я вас не понимаю. Напишите /help')

    elif '/reg' in text and len(text) > 5:
        dbname = text.split('_')[1]
        if dbname in ['bach', 'magi', 'inter', 'dpo', 'mba', 'startup', 'kasal', 'popas', 'dobav', 'drugoe']:
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
