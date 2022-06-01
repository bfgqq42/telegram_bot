from Bd.libraries import dbwork


class Register:

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
        dbwork.save_data([self.name, self.last_name, self.age, self.number, self.reason], self.dbname)
        self.bot.send_message(self.user, 'Спасибо, после обработки заявки тебе обязательно перезвонят!')
