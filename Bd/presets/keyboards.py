from telebot import types
from Bd.libraries.lib import create_button


# keyboards
help_keyboard = types.ReplyKeyboardMarkup(row_width=1).add(*[
    create_button('ЭШКО Young', 'basic-eshko'),
    create_button('Бакалавриат', 'basic-bach'),
    create_button('Магистратура', 'basic-magi'),
    create_button('International course (на английском языке)', 'basic-inter'),
    create_button('ДПО ЦифрЭк в АПК (252 часа)', 'basic-dpo'),
    create_button('Другое. Задать свой вопрос.', 'basic-drugoe'),

])

eshko_keyboard = types.InlineKeyboardMarkup(row_width=1).add(*[
    create_button('1. Какой срок обучения?', 'eshko-ask_1'),
    create_button('2. Какая стоимость обучения?', 'eshko-ask_2'),
    create_button('3. Есть ли бюджетные места?', 'eshko-ask_3'),
    create_button('4. Какие экзамены необходимы для поступления?', 'eshko-ask_4'),
    create_button('5. Какие документы необходимо подать в вуз?', 'eshko-ask_5'),

    create_button('Зарегистрироваться', 'reg-eshko'),
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

    create_button('Зарегистрироваться', 'reg-bach'),
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

    create_button('Зарегистрироваться', 'reg-magi'),
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

    create_button('Register ', 'reg-inter'),
])

dpo_keyboard = types.InlineKeyboardMarkup(row_width=1).add(*[
    create_button('1. Срок обучения?', 'dpo-ask_1'),
    create_button('2. Блоки преподаваемых дисциплин', 'dpo-ask_2'),
    create_button('3. Стоимость обучения', 'dpo-ask_3'),
    create_button('4. Подробнее о программе. Ригистрация', 'dpo-ask_4'),

    create_button('Зарегистрироваться', 'reg-dpo'),
])


drugoe_keyboard = types.InlineKeyboardMarkup(row_width=1).add(*[
    create_button('1. Наш сайт', 'drugoe-ask_1'),
    create_button('2. Как добраться в ЦифрЭк?', 'drugoe-ask_2'),
    create_button('3. Хочу стать партнёром ЦифрЭк', 'drugoe-ask_3'),
    create_button('4. MBA/Программа для продвинутых', 'drugoe-ask_4'),
    create_button('5. Преврати свою идею в прибыльный бизнес!', 'drugoe-ask_5'),
    create_button('6. Консалтинговые услуги ЦифрЭк КубГАУ', 'drugoe-ask_6'),
    create_button('7. Наши контакы', 'drugoe-ask_7'),
])
