from sys import argv

import telebot

import sensitive_config


bot = telebot.TeleBot(sensitive_config.token)
bot.send_message(sensitive_config.master_id,
                 "Bot was restarted because some issue ({}):\n<code>{}</code>".format(argv[1].split('.')[0], argv[2]),
                 parse_mode='HTML')
