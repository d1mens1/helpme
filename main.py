import os
import sqlite3
import time

import telebot
from dotenv import load_dotenv
from telebot import types

load_dotenv()
TOKEN = str(os.environ['TOKEN'])
bot = telebot.TeleBot(TOKEN)

base = sqlite3.connect('database/database.db', check_same_thread=False)
cursor = base.cursor()


def splt(a): return " ".join(a.split("-"))


e = '\'game/work\''


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Начать")
    btnexit = types.KeyboardButton("Ойфсе")
    markup.add(btn1, btnexit)
    bot.send_message(message.chat.id, text="Здравствуйте.\nЯ Паскаль, помогу вам подобрать компьютерные комплектующие.".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Ойфсе"):
        delete = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, text="Самоуничтожение через", reply_markup=delete)
        time.sleep(1)
        bot.send_message(message.chat.id, text="5")
        time.sleep(1)
        bot.send_message(message.chat.id, text="4")
        time.sleep(1)
        bot.send_message(message.chat.id, text="3")
        time.sleep(1)
        bot.send_message(message.chat.id, text="2")
        time.sleep(1)
        bot.send_message(message.chat.id, text="1")
        time.sleep(1)
        bot.send_message(message.chat.id, text="Ошибка, нажмите /start, чтобы начать по-новой.")

    if (message.text == "Начать"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Низкий")
        btn2 = types.KeyboardButton("Средний")
        btn3 = types.KeyboardButton("Высокий")
        btn4 = types.KeyboardButton("Неограниченный")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text="Бюджет конфигурации ПК".format(message.from_user), reply_markup=markup)

    elif message.text == "Низкий":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        global a
        a = 1
        btn5 = types.KeyboardButton("Домашний компьютер")
        btn6 = types.KeyboardButton("Рабочий компьютер")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id,text="Область применения компьютера.\nДомашний компьютер (мультимедиа, развлечение, серфинг интернета)\nРабочий компьютер (офис, монтаж, сложные вычислительные задачи) ".format(message.from_user), reply_markup=markup)

    elif message.text == "Средний":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a = 2
        btn5 = types.KeyboardButton("Домашний компьютер")
        btn6 = types.KeyboardButton("Рабочий компьютер")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, text="Область применения компьютера.\nДомашний компьютер (мультимедиа, развлечение, серфинг интернета)\nРабочий компьютер (офис, монтаж, сложные вычислительные задачи)".format(message.from_user), reply_markup=markup)

    elif message.text == "Высокий":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a = 3
        btn5 = types.KeyboardButton("Домашний компьютер")
        btn6 = types.KeyboardButton("Рабочий компьютер")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, text="Область применения компьютера.\nДомашний компьютер (мультимедиа, развлечение, серфинг интернета)\nРабочий компьютер (офис, монтаж, сложные вычислительные задачи)".format(message.from_user), reply_markup=markup)

    elif message.text == "Неограниченный":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a = 4
        btn5 = types.KeyboardButton("Домашний компьютер")
        btn6 = types.KeyboardButton("Рабочий компьютер")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, text="Область применения компьютера.\nДомашний компьютер (мультимедиа, развлечение, серфинг интернета)\nРабочий компьютер (офис, монтаж, сложные вычислительные задачи)".format(message.from_user), reply_markup=markup)

    elif message.text == "Домашний компьютер":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        global b
        b = '\'game\''
        btn7 = types.KeyboardButton("8 Гб")
        btn8 = types.KeyboardButton("16 Гб")
        btn9 = types.KeyboardButton("32 Гб")
        btn10 = types.KeyboardButton("64 Гб")
        markup.add(btn7, btn8, btn9, btn10)
        bot.send_message(message.chat.id, text="Объем оперативной памяти(больше=лучше)".format(message.from_user),reply_markup=markup)

    elif message.text == "Рабочий компьютер":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b = '\'work\''
        btn7 = types.KeyboardButton("8 Гб")
        btn8 = types.KeyboardButton("16 Гб")
        btn9 = types.KeyboardButton("32 Гб")
        btn10 = types.KeyboardButton("64 Гб")
        markup.add(btn7, btn8, btn9, btn10)
        bot.send_message(message.chat.id, text="Объем оперативной памяти(больше=лучше)".format(message.from_user),reply_markup=markup)

    elif message.text == "8 Гб":
        c = '8'
        rcpu = cursor.execute(f'SELECT cpu_name FROM cpu WHERE cpu_price == {a} AND (cpu_task == {b} OR cpu_task == {e}) ORDER BY cpu_bench DESC').fetchone()[0]
        socket = cursor.execute(f'SELECT cpu_socket FROM cpu WHERE cpu_name == \'{rcpu}\' ').fetchone()[0]
        rgpu = cursor.execute(f'SELECT gpu_name FROM gpu WHERE gpu_price == {a} AND gpu_task == {b} ').fetchone()[0]
        mb = cursor.execute(f'SELECT mb_name FROM mother_board WHERE mb_socket == {socket} AND (mb_price == {a} OR mb_price == {3}) ').fetchone()[0]
        rram = cursor.execute(f'SELECT ram_name FROM ram WHERE ram_price == {a}').fetchone()[0]
        cputdp = cursor.execute(f'SELECT cpu_tdp FROM cpu WHERE cpu_name == \'{rcpu}\' ').fetchone()[0]
        gputdp = cursor.execute(f'SELECT gpu_tdp FROM gpu WHERE gpu_name == \'{rgpu}\' ').fetchone()[0]
        bp = cursor.execute(f'SELECT bp_name FROM bp WHERE bp_power > {cputdp + gputdp + 150}').fetchone()[0]

        bot.send_message(message.chat.id, f'В таком случае вам подходит процессор {splt(rcpu)}, в связке с видеокартой {rgpu}, с {c} Гб оперативной памяти серии {rram}, на базе материнской платы {mb}. Питать это будет блок питания {bp} ',reply_markup=types.ReplyKeyboardRemove())

    elif message.text == "16 Гб":
        c = '16'
        rcpu = cursor.execute(f'SELECT cpu_name FROM cpu WHERE cpu_price == {a} AND (cpu_task == {b} OR cpu_task == {e}) ORDER BY cpu_bench DESC').fetchone()[0]
        socket = cursor.execute(f'SELECT cpu_socket FROM cpu WHERE cpu_name == \'{rcpu}\' ').fetchone()[0]
        rgpu = cursor.execute(f'SELECT gpu_name FROM gpu WHERE gpu_price == {a} AND gpu_task == {b} ').fetchone()[0]
        mb = cursor.execute(f'SELECT mb_name FROM mother_board WHERE mb_socket == {socket} AND (mb_price == {a} OR mb_price == {3}) ').fetchone()[0]
        rram = cursor.execute(f'SELECT ram_name FROM ram WHERE ram_price == {a}').fetchone()[0]
        cputdp = cursor.execute(f'SELECT cpu_tdp FROM cpu WHERE cpu_name == \'{rcpu}\' ').fetchone()[0]
        gputdp = cursor.execute(f'SELECT gpu_tdp FROM gpu WHERE gpu_name == \'{rgpu}\' ').fetchone()[0]
        bp = cursor.execute(f'SELECT bp_name FROM bp WHERE bp_power > {cputdp + gputdp + 150}').fetchone()[0]

        bot.send_message(message.chat.id, f'В таком случае вам подходит процессор {splt(rcpu)}, в связке с видеокартой {rgpu}, с {c} Гб оперативной памяти серии {rram}, на базе материнской платы {mb}. Питать это будет блок питания {bp} ',reply_markup=types.ReplyKeyboardRemove())

    elif message.text == "32 Гб":
        c = '32'
        rcpu = cursor.execute(f'SELECT cpu_name FROM cpu WHERE cpu_price == {a} AND (cpu_task == {b} OR cpu_task == {e}) ORDER BY cpu_bench DESC').fetchone()[0]
        socket = cursor.execute(f'SELECT cpu_socket FROM cpu WHERE cpu_name == \'{rcpu}\' ').fetchone()[0]
        rgpu = cursor.execute(f'SELECT gpu_name FROM gpu WHERE gpu_price == {a} AND gpu_task == {b} ').fetchone()[0]
        mb = cursor.execute(f'SELECT mb_name FROM mother_board WHERE mb_socket == {socket} AND (mb_price == {a} OR mb_price == {3}) ').fetchone()[0]
        rram = cursor.execute(f'SELECT ram_name FROM ram WHERE ram_price == {a}').fetchone()[0]
        cputdp = cursor.execute(f'SELECT cpu_tdp FROM cpu WHERE cpu_name == \'{rcpu}\' ').fetchone()[0]
        gputdp = cursor.execute(f'SELECT gpu_tdp FROM gpu WHERE gpu_name == \'{rgpu}\' ').fetchone()[0]
        bp = cursor.execute(f'SELECT bp_name FROM bp WHERE bp_power > {cputdp + gputdp + 150}').fetchone()[0]

        bot.send_message(message.chat.id, f'В таком случае вам подходит процессор {splt(rcpu)}, в связке с видеокартой {rgpu}, с {c} Гб оперативной памяти серии {rram}, на базе материнской платы {mb}. Питать это будет блок питания {bp} ',reply_markup=types.ReplyKeyboardRemove())

    elif message.text == "64 Гб":
        c = '64'
        rcpu = cursor.execute(f'SELECT cpu_name FROM cpu WHERE cpu_price == {a} AND (cpu_task == {b} OR cpu_task == {e}) ORDER BY cpu_bench DESC').fetchone()[0]
        socket = cursor.execute(f'SELECT cpu_socket FROM cpu WHERE cpu_name == \'{rcpu}\' ').fetchone()[0]
        rgpu = cursor.execute(f'SELECT gpu_name FROM gpu WHERE gpu_price == {a} AND gpu_task == {b} ').fetchone()[0]
        mb = cursor.execute(f'SELECT mb_name FROM mother_board WHERE mb_socket == {socket} AND (mb_price == {a} OR mb_price == {3})').fetchone()[0]
        rram = cursor.execute(f'SELECT ram_name FROM ram WHERE ram_price == {a}').fetchone()[0]
        cputdp = cursor.execute(f'SELECT cpu_tdp FROM cpu WHERE cpu_name == \'{rcpu}\' ').fetchone()[0]
        gputdp = cursor.execute(f'SELECT gpu_tdp FROM gpu WHERE gpu_name == \'{rgpu}\' ').fetchone()[0]
        bp = cursor.execute(f'SELECT bp_name FROM bp WHERE bp_power > {cputdp + gputdp + 150}').fetchone()[0]

        bot.send_message(message.chat.id, f'В таком случае вам подходит процессор {splt(rcpu)}, в связке с видеокартой {rgpu}, с {c} Гб оперативной памяти серии {rram}, на базе материнской платы {mb}. Питать это будет блок питания {bp} ',reply_markup=types.ReplyKeyboardRemove())


bot.polling(none_stop=True)
