import tkinter


class PomodoroTimer:

    PINK = "#e2979c"
    RED = "#e7305b"
    GREEN = "#9bdeac"
    YELLOW = "#f7f5dd"
    FONT_NAME = "Courier"
    WORK_MIN = 25
    SHORT_BREAK_MIN = 5
    LONG_BREAK_MIN = 20
    CHECK_MARK = '✔️'

    def __init__(self):
        self.reps = 0
        self.time_color = PomodoroTimer.YELLOW
        self.check_marks_string = ''
        self.timer_id = None

        self.root = tkinter.Tk()
        self.root.title('Pomodoro timer')
        self.root.config(padx=100, pady=50, bg=PomodoroTimer.YELLOW)

        self.title_label = tkinter.Label(text='Timer', fg=PomodoroTimer.GREEN, bg=PomodoroTimer.YELLOW, font=(PomodoroTimer.FONT_NAME, 50, 'bold'))
        self.title_label.grid(column=2, row=1)

        self.canvas = tkinter.Canvas(width=200, height=224, bg=PomodoroTimer.YELLOW, highlightthickness=0)
        self.tomato = tkinter.PhotoImage(file='tomato.png')
        self.canvas.create_image(100, 112, image=self.tomato)
        self.timer_text = self.canvas.create_text(100, 130, text='00:00', fill=PomodoroTimer.YELLOW, font=(PomodoroTimer.FONT_NAME, 35, 'bold'))
        self.canvas.grid(column=2, row=2)

        self.start_button = tkinter.Button(text='Start', command=self.start_timer)
        self.start_button.grid(column=1, row=3)

        self.reset_button = tkinter.Button(text='Reset', command=self.reset)
        self.reset_button.grid(column=3, row=3)

        self.check_marks_label = tkinter.Label(text=self.check_marks_string, bg=PomodoroTimer.YELLOW, fg=PomodoroTimer.GREEN, highlightthickness=0)
        self.check_marks_label.grid(column=2, row=4)

        self.reset()

        self.root.mainloop()

    def count_down(self, count):
        self.canvas.itemconfig(self.timer_text, text=f'{int(count / 60):02d}:{count % 60:02d}')
        if count > 0:
            self.timer_id = self.root.after(1000, self.count_down, count - 1)
        else:
            if self.reps < 8:
                self.start_timer()

    def start_timer(self):
        if self.reps == 0 or self.reps == 2 or self.reps == 4 or self.reps == 6:
            time = PomodoroTimer.WORK_MIN
            self.title_label.config(text='Work', fg=PomodoroTimer.GREEN)
        elif self.reps == 1 or self.reps == 3 or self.reps == 5:
            time = PomodoroTimer.SHORT_BREAK_MIN
            self.check_marks_string += PomodoroTimer.CHECK_MARK
            self.check_marks_label.config(text=self.check_marks_string)
            self.title_label.config(text='Break', fg=PomodoroTimer.RED)
        elif self.reps == 7:
            time = PomodoroTimer.LONG_BREAK_MIN
            self.title_label.config(text='End', fg=PomodoroTimer.PINK)
        else:
            time = 0
        self.reps += 1
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
        self.count_down(time * 60)

    def reset(self):
        self.reps = 0
        self.time_color = PomodoroTimer.YELLOW
        self.check_marks_string = ''
        self.check_marks_label.config(text=self.check_marks_string)
        self.title_label.config(text='Timer', fg=PomodoroTimer.GREEN)
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
            self.canvas.itemconfig(self.timer_text, text='00:00')


if __name__ == '__main__':
    PomodoroTimer()
