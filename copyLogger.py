import shutil
from time import sleep


def copy():
    file = open('name.txt')
    copyName = str(file.readline())
    file.close()

    end = 'Copy created successfully'

    try:
        shutil.copyfile('main.exe', f'{str(copyName)}.exe')
    except BaseException:
        end = 'Copy not created due to error'

    print(end)
    sleep(0.2)

if __name__ == '__main__':
    copy()