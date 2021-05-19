import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = '✔️'
reps = 0
time_color = YELLOW
check_marks_string = ''
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    global time_color
    global check_marks_string
    reps = 0
    time_color = YELLOW
    check_marks_string = ''
    check_marks_label.config(text=check_marks_string)
    title_label.config(text='Timer', fg=GREEN)
    if timer is not None:
        root.after_cancel(timer)
        canvas.itemconfig(timer_text, text='00:00')

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global time_color
    global check_marks_string
    if reps == 0 or reps == 2 or reps == 4 or reps == 6:
        time = WORK_MIN
        title_label.config(text='Work', fg=GREEN)
    elif reps == 1 or reps == 3 or reps == 5:
        time = SHORT_BREAK_MIN
        check_marks_string += CHECK_MARK
        check_marks_label.config(text=check_marks_string)
        title_label.config(text='Break', fg=RED)
    elif reps == 7:
        time = LONG_BREAK_MIN
        title_label.config(text='End', fg=PINK)
    else:
        time = 0
    reps += 1
    count_down(time * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    canvas.itemconfig(timer_text, text=f'{int(count / 60):02d}:{count % 60:02d}')
    if count > 0:
        timer = root.after(1000, count_down, count - 1)
    else:
        if reps < 8:
            start_timer()

# ---------------------------- UI SETUP ------------------------------- #
root = tkinter.Tk()
root.title('Pomodoro timer')
root.config(padx=100, pady=50, bg=YELLOW)

title_label = tkinter.Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, 'bold'))
title_label.grid(column=2, row=1)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text='00:00', fill=YELLOW, font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=2, row=2)

start_button = tkinter.Button(text='Start', command=start_timer)
start_button.grid(column=1, row=3)

reset_button = tkinter.Button(text='Reset', command=reset)
reset_button.grid(column=3, row=3)

check_marks_label = tkinter.Label(text=check_marks_string, bg=YELLOW, fg=GREEN, highlightthickness=0)
check_marks_label.grid(column=2, row=4)

reset()




root.mainloop()
