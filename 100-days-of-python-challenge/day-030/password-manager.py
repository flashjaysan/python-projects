import random
import pyperclip
import tkinter
import tkinter.messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_digits = [random.choice(digits) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_digits
    random.shuffle(password_list)

    return ''.join(password_list)
# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
root = tkinter.Tk()
root.title('Password Manager')
root.config(padx=50, pady=50, bg='white')

canvas = tkinter.Canvas(width=200, height=200, bg='white', highlightthickness=0)
logo = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=2, row=1)

website_label = tkinter.Label(text='Website:', bg='white')
website_label.grid(column=1, row=2, sticky='e')

website_entry = tkinter.Entry(bg='white', width=35)
website_entry.grid(column=2, row=2, columnspan=2, sticky=tkinter.NW + tkinter.SE)
website_entry.focus()

email_label = tkinter.Label(text='Email/Username:', bg='white')
email_label.grid(column=1, row=3, sticky='e')

email_entry = tkinter.Entry(bg='white', width=35)
email_entry.grid(column=2, row=3, sticky=tkinter.NW + tkinter.SE, columnspan=2)
email_entry.insert(0, '@gmail.com')

password_label = tkinter.Label(text='Password:', bg='white')
password_label.grid(column=1, row=4, sticky='e')

password_entry = tkinter.Entry(bg='white', width=21)
password_entry.grid(column=2, row=4, sticky=tkinter.NW + tkinter.SE)


def generate_password_gui():
    password_entry.delete(0, tkinter.END)
    password = generate_password()
    password_entry.insert(0, password)
    pyperclip.copy(password)


password_button = tkinter.Button(text='Generate Password', bg='white', command=generate_password_gui)
password_button.grid(column=3, row=4, sticky=tkinter.NW + tkinter.SE)


def save():
    site = website_entry.get()
    login = email_entry.get()
    password = password_entry.get()
    new_data = {
        site: {
            'email': login,
            'password': password,
        }
    }


    if len(site) == 0 or len(login) == 0 or len(password) == 0:
        tkinter.messagebox.showinfo(title='Invalid data', message='Some fields are empty.')
    else:
        with open('passwords.json', 'r') as file:
            data = json.load(file)
            data.update(new_data)
        with open('passwords.json', 'w') as file:
            json.dump(data, file, indent=4)
        website_entry.delete(0, tkinter.END)
        password_entry.delete(0, tkinter.END)


add_button = tkinter.Button(text='Add', bg='white', width=36, command=save)
add_button.grid(column=2, row=5, columnspan=2, sticky=tkinter.NW + tkinter.SE)

root.mainloop()
