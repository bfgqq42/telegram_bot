from telebot import types
from Bd.libraries.lib import create_button


# keyboards
help_keyboard = types.ReplyKeyboardMarkup(row_width=1).add(*[
    create_button('ЭШКО Young', 'basic-eshko'),
    create_button('Бакалавриат', 'basic-bach'),
    create_button('Магистратура', 'basic-magi'),
    create_button('International course (на английском языке)', 'basic-inter'),
    create_button('Дополнительное образование(252 часа)', 'basic-dpo'),
    create_button('Другое', 'basic-drugoe'),

])

eshko_keyboard = types.InlineKeyboardMarkup(row_width=1).add(*[
    create_button('1. Какой срок обучения?', 'eshko-ask_1'),
    create_button('2. Какая стоимость обучения?', 'eshko-ask_2'),
    create_button('3. Какой формат обучения?', 'eshko-ask_3'),
    create_button('4. Подробнее об ЭШКО', 'eshko-ask_4'),

    create_button('Обратная связь', 'reg-eshko'),
])

bach_keyboard = types.InlineKeyboardMarkup(row_width=1).add(*[
    create_button('1. Какой срок обучения?', 'bach-ask_1'),
    create_button('2. Стоимость обучения', 'bach-ask_2'),
    create_button('3. Бюджетные места', 'bach-ask_3'),
    create_button('4. Экзамены для поступления', 'bach-ask_4'),
    create_button('5. Документы для поступления', 'bach-ask_5'),
    create_button('6. Есть ли общежитие?', 'bach-ask_6'),
    create_button('7. Проходной балл', 'bach-ask_7'),
    create_button('8. Заключить договор', 'bach-ask_8'),
    create_button('9. Военная кафедра', 'bach-ask_9'),

    create_button('Обратная связь', 'reg-bach'),
])

magi_keyboard = types.InlineKeyboardMarkup(row_width=1).add(*[
    create_button('1. Какой срок обучения?', 'magi-ask_1'),
    create_button('2. Какая стоимость обучения?', 'magi-ask_2'),
    create_button('3. Есть ли бюджетные места?', 'magi-ask_3'),
    create_button('4. Есть ли военная кафедра?', 'magi-ask_4'),
    create_button('5. Проходной балл', 'magi-ask_5'),
    create_button('6. Экзамены для сдачи', 'magi-ask_6'),
    create_button('7. Есть ли общежитие?', 'magi-ask_7'),
    create_button('8. Заключить договор', 'magi-ask_8'),
    create_button('9. Подробнее о программе', 'magi-ask_9'),

    create_button('Обратная связь', 'reg-magi'),
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
    create_button('1. Подробнее о программе', 'dpo-ask_4'),
    create_button('2. Преподаваемые дисциплины', 'dpo-ask_2'),
    create_button('3. Стоимость обучения', 'dpo-ask_3'),
    create_button('4. Срок обучения', 'dpo-ask_1'),

    create_button('Обратная связь', 'reg-dpo'),
])


drugoe_keyboard = types.InlineKeyboardMarkup(row_width=1).add(*[
    create_button('1. Партнерство ЦифрЭк', 'drugoe-ask_3'),
    create_button('2. MBA/Углубленный уровень', 'drugoe-ask_4'),
    create_button('3. Преврати идею в бизнес!', 'drugoe-ask_5'),
    create_button('4. Консалтинг ЦифрЭк', 'drugoe-ask_6'),
    create_button('5. Наш сайт', 'drugoe-ask_1'),
    create_button('6. Мы в социальных сетях', 'drugoe-ask_7'),
    create_button('7. Режим работы', 'drugoe-ask_8'),
    create_button('8. Как добраться в ЦифрЭк?', 'drugoe-ask_2'),

])
