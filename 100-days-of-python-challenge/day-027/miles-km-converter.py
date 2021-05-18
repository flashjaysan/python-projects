import tkinter

root = tkinter.Tk()
root.title('Miles to Km Converter')
root.minsize(width=640, height=360)
root.config(padx=20, pady=20)

miles_input = tkinter.StringVar()
miles = tkinter.Entry(root, textvariable=miles_input)
miles.grid(row=0, column=1)

miles_label = tkinter.Label(root, text='miles')
miles_label.grid(row=0, column=2)

equal_label = tkinter.Label(root, text='is equal to')
equal_label.grid(row=1, column=0)

km = tkinter.Label(root, text='0')
km.grid(row=1, column=1)

km_label = tkinter.Label(root, text='kilometers')
km_label.grid(row=1, column=2)


def calculate():
    miles_string = miles_input.get()
    miles_number = int(miles_string)
    km_number = miles_number * 1.609344
    km['text'] = f'{km_number:.2f}'


calculate_button = tkinter.Button(root, text='Calculate', command=calculate)
calculate_button.grid(row=2, column=1)

root.mainloop()
