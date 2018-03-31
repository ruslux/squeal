import re

import telebot

# import db
import sensitive_config
import strings


class Squeal(telebot.TeleBot):
    def __init__(self):
        super().__init__(sensitive_config.token)

        def get_data(message, parent_function, regexp):
            if re.search(regexp, message.text):
                return message.text
            else:
                self.send_message(message.chat.id, strings.dialog.parse_error)
                self.register_next_step_handler(message, parent_function)

        @self.message_handler(commands=['start'])
        def start(message):
            self.send_message(message.chat.id, strings.dialog.start, parse_mode='Markdown')
            if True:
                self.send_message(message.chat.id, strings.dialog.start_setup + strings.dialog.full_name_format)
                self.register_next_step_handler(message, get_full_name)

        def get_full_name(message):
            telegram_id = message.chat.id
            full_name = get_data(message, get_full_name, r'^\w+ \w+$')
            first_name = re.search(r'^\w+', full_name)
            second_name = re.search(r'\w+$', full_name)
            email = first_name.lower() + '.' + second_name.lower() + '@spl.co'

            # db.User.set(telegram_id, 'first_name', first_name)
            # db.User.set(telegram_id, 'second_name', second_name)
            # db.User.set(telegram_id, 'email', email)

            get_auth(message)

        def get_auth(message):
            telegram_id = message.chat.id
            # email = db.User.get(telegram_id, 'email')
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(
                telebot.types.InlineKeyboardButton(strings.button.auth, callback_data='auth'),
                telebot.types.InlineKeyboardButton(strings.button.change_email, callback_data='change_email')
            )
            # self.send_message(message.chat.id,
            #                   strings.dialog.get_auth.format(current_email=email),
            #                   reply_markup=markup)

        @self.callback_query_handler(func=lambda callback: callback.data == 'change_email')
        def get_email(callback):
            self.send_message(callback.message.chat.id, strings.dialog.get_email)
            self.register_next_step_handler(callback.message, change_email)

            self.edit_message_text(callback.message.message_id, )

        def change_email(message):
            if re.search(r'\w+\.\w+@\w+\.\w+', message.text):
                get_auth(message)
            else:
                self.send_message(message.chat.id, "Ты указал невалидный email, попробуй еще разок")
                self.register_next_step_handler(message, get_email)


if __name__ == '__main__':
    bot = Squeal()
    bot.polling(none_stop=True)
