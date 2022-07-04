from telebot import types
from Bd.libraries.lib import create_button


# keyboards
help_keyboard = types.ReplyKeyboardMarkup(row_width=1).add(*{
    create_button('Бакалавриат/Специалитет', 'basic-bach'),
    create_button('Магистратура', 'basic-magi'),
    create_button('Аспирантура', 'basic-inter')
})

bach_keyboard = types.InlineKeyboardMarkup(row_width=1).add(*[
    create_button('1. Какие документы необходимы для подачи?', 'bach-ask_1'),
    create_button('2. На сколько направлений Я могу подать документы?', 'bach-ask_2'),
    create_button('3. Что такое очна-заочная форма обучения?', 'bach-ask_3'),
    create_button('4. Перевод из другого ВУЗа', 'bach-ask_4'),
    create_button('5. Кто может сдавать внутренние вступительные испытания?', 'bach-ask_5'),
    create_button('6. Особая квота', 'bach-ask_6'),
    create_button('7. Справка 086-У', 'bach-ask_7'),
])

magi_keyboard = types.InlineKeyboardMarkup(row_width=1).add(*[
    create_button('1. Какие документы необходимы для подачи?', 'magi-ask_1'),
    create_button('2. На сколько направлений Я могу подать документы?', 'magi-ask_2'),
    create_button('3. Перевод из другого ВУЗа', 'magi-ask_3'),
    create_button('4. Справка 086-У', 'magi-ask_4'),
    create_button('5. Внутренние вступительные испытания', 'magi-ask_5'),
])
inter_keyboard = types.InlineKeyboardMarkup(row_width=1).add(*[
    create_button('1. Подробнее об уровне образования', 'inter-ask_1'),
])