import telebot
from telebot import TeleBot, types
import tablework


token = '5311880278:AAHyAHNG3feWC-aQuj_N5zSOAeU-qOQIfRI'
bot: TeleBot = telebot.TeleBot(token)

name = ''
last_name = ''
age = ''
number = ''


def issued_command(text):
    print(f'Issued command \'{text}\'' if text is not None else 'Command is None')


def create_button(folder, text):
    return types.InlineKeyboardButton(text=text, callback_data=f'{folder}-ask_{text}')


@bot.callback_query_handler(func=lambda call: True)
def test_callback(call):
    folder, file = call.data.split('-')
    print(folder, file)
    with open(f'data/{folder}/{file}.txt', 'r', encoding='utf-8') as f:
        bot.send_message(call.message.chat.id, f.read())

    print(f'Issued callback for {call.data}')


@bot.message_handler(content_types=['text'])
def start(message):
    user = message.from_user.id
    issued_command(message.text)
    if message.text == '/help':
        bot.send_message(user, 'Выбери одно из интересующих тебя направлений /Bakalavriat, /Magistratura, /dop_info')
    elif message.text == 'Шальной прибор':
        bot.send_message(user, 'Выбери одно из интересующих тебя направлений /Bakalavriat, /Magistratura, /dop_info')
    elif message.text == 'Здарова':
        bot.send_message(user, 'Выбери одно из интересующих тебя направлений /Bakalavriat, /Magistratura, /dop_info')
    elif message.text == 'Добрый день':
        bot.send_message(user, 'Выбери одно из интересующих тебя направлений /Bakalavriat, /Magistratura, /dop_info')

    elif message.text == '/Bakalavriat':
        keyboard = types.InlineKeyboardMarkup()
        button1 = create_button('bakal', '1')
        button2 = create_button('bakal', '2')
        button3 = create_button('bakal', '3')
        button4 = create_button('bakal', '4')
        button5 = create_button('bakal', '5')
        button6 = create_button('bakal', '6')
        button7 = create_button('bakal', '7')
        button8 = create_button('bakal', '8')
        button9 = create_button('bakal', '9')
        button10 = create_button('bakal', '10')
        button11 = create_button('bakal', '11')
        keyboard.add(button1, button2, button3)
        keyboard.add(button4, button5, button6)
        keyboard.add(button7, button8, button9)
        keyboard.add(button10, button11)
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
                         'Eсли хочешь оставить заявку чтобы тебе перезвонили напиши /reg\n', reply_markup=keyboard)

    elif message.text == '/Magistratura':
        keyboard = types.InlineKeyboardMarkup()
        button1 = create_button('magi', '1')
        button2 = create_button('magi', '2')
        button3 = create_button('magi', '3')
        button4 = create_button('magi', '4')
        button5 = create_button('magi', '5')
        button6 = create_button('magi', '6')
        button7 = create_button('magi', '7')
        button8 = create_button('magi', '8')
        button9 = create_button('magi', '9')
        button10 = create_button('magi', '10')

        keyboard.add(button1, button2, button3)
        keyboard.add(button4, button5, button6)
        keyboard.add(button7, button8, button9)
        keyboard.add(button10)
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
            
                         'Eсли хочешь оставить заявку чтобы тебе перезвонили напиши /reg\n', reply_markup=keyboard)

    elif message.text == '/dop_info':
        keyboard = types.InlineKeyboardMarkup()
        button1 = create_button('dop', '1')
        button2 = create_button('dop', '2')
        button3 = create_button('dop', '3')
        button4 = create_button('dop', '4')
        button5 = create_button('dop', '5')
        button6 = create_button('dop', '6')
        button7 = create_button('dop', '7')
        button8 = create_button('dop', '8')
        button9 = create_button('dop', '9')
        button10 = create_button('dop', '10')

        keyboard.add(button1, button2, button3)
        keyboard.add(button4, button5, button6)
        keyboard.add(button7, button8, button9)
        keyboard.add(button10)
        bot.send_message(user, 'Нажми кнопку с цифрой интересующего тебя вопроса:\n\n'
                               '1. International course "Digital economy & AgriFoodTech" (на английском языке) Bachelor’s Degree''\n'
                               '2. Дополнительное образование Цифровая Экономика в АПК (252 часа)\n'
                               '3. MBA Executive\n'
                               '4. Startup-студия. Центр инновационного предпринимательства.\n'
                               '5. Консалтинг, индивидуальные консультации\n'
                               '6. Хочу стать партнёром ЦифрЭк\n'
                               '7. Контакты'
                               '8. Попасть на сайт ЦифрЭк\n'
                               '9. Как добраться в ЦифрЭк\n'
                               '10. Другое. Задать свой вопрос.\n\n'

                               'Eсли хочешь оставить заявку чтобы тебе перезвонили напиши /reg\n',
                         reply_markup=keyboard)

    elif message.text == '/reg':
        bot.send_message(user, 'Начнем заполнять заявку!\n Как тебя зовут?')
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(user, 'Простите, я вас не понимаю, напишите /help')


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_last_name)


def get_last_name(message):
    global last_name
    last_name = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    age = message.text
    bot.send_message(message.from_user.id, 'Какой твой номер телефона?')
    bot.register_next_step_handler(message, get_number)


def get_number(message):
    global name, last_name, age, number
    number = message.text
    tablework.save_data([name, last_name, age, number])
    bot.send_message(message.from_user.id, 'Спасибо, после обработки заявки тебе обязательно перезвонят!')


def main():
    try:
        print('Бот запущен успешно')
        bot.polling()
    except Exception:
        print('Ошибка!')


if __name__ == '__main__':
    main()
