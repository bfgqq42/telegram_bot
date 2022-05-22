from Bd import dbwork


class Register:

    def __init__(self, bot, message, dbname):
        self.bot, self.dbname = bot, dbname
        self.name, self.last_name, self.age, self.number = '', '', '', ''
        self.bot.send_message(message.from_user.id, 'Начнем заполнять заявку!\n'
                                                    'Как тебя зовут?')
        self.bot.register_next_step_handler(message, self.get_name)

    def get_name(self, message):
        self.name = message.text
        self.bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
        self.bot.register_next_step_handler(message, self.get_last_name)

    def get_last_name(self, message):
        self.last_name = message.text
        self.bot.send_message(message.from_user.id, 'Сколько тебе лет?')
        self.bot.register_next_step_handler(message, self.get_age)

    def get_age(self, message):
        self.age = message.text
        self.bot.send_message(message.from_user.id, 'Какой твой номер телефона?')
        self.bot.register_next_step_handler(message, self.get_number)

    def get_number(self, message):
        self.number = message.text
        dbwork.save_data([self.name, self.last_name, self.age, self.number], self.dbname)
        self.bot.send_message(message.from_user.id, 'Спасибо, после обработки заявки тебе обязательно перезвонят!')
