import telebot

from Bd.presets.keyboards import *
from Bd.libraries.lib import *

from data.json_work import read
from Bd.libraries.registration import Register


# bot configuration
token = '5311880278:AAHyAHNG3feWC-aQuj_N5zSOAeU-qOQIfRI'
bot: telebot.TeleBot = telebot.TeleBot(token)


# shortcuts
main_text = 'Нажми кнопку с цифрой интересующего тебя вопроса:\n' \
            'Eсли хочешь оставить заявку чтобы тебе перезвонили по данному вопросу напиши'

shortcut = MultiDict(
    ['bach', 'Бакалавриат'],
    ['magi', 'Магистратура'],
    ['inter', 'International course (на английском языке)'],
    ['dpo', 'ДПО ЦифрЭк в АПК (252 часа)'],
    ['mba', 'MBA Executive'],
    ['startup', 'Startup-студия'],
    ['kasal', 'Консалтинг'],
    ['popas', 'Хочу стать партнёром ЦифрЭк'],
    ['dobav', 'Как добраться в ЦифрЭк'],
    ['drugoe', 'Другое. Задать свой вопрос.']
)

all_keyboards = {
    'bach': bach_keyboard,
    'magi': magi_keyboard,
    'inter': inter_keyboard,
    'dpo': dpo_keyboard,
    'drugoe': drugoe_keyboard
}

ask_answers = {
    'bach': read('bach'),
    'magi': read('magi'),
    'inter': read('inter'),
    'dpo': read('dpo'),
    'drugoe': read('drugoe')
}


@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    issued("callback", call.data)

    if 'ask' in call.data:
        spec, name = call.data.split('-')
        text = search_ask(all_keyboards, call.data)

        bot.send_message(chat_id=call.message.chat.id,
                         text=f'<u><i><b>{text}</b></i></u>\n' + ask_answers[spec][name],
                         reply_markup=types.InlineKeyboardMarkup(row_width=1).add(*[
                             create_button('Вернуться назад', f'return-{spec}')
                         ]),
                         parse_mode='HTML')

    elif 'return' in call.data:
        text = call.data.split('-')[1]

        bot.send_message(chat_id=call.message.chat.id,
                         text=f'<u><i><b>{shortcut.get_value(text, 0)}</b></i></u>\n' + main_text + f' /reg_{text}\n',
                         reply_markup=all_keyboards[text], parse_mode='HTML')

    elif 'reg' in call.data:
        dbname = call.data.split('-')[1]
        Register(bot, call.message, call.from_user.id, dbname)


@bot.message_handler(content_types=['text'])
def start(message):
    issued("command", message.text)

    if message.text in ['/help', '/start', 'Здравствуй', 'Здарова', 'Добрый день']:
        bot.send_message(chat_id=message.from_user.id,
                         text='Выбери одно из интересующих тебя направлений',
                         reply_markup=help_keyboard)

    elif message.text in shortcut.get_data(1):
        name = shortcut.get_value(message.text, 1)
        bot.send_message(chat_id=message.from_user.id,
                         text=f'<u><i><b>{message.text}</b></i></u>\n' + main_text + f' /reg_{name}\n',
                         reply_markup=all_keyboards[name], parse_mode='HTML')

    else:
        bot.send_message(chat_id=message.from_user.id,
                         text='Простите, я вас не понимаю. Напишите /help')


if __name__ == '__main__':
    print('> Bot started successfully!')
    bot.polling()
    # try:
    #
    # except Exception as e:
    #     print(f'> Exception caught "{e}"')
