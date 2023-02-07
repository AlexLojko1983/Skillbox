print('Hello')  # функция вывода

name = 'Alex'  # переменная

user_info = ['Alex', 'Привет! Как дела', '2023-02-06']

print(user_info[0])

for i in user_info:
    print('>>', 'Hi', i)

""" Словарь"""

chat_dict = {}

chat_dict['Саша'] = ['привет ребята'], ['21-34']
chat_dict['viktor'] = ['ku'], ['22-01']

print(chat_dict['viktor'])

"""импорт"""
#
import datetime as dt

#
print(dt.datetime.now())
#
from datetime import datetime

#
print(datetime.now())

"""Мессенджер"""

all_messages = []

"""Создание словаря с ключами sender, text, time. Забрасываем его в пустой словарь"""


def add_message(sender, text):
    new_message = {
        'sender': sender,
        'text': text,
        'time': datetime.now()
    }
    all_messages.append(new_message)


"""Вывод на печать ... Кто что когда. !!! по одному сообщению!!!"""


def print_message(new_message):
    print('Отправитель', new_message['sender'], '| Текст:', new_message['text'], '| Время отправления:',
          new_message['time'])


"""Печать всех сообщений сразу"""


def print_all_messages(all_messages):
    for new_message in all_messages:
        print_message(new_message)


add_message('Alex', 'Привет бот')
add_message('viktor', 'Тот еще сапог')

print_all_messages(all_messages)
