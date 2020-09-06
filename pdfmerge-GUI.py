from tkinter import * 
from tkinter.ttk import * 

bgColor='#ff3333'

class Janela:
    def __init__(self, window):
        window.title('PDFMerge - EM DESENVOLVIMENTO')
        window.geometry('600x450')
        window.resizable(False, False)
        window.configure(bg=bgColor)

        self.style = Style() 

        self.style.configure('W.TButton', font = ('calibri', 10))

        self.mainframe = Frame(window)

        self.title = Label(self.mainframe, text="PDFMerge")

        self.btChoose = Button(self.mainframe, text="Escolher Pasta", style = 'W.TButton')

        self.packWidgets()

    def packWidgets(self):
        self.mainframe.pack()

        self.title.pack()
        self.btChoose.pack()

root = Tk()
Janela(root)
root.mainloop()