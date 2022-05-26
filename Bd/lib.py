from telebot import types


def issued(reason, text):
    """
    Выведение в консоль информации.

    :return: нету
    """
    print(f"> Вызван код {reason} для причины \'{text}\'" if text else "> Комманда отсутствует.")


def create_button(text, call):
    """
    Функция возвращает кнопку с заданным callback.

    :return: InlineKeyboardButton
    """
    return types.InlineKeyboardButton(text=text, callback_data=call)


def fill_keyboard(buttons, width):
    """
    Возвращает клавиатуру с кнопками с заданным количеством столбцов.

    :return: InlineKeyboardMarkup
    """
    return types.InlineKeyboardMarkup(row_width=width).add(*buttons)


