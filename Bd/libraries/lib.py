from telebot import types


def issued(reason, text):
    """
    Выведение в консоль информации.

    :return: нету
    """
    print(f"> Вызван {reason} для \'{text}\'" if text else "> Комманда отсутствует.")


def create_button(text, call) -> types.InlineKeyboardButton:
    """
    Функция возвращает кнопку с заданным callback.

    :return: InlineKeyboardButton
    """
    return types.InlineKeyboardButton(text=text, callback_data=call)


def fill_keyboard(buttons, width) -> types.InlineKeyboardMarkup:
    """
    Возвращает клавиатуру с кнопками с заданным количеством столбцов.

    :return: InlineKeyboardMarkup
    """
    return types.InlineKeyboardMarkup(row_width=width).add(*buttons)


def search_ask(keyboards: dict, call: str) -> str:
    """
    Возвращает текст вопроса к данному сall.

    :return: str
    """
    for i in keyboards.values():
        for j in i.keyboard:
            if call == j[0].callback_data:
                return j[0].text


def format_text(text: str, modes: list) -> str:
    for i in modes:
        text = f'<{i}>{text}</{i}>'
    return text


class MultiDict:
    """
    Самодельный словарь в которм можно задавать ключ в аргументе(привязки ключа нету).
    Состоит из списка списков, внутри которых - связанные элементы.
    """

    def __init__(self, *args):
        self.lst = [i for i in args]

    def get_value(self, value, mode: int):
        if mode == 1 or mode == 0:
            for i in self.lst:
                if i[mode] == value:
                    return i[1 - mode]
            raise Exception('Not found key in selected mode and list')
        raise Exception('Wrong mode selected')

    def get_data(self, mode: int):
        if mode == 1 or mode == 0:
            return [i[mode] for i in self.lst]
        raise Exception('Wrong mode selected')
