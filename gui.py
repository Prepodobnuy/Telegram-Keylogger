from tkinter import *
import os


class App(Tk):
    def __init__(self):
        super().__init__()

        self.resizable(False, False)

        self.entryToken = Entry()
        self.entryChatid = Entry()
        self.entryName = Entry()

        self.labelToken = Label(text='Token:')
        self.labelChatid = Label(text='Chat id:')
        self.labelName = Label(text='Name:')

        self.buttonstart = Button(text='Start', command=self.start, width=5, height=1)
    
        self.entryToken.grid(row=1, column=0)
        self.entryChatid.grid(row=3, column=0)
        self.entryName.grid(row=5, column=0)

        self.labelToken.grid(row=0, column=0, columnspan=2)
        self.labelChatid.grid(row=2, column=0, columnspan=2)
        self.labelName.grid(row=4, column=0, columnspan=2)

        self.buttonstart.grid(row=5, column=3)
    
    def start(self):
        token = str(self.entryToken.get())
        chatid = str(self.entryChatid.get())
        fakename = str(self.entryName.get())
        
        with open('conf', 'w+') as file:
            file.write(f'{token}\n{chatid}\n{fakename}')
                
        os.system('install.py')
        os.remove('conf')    

if __name__ == '__main__':
    app = App()
    app.mainloop()