import tkinter
import random
import pandas

kanas_df = pandas.read_csv('kanas.csv')
kanas = [{'romaji': row['romaji'], 'hiragana': row['hiragana'], 'katakana': row['katakana']} for (index, row) in kanas_df.iterrows()]
kana_type = 'hiragana'


def new_kana():
    return random.choice(kanas)


def set_hiragana():
    global kana_type
    kana_type = 'hiragana'


def set_katakana():
    global kana_type
    kana_type = 'katakana'


current_kana = new_kana()

root = tkinter.Tk()
root.title('Kanas quiz')
root.config(padx=20, pady=20)

menubar = tkinter.Menu(root)
menu = tkinter.Menu(menubar, tearoff=0)
menu.add_command(label="Hiragana", command=set_hiragana)
menu.add_command(label="Katakana", command=set_katakana)
menubar.add_cascade(label="Select", menu=menu)
root['menu'] = menubar

label = tkinter.Label(root)
label['font'] = ('Arial', 20)
label['text'] = current_kana['katakana']
label.pack()

entry = tkinter.Entry(root)
entry['justify'] = 'center'
entry.pack()


def check():
    global current_kana
    if entry.get() == current_kana['romaji']:
        current_kana = new_kana()
        label['text'] = current_kana[kana_type]
    entry.delete(0, tkinter.END)


button = tkinter.Button(root, text='Check')
button.pack()
button['command'] = check

root.mainloop()
