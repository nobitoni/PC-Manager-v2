from telebot import *
import os
import psutil
import pyautogui
import json

with open("config.json", 'r') as f:
    data = json.load(f)
    verified_users = data['users']
    bot = TeleBot(data['token'])


def start_bot():
    bot.polling()


@bot.message_handler(commands=['start'])
def cmd_start(message):
    if message.from_user.id in verified_users:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_turn_off = types.InlineKeyboardButton('выкл. пк')
        btn_hibernation_mode = types.InlineKeyboardButton('гибернация')
        btn_take_screenshot = types.InlineKeyboardButton('скрин')
        btn_block_windows = types.InlineKeyboardButton('lock')
        btn_battery_status = types.InlineKeyboardButton('акб')
        # btn_settings = types.InlineKeyboardButton('⚙️')
        markup.add(btn_battery_status, btn_take_screenshot, btn_block_windows,
                   btn_hibernation_mode, btn_turn_off)
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!',
                         reply_markup=markup)


@bot.message_handler(func=lambda message: message.text.lower() == 'выкл. пк')
def system_torn_off(message):
    if message.from_user.id in verified_users:
        try:
            bot.send_message(message.from_user.id, 'Выключаем..')
            os.system('shutdown /s /f /t 0')
        except Exception as e:
            bot.send_message(message.chat.id, f'Error:\n{e}')


@bot.message_handler(func=lambda message: message.text.lower() == 'гибернация')
def system_hibernation_mode(message):
    if message.from_user.id in verified_users:
        try:
            bot.send_message(message.from_user.id, 'Гибер.. Что? Да.')
            os.system('shutdown /h')
        except Exception as e:
            bot.send_message(message.from_user.id, f'Error:\n{e}')


@bot.message_handler(func=lambda message: message.text.lower() == 'акб')
def battery_status(message):
    if message.from_user.id in verified_users:
        try:
            battery = psutil.sensors_battery()
            percent = battery.percent
            charging = battery.power_plugged

            if charging:
                status = 'Заряжается'
            else:
                status = 'Не заряжается'

            response = f'Заряд аккумулятора: {percent}%\nСтатус: {status}'
            bot.send_message(message.chat.id, response)
        except Exception as e:
            bot.send_message(message.chat.id, f'Error:\n{e}')


@bot.message_handler(func=lambda message: message.text.lower() == 'скрин')
def take_screenshot(message):
    if message.chat.id in verified_users:
        try:
            bot.send_message(message.chat.id, "Делаем скриншот...")
            screenshot = pyautogui.screenshot()
            screenshot.save('screenshot.png')
            with open('screenshot.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
            os.remove("screenshot.png")
        except Exception as e:
            bot.send_message(message.chat.id, f'Error:\n{e}')


@bot.message_handler(func=lambda message: message.text.lower() == 'lock')
def block_windows(message):
    if message.from_user.id in verified_users:
        try:
            bot.send_message(message.from_user.id, 'Блокируем..')
            os.system('Rundll32.exe user32.dll,LockWorkStation')
        except Exception as e:
            bot.send_message(message.chat.id, f'Error:\n{e}')


'''
@bot.message_handler(func=lambda message: message.text.lower() == '⚙️')
def settings(message):
    if message.from_user.id in verified_users:
        try:
            settings_msg_text = (
                f"Включать бота при запуске = {turn_on_bot}"
                f"Верифицированные пользователи = {verified_users}"
            )
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_turn_on_bot = types.ReplyKeyboardMarkup()
            bot.send_message(message.chat.id, settings_msg_text)

        except Exception as e:
            bot.send_message(message.from_user.id, f'Error:\n{e}')
'''

if __name__ == '__main__':
    start_bot()