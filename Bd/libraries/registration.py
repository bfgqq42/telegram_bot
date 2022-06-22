import os
import sqlite3
import time


def create_db(file, execute):
    """
    Создание файла базы данных.

    :return: нету
    """
    con = sqlite3.connect(file)
    cur = con.cursor()
    cur.execute(execute)
    con.commit()
    con.close()


# bach
class RegisterBachMagi:

    def __init__(self, bot, message, user, dbname):
        self.user = user
        self.bot, self.dbname = bot, dbname
        self.name, self.last_name, self.age, self.number, self.reason = '', '', '', '', ''
        self.bot.send_message(self.user, 'Начнем заполнять заявку!\n'
                                         'Как тебя зовут?')
        self.bot.register_next_step_handler(message, self.get_name)

    def get_name(self, message):
        self.name = message.text
        self.bot.send_message(self.user, 'Какая у тебя фамилия?')
        self.bot.register_next_step_handler(message, self.get_last_name)

    def get_last_name(self, message):
        self.last_name = message.text
        self.bot.send_message(self.user, 'Сколько тебе лет?')
        self.bot.register_next_step_handler(message, self.get_age)

    def get_age(self, message):
        self.age = message.text
        self.bot.send_message(self.user, 'Какой твой номер телефона?')
        self.bot.register_next_step_handler(message, self.get_number)

    def get_number(self, message):
        self.number = message.text
        self.bot.send_message(self.user, 'Опиши свой вопрос.')
        self.bot.register_next_step_handler(message, self.get_reason)

    def get_reason(self, message):
        self.reason = message.text
        self.write_data()
        self.bot.send_message(self.user, 'Спасибо, после обработки заявки тебе обязательно перезвонят!')

    def write_data(self):
        file = f'db/{self.dbname}.db'

        if f'{self.dbname}.db' not in os.listdir('db'):
            create_db(file,
                      '''CREATE TABLE stocks 
                      (date text, name text, last_name text, age text, phone text, question text)''')

        con = sqlite3.connect(file)
        cur = con.cursor()
        cur.execute(f"INSERT INTO stocks VALUES "
                    f"("
                    f"\'{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}\',"
                    f"\'{self.name}\',"
                    f"\'{self.last_name}\',"
                    f"\'{self.age}\',"
                    f"\'{self.number}\',"
                    f"\'{self.reason}\'"
                    f")")
        con.commit()
        con.close()


class RegisterEshko:

    def __init__(self, bot, message, user, dbname):
        self.user = user
        self.bot, self.dbname = bot, dbname
        self.name_surname, self.abit, self.apply, self.phone, self.city = '', '', '', '', ''
        self.bot.send_message(self.user, 'Начнем заполнять заявку!\n'
                                         'Напишите Фамилию и Имя')
        self.bot.register_next_step_handler(message, self.get_name)

    def get_name(self, message):
        self.name_surname = message.text
        self.bot.send_message(self.user, 'Уже абитуриент или еще школьник(укажите класс)?')
        self.bot.register_next_step_handler(message, self.get_last_name)

    def get_last_name(self, message):
        self.abit = message.text
        self.bot.send_message(self.user, 'Куда хотите поступать(ЦифрЭк/бухучет/в мед/свой вариант)?')
        self.bot.register_next_step_handler(message, self.get_age)

    def get_age(self, message):
        self.apply = message.text
        self.bot.send_message(self.user, 'Ваш номер телефона')
        self.bot.register_next_step_handler(message, self.get_number)

    def get_number(self, message):
        self.phone = message.text
        self.bot.send_message(self.user, 'Из какого вы города?')
        self.bot.register_next_step_handler(message, self.get_reason)

    def get_reason(self, message):
        self.city = message.text
        self.write_data()
        self.bot.send_message(self.user, 'Спасибо, после обработки заявки тебе обязательно перезвонят!')

    def write_data(self):
        file = f'db/{self.dbname}.db'

        if f'{self.dbname}.db' not in os.listdir('db'):
            create_db(file,
                      '''CREATE TABLE stocks 
                      (date text, name_surname text, abit text, apply text, phone text, city text)''')
            con = sqlite3.connect(file)
            cur = con.cursor()
            cur.execute(f"INSERT INTO stocks VALUES "
                        f"("
                        f"\'{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}\',"
                        f"\'{self.name_surname}\',"
                        f"\'{self.abit}\',"
                        f"\'{self.apply}\',"
                        f"\'{self.phone}\',"
                        f"\'{self.city}\'"
                        f")")
            con.commit()
            con.close()

