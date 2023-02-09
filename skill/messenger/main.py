from datetime import datetime
from flask import Flask, render_template, request
import json

app = Flask(__name__)

"""СОЗДАЕМ Функции. Для добавления и сохранения пользователя"""

"""Откроем файл для чтения(db.json) Словарь. """


def load_info(db_name):
    with open(db_name, 'r') as db:  # Открываем для чтения
        db_info = json.load(db)
    return db_info['messanges']


"""функция для сохранения """


def save_info(db_info, db_name):  # Параметры: Файл и переменная куда пишем
    with open(db_name, 'w') as json_file:  # Открываем файл для записи
        json.dump({'messanges': db_info}, json_file)  # Записываем (не забывая, что пишем "словарь")


db_name = 'db.json'  # переменная
all_messages = load_info(db_name)

"""Добавляем страницу чата"""


@app.route('/chat')
def display_chat():
    return render_template('form.html')


"""Добавляем и сохраняем сообщение"""


@app.route('/get_messages')  # параметр смотрим в html
def get_message():
    return {'messages': all_messages}  # Словарь messages записываем all_messages


"""Функция для отправки сообщения"""


@app.route('/send_message')  # параметр смотрим в html
def send_message():
    sender = request.args['name']  # По ключу name получаем пользователя
    text = request.args['text']
    time = datetime.now().strftime('%H:%M')
    text_info = {  # Создаем словарь
        'text': text,
        'sender': sender,
        'time': time
    }
    all_messages.append(text_info)  # Добавляем в переменную all_messages
    save_info(all_messages, db_name)  # Сохраняем в файле


"""страница (индекс)"""


@app.route('/index')
def index_page():
    return "Hello Sania"


"""Запускаем сервак(127,0,0,0:80)"""

app.run(host='0.0.0.0', port=80)
