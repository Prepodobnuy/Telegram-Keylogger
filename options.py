from fastInstall import install


def info():
    print('       ╭╮\n       ┃┃\n╭━━┳╮ ╭┫┃╭━━┳━━┳━━┳━━┳━╮\n┃╭╮┃┃ ┃┃┃┃╭╮┃╭╮┃╭╮┃┃━┫╭╯\n┃╰╯┃╰━╯┃╰┫╰╯┃╰╯┃╰╯┃┃━┫┃\n┃╭━┻━╮╭┻━┻━━┻━╮┣━╮┣━━┻╯\n┃┃ ╭━╯┃     ╭━╯┣━╯┃\n╰╯ ╰━━╯     ╰━━┻━━╯')
    print('----About--programm----\n--Author: https://github.com/Prepodobnuy\n--Version: 2.1\n-----------------------')

def changeName():
    print('Enter new logger name below')
    ask = input('>>')

    file = open('name.txt', 'w')
    file.write(f'{ask}')
    file.close()
    print('\nName changed successfully\n')
    
def main():
    ask = input('>>')
    if ask == 'strt':
        install()
    elif ask == 'name':
        changeName()
    elif ask == 'help':
        print('\n---List of commands---\n-Change logger name: name\n-Install:            strt\n-Show this message:  help\n-About programm:     info')
    elif ask == 'info':
        info()

if __name__ == '__main__':
    print('       ╭╮\n       ┃┃\n╭━━┳╮ ╭┫┃╭━━┳━━┳━━┳━━┳━╮\n┃╭╮┃┃ ┃┃┃┃╭╮┃╭╮┃╭╮┃┃━┫╭╯\n┃╰╯┃╰━╯┃╰┫╰╯┃╰╯┃╰╯┃┃━┫┃\n┃╭━┻━╮╭┻━┻━━┻━╮┣━╮┣━━┻╯\n┃┃ ╭━╯┃     ╭━╯┣━╯┃\n╰╯ ╰━━╯     ╰━━┻━━╯')
    print('\n---List of commands---\n-Change logger name: name\n-Install:            strt\n-Show this message:  help\n-About programm:     info')
    while True:
        main()
