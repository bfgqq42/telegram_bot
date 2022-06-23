import telebot

from Bd.presets.keyboards import *
from Bd.libraries.lib import *

from data.json_work import read


# bot configuration
token = '5428301440:AAGACq5BLVyew5mnPpi-pGSCtqIUHF1t99E'
bot: telebot.TeleBot = telebot.TeleBot(token)


# shortcuts
main_text = 'Выберете интересующий Вас вопрос:'

shortcut = MultiDict(
    ['bach', 'Бакалавриат/Специалитет'],
    ['magi', 'Магистратура'],
    ['inter', 'Аспирантура']
)

all_keyboards = {
    'bach': bach_keyboard,
    'magi': magi_keyboard,
    'inter': inter_keyboard
}

ask_answers = {
    'bach': read('bach'),
    'magi': read('magi'),
    'inter': read('inter')
}


@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    issued("callback", call.data)

    if 'ask' in call.data:
        spec, name = call.data.split('-')
        text = search_ask(all_keyboards, call.data)

        bot.send_message(chat_id=call.message.chat.id,
                         text=f'<b><>{text}</b>\n' + ask_answers[spec][name],
                         reply_markup=types.InlineKeyboardMarkup(row_width=1).add(*[
                             create_button('Вернуться назад', f'return-{spec}')
                         ]),
                         parse_mode='HTML')

    elif 'return' in call.data:
        text = call.data.split('-')[1]

        bot.send_message(chat_id=call.message.chat.id,
                         text=f'{format_text(shortcut.get_value(text, 0), "uib")}\n' + main_text,
                         reply_markup=all_keyboards[text], parse_mode='HTML')



@bot.message_handler(content_types=['text'])
def start(message):
    issued("command", message.text)

    if message.text in ['/help', '/start', 'Здравствуй', 'Здарова', 'Добрый день']:
        bot.send_message(chat_id=message.from_user.id,
                         text='Выбери одно из интересующих тебя направлений:',
                         reply_markup=help_keyboard)

    elif message.text in shortcut.get_data(1):
        name = shortcut.get_value(message.text, 1)
        bot.send_message(chat_id=message.from_user.id,
                         text=f'<b>{message.text}</b>\n' + main_text,
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
