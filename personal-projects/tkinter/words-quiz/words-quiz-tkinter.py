import word
import dictionary
import tkinter


class WordsQuizTkinter:

    def __init__(self):
        self.dictionary = dictionary.Dictionary()
        self.dictionary.load_dictionary('japonais.csv')

        self.show_furigana = True
        self.show_roumaji = True

        self.root = tkinter.Tk()
        self.root.title('Words Quiz')
        self.root.config(padx=20, pady=20)
        self.root.bind('<Return>', self.check)

        self.menubar = tkinter.Menu(self.root)
        self.menu = tkinter.Menu(self.menubar, tearoff=0)
        self.menu.add_command(label="Furigana", command=self.set_furigana)
        self.menu.add_command(label="Roumaji", command=self.set_roumaji)
        self.menubar.add_cascade(label="Select", menu=self.menu)
        self.root['menu'] = self.menubar

        self.native = tkinter.Label(self.root)
        self.native['font'] = ('Arial', 20)
        self.native.pack()

        self.alternate = tkinter.Label(self.root)
        self.alternate['font'] = ('Arial', 10)
        self.alternate.pack()

        self.latin = tkinter.Label(self.root)
        self.latin['font'] = ('Arial', 10)
        self.latin.pack()

        self.entry = tkinter.Entry(self.root)
        self.entry['justify'] = 'center'
        self.entry.pack()

        self.button = tkinter.Button(self.root, text='Check')
        self.button.pack_configure(pady=10)
        self.button.pack()
        self.button['command'] = self.check

        self.new_random_word()

        self.root.mainloop()

    def check(self, *args):
        if self.entry.get() == self.random_word.translation:
            self.new_random_word()
        self.entry.delete(0, tkinter.END)

    def new_random_word(self):
        self.random_word = self.dictionary.get_random_word()
        self.native['text'] = self.random_word.native
        if self.show_furigana:
            self.alternate['text'] = self.random_word.alternate
        else:
            self.alternate['text'] = ''
        if self.show_roumaji:
            self.latin['text'] = self.random_word.latin
        else:
            self.latin['text'] = ''

    def set_furigana(self):
        self.show_furigana = not self.show_furigana
        if self.show_furigana:
            self.alternate['text'] = self.random_word.alternate
        else:
            self.alternate['text'] = ''

    def set_roumaji(self):
        self.show_roumaji = not self.show_roumaji
        if self.show_roumaji:
            self.latin['text'] = self.random_word.latin
        else:
            self.latin['text'] = ''


if __name__ == '__main__':
    WordsQuizTkinter()