class RegisterDPO:

    def __init__(self, bot, message, user, dbname):
        self.user = user
        self.bot, self.dbname = bot, dbname
        self.name, self.last_name, self.age, self.number, self.reason = '', '', '', '', ''
        self.bot.send_message(self.user, 'Начнем заполнять заявку!\n'
                                         'Как тебя зовут?')
        self.bot.register_next_step_handler(message, self.get_name)

    def get_name(self, message):
        self.name = message.text
        self.bot.send_message(self.user, 'Какая у тебя фамилия?')
        self.bot.register_next_step_handler(message, self.get_last_name)

    def get_last_name(self, message):
        self.last_name = message.text
        self.bot.send_message(self.user, 'Сколько тебе лет?')
        self.bot.register_next_step_handler(message, self.get_age)

    def get_age(self, message):
        self.age = message.text
        self.bot.send_message(self.user, 'Какой твой номер телефона?')
        self.bot.register_next_step_handler(message, self.get_number)

    def get_number(self, message):
        self.number = message.text
        self.bot.send_message(self.user, 'Опиши свой вопрос.')
        self.bot.register_next_step_handler(message, self.get_reason)

    def get_reason(self, message):
        self.reason = message.text
        self.write_data()
        self.bot.send_message(self.user, 'Спасибо, после обработки заявки тебе обязательно перезвонят!')

    def write_data(self):
        file = f'db/{self.dbname}.db'

        if f'{self.dbname}.db' not in os.listdir('db'):
            create_db(file,
                      '''CREATE TABLE stocks 
                      (date text, name text, last_name text, age text, phone text, question text)''')

        con = sqlite3.connect(file)
        cur = con.cursor()
        cur.execute(f"INSERT INTO stocks VALUES "
                    f"("
                    f"\'{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}\',"
                    f"\'{self.name}\',"
                    f"\'{self.last_name}\',"
                    f"\'{self.age}\',"
                    f"\'{self.number}\',"
                    f"\'{self.reason}\'"
                    f")")
        con.commit()
        con.close()

class RegisterIntero:

    def __init__(self, bot, message, user, dbname):
        self.user = user
        self.bot, self.dbname = bot, dbname
        self.name_surname, self.abit, self.apply, self.phone, self.city = '', '', '', '', ''
        self.bot.send_message(self.user, 'Начнем заполнять заявку!\n'
                                         'Напишите Фамилию и Имя')
        self.bot.register_next_step_handler(message, self.get_name)

    def get_name(self, message):
        self.name_surname = message.text
        self.bot.send_message(self.user, 'Уже абитуриент или еще школьник(укажите класс)?')
        self.bot.register_next_step_handler(message, self.get_last_name)

    def get_last_name(self, message):
        self.abit = message.text
        self.bot.send_message(self.user, 'Куда хотите поступать(ЦифрЭк/бухучет/в мед/свой вариант)?')
        self.bot.register_next_step_handler(message, self.get_age)

    def get_age(self, message):
        self.apply = message.text
        self.bot.send_message(self.user, 'Ваш номер телефона')
        self.bot.register_next_step_handler(message, self.get_number)

    def get_number(self, message):
        self.phone = message.text
        self.bot.send_message(self.user, 'Из какого вы города?')
        self.bot.register_next_step_handler(message, self.get_reason)

    def get_reason(self, message):
        self.city = message.text
        self.write_data()
        self.bot.send_message(self.user, 'Спасибо, после обработки заявки тебе обязательно перезвонят!')

    def write_data(self):
        file = f'db/{self.dbname}.db'

        if f'{self.dbname}.db' not in os.listdir('db'):
            create_db(file,
                      '''CREATE TABLE stocks 
                      (date text, name_surname text, abit text, apply text, phone text, city text)''')
            con = sqlite3.connect(file)
            cur = con.cursor()
            cur.execute(f"INSERT INTO stocks VALUES "
                        f"("
                        f"\'{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}\',"
                        f"\'{self.name_surname}\',"
                        f"\'{self.abit}\',"
                        f"\'{self.apply}\',"
                        f"\'{self.phone}\',"
                        f"\'{self.city}\'"
                        f")")
            con.commit()
            con.close()

class RegisterInter:

    def __init__(self, bot, message, user, dbname):
        self.user = user
        self.bot, self.dbname = bot, dbname
        self.name_surname, self.abit, self.apply, self.phone, self.city = '', '', '', '', ''
        self.bot.send_message(self.user, 'Lets start filling out the application!\n'
                                         'Напишите Фамилию и Имя')
        self.bot.register_next_step_handler(message, self.get_name)

    def get_name(self, message):
        self.name_surname = message.text
        self.bot.send_message(self.user, 'Уже абитуриент или еще школьник(укажите класс)?')
        self.bot.register_next_step_handler(message, self.get_last_name)

    def get_last_name(self, message):
        self.abit = message.text
        self.bot.send_message(self.user, 'Куда хотите поступать(ЦифрЭк/бухучет/в мед/свой вариант)?')
        self.bot.register_next_step_handler(message, self.get_age)

    def get_age(self, message):
        self.apply = message.text
        self.bot.send_message(self.user, 'Ваш номер телефона')
        self.bot.register_next_step_handler(message, self.get_number)

    def get_number(self, message):
        self.phone = message.text
        self.bot.send_message(self.user, 'Из какого вы города?')
        self.bot.register_next_step_handler(message, self.get_reason)

    def get_reason(self, message):
        self.city = message.text
        self.write_data()
        self.bot.send_message(self.user, 'Спасибо, после обработки заявки тебе обязательно перезвонят!')

    def write_data(self):
        file = f'db/{self.dbname}.db'

        if f'{self.dbname}.db' not in os.listdir('db'):
            create_db(file,
                      '''CREATE TABLE stocks 
                      (date text, name_surname text, abit text, apply text, phone text, city text)''')
            con = sqlite3.connect(file)
            cur = con.cursor()
            cur.execute(f"INSERT INTO stocks VALUES "
                        f"("
                        f"\'{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}\',"
                        f"\'{self.name_surname}\',"
                        f"\'{self.abit}\',"
                        f"\'{self.apply}\',"
                        f"\'{self.phone}\',"
                        f"\'{self.city}\'"
                        f")")
            con.commit()
            con.close()
