from tkinter import *


def add_frame(root, side): 
    frame = Frame(root)
    frame.pack(side=side, expand=YES, fill=BOTH)
    return frame


def add_button(root, side, text, command=None):
    button = Button(root, text=text, command=command)
    button.pack(side=side, expand=YES, fill=BOTH)
    return button


class Calculator(Frame):
    
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Simple Calculator')
        self.master.iconname("calc1")
        
        display = StringVar()
        entry = Entry(self, relief=SUNKEN, textvariable=display)
        entry.pack(side=TOP, expand=YES, fill=BOTH)
        
        for keys in ("123", "456", "789", "-0."):
            key_frame = add_frame(self, TOP)
            for char in keys:
                add_button(key_frame, LEFT, char, lambda w=display, s=' %s '%char: w.set(w.get() + s))
        opsF = add_frame(self, TOP)
        for char in "+-*/=":
            if char == '=':
                button = add_button(opsF, LEFT, char)
                button.bind('<ButtonRelease-1>', lambda e, s=self, w=display: s.calc(w), '+')
            else:
                button = add_button(opsF, LEFT, char, lambda w=display, c=char: w.set(w.get() + ' ' + c + ' '))
                clear_frame = add_frame(self, BOTTOM)
                add_button(clear_frame, LEFT, 'Clr', lambda w=display: w.set(''))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except ValueError:
            display.set("ERROR")


if __name__ == '__main__':
    Calculator().mainloop()
    