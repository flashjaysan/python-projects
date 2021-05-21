import tkinter


class Application(tkinter.Frame):
    
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tkinter.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()


app = Application()
app.master.title('Sample application')
app.mainloop()
