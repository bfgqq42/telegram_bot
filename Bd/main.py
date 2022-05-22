import telebot
from telebot import TeleBot, types

from Bd.registration import Register

token = '5311880278:AAHyAHNG3feWC-aQuj_N5zSOAeU-qOQIfRI'
bot: TeleBot = telebot.TeleBot(token)


def issued(reason, text):
    print(f"> Issued {reason} for \'{text}\'" if text else "Command is None")


def create_button(folder, text):
    """
    Function gives button with custom callback.

    :return: InlineKeyboardButton
    """
    return types.InlineKeyboardButton(text=text, callback_data=f'{folder}-ask_{text}')


def create_button_array(folder, num):
    """
    Function gives button array with custom callback for each button.

    :return: list of InlineKeyboardButton
    """
    return [create_button(folder, i+1) for i in range(num)]


def fill_keyboard(buttons, width):
    """
    Function gives an inline keyboard consisting of buttons with line_num row size.

    :return: InlineKeyboardMarkup - consist of buttons, [line_num] row size
    """
    return types.InlineKeyboardMarkup(row_width=width).add(*buttons)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if 'ask' in call.data:
        folder, file = call.data.split('-')
        with open(f'data/{folder}/{file}.txt', 'r', encoding='utf-8') as f:
            bot.send_message(call.message.chat.id, f.read())
        issued("callback", call.data)


@bot.message_handler(content_types=['text'])
def start(message):
    user = message.from_user.id
    text = message.text
    issued("command", message.text)

    if text in ['/help', 'Здравствуй', 'Здарова', 'Добрый день']:
        bot.send_message(user, 'Выбери одно из интересующих тебя направлений: \n'
                               '1. Бакалавр - /bachelor\n'
                               '2. Магистратура - /magistracy\n'
                               '3. Доп. информация - /aux_info')

    elif text == '/bachelor':
        buttons = create_button_array('bach', 11)
        keyboard = fill_keyboard(buttons, 3)
        bot.send_message(user, 'Нажми кнопку с цифрой интересующего тебя вопроса:\n\n'
                               '1. Какой срок обучения?\n'
                               '2. Какая стоимость обучения?\n'
                               '3. Есть ли бюджетные места?\n'
                               '4. Какие вступительные экзамены необходимы для поступления?\n'
                               '5. Какие документы необходимо подать в вуз?\n'
                               '6. Какие экзамены нужны для поступления на ЦифрЭк?\n'
                               '7. -\n'
                               '8. Предоставляется ли общежитие?\n'
                               '9. Какой проходной бал при поступлении?\n'
                               '10. Как и когда можно заключить договор?\n'
                               '11. Есть ли военная кафедра и как на нее поступить?\n\n'
                         'Eсли хочешь оставить заявку чтобы тебе перезвонили по данному вопросу напиши /reg_bach\n',
                         reply_markup=keyboard)

    elif text == '/magistracy':
        buttons = create_button_array('magi', 10)
        keyboard = fill_keyboard(buttons, 3)
        bot.send_message(user, 'Нажми кнопку с цифрой интересующего тебя вопроса:\n\n'
                               '1. Какой срок обучения?\n'
                               '2. Какая стоимость обучения?\n'
                               '3. Есть ли бюджетные места?\n'
                               '4. Военная кафедра\n'
                               '5. Проходной бал при поступлении\n'
                               '6. Какие экзамены?\n'
                               '7. Общежитие'
                               '8. Подробнее о программе\n'
                               '9. Как и когда можно заключить договор?\n'
                               '10. Другое. Напиши свой вопрос\n\n'
            
                         'Eсли хочешь оставить заявку чтобы тебе перезвонили по данному вопросу напиши /reg_magi\n',
                         reply_markup=keyboard)

    elif text == '/aux_info':
        buttons = create_button_array('aux', 10)
        keyboard = fill_keyboard(buttons, 3)
        bot.send_message(user, 'Нажми кнопку с цифрой интересующего тебя вопроса:\n\n'
                               '1. International course "Digital economy & AgriFoodTech" Bachelor’s Degree '
                               '(на английском языке)\n'
                               '2. Дополнительное образование Цифровая Экономика в АПК (252 часа)\n'
                               '3. MBA Executive\n'
                               '4. Startup-студия. Центр инновационного предпринимательства.\n'
                               '5. Консалтинг, индивидуальные консультации\n'
                               '6. Хочу стать партнёром ЦифрЭк\n'
                               '7. Контакты'
                               '8. Попасть на сайт ЦифрЭк\n'
                               '9. Как добраться в ЦифрЭк\n'
                               '10. Другое. Задать свой вопрос.\n\n'

                               'Eсли хочешь оставить заявку чтобы тебе перезвонили по данному вопросу напиши /reg_aux\n',
                         reply_markup=keyboard)

    elif '/reg' in text and len(text) > 5:
        dbname = text.split('_')[1]
        if dbname in ['bach', 'magi', 'aux']:
            Register(bot, message, dbname)

    else:
        bot.send_message(user, 'Простите, я вас не понимаю. Напишите /help')


if __name__ == '__main__':
    try:
        print('> Bot started successfully!')
        bot.polling()
    except Exception as e:
        print(f'> Exception caught "{e}"')
