import tkinter
import pandas
import random


class FlashCards:

    BACKGROUND_COLOR = "#B1DDC6"

    def __init__(self):
        try:
            data = pandas.read_csv('data/words_to_learn.csv')
        except FileNotFoundError:
            data = pandas.read_csv('data/french_words.csv')
        self.words_list = data.to_dict(orient="records")

        self.word = None
        self.after_id = None

        self.root = tkinter.Tk()
        self.root.config(bg=FlashCards.BACKGROUND_COLOR, padx=50, pady=50)
        self.root.title('Flashcards')

        self.canvas = tkinter.Canvas(width=800, height=526, bg=FlashCards.BACKGROUND_COLOR, highlightthickness=0, bd=0)
        self.canvas.grid(row=0, column=0, columnspan=2)

        self.image_card_front = tkinter.PhotoImage(file="images/card_front.png")
        self.image_card_back = tkinter.PhotoImage(file="images/card_back.png")
        self.canvas_image_card = self.canvas.create_image(400, 263, image=self.image_card_front)
        self.canvas_language_text = self.canvas.create_text(400, 150, font=('Ariel', 40, 'italic'), text='')
        self.canvas_word_text = self.canvas.create_text(400, 263, font=('Ariel', 60, 'bold'), text='')

        image_wrong = tkinter.PhotoImage(file="images/wrong.png")
        button_wrong = tkinter.Button(image=image_wrong, highlightthickness=0, bd=0, relief='flat', command=self.wrong)
        button_wrong.grid(row=1, column=0)

        image_right = tkinter.PhotoImage(file="images/right.png")
        button_right = tkinter.Button(image=image_right, highlightthickness=0, bd=0, relief='flat', command=self.right)
        button_right.grid(row=1, column=1)

        self.new_word()

        self.root.mainloop()

    def wrong(self):
        self.root.after_cancel(self.after_id)
        self.new_word()

    def right(self):
        self.root.after_cancel(self.after_id)
        self.remove_current_word()
        self.new_word()

    def remove_current_word(self):
        self.words_list.remove(self.word)
        data_frame = pandas.DataFrame(self.words_list)
        data_frame.to_csv('data/words_to_learn.csv', index=False)

    def new_word(self):
        self.word = random.choice(self.words_list)
        self.canvas.itemconfigure(self.canvas_language_text, text='French', fill='black')
        self.canvas.itemconfigure(self.canvas_word_text, text=self.word['French'], fill='black')
        self.canvas.itemconfigure(self.canvas_image_card, image=self.image_card_front)
        self.after_id = self.root.after(3000, self.switch_image)

    def switch_image(self):
        self.canvas.itemconfigure(self.canvas_language_text, text='English', fill='white')
        self.canvas.itemconfigure(self.canvas_word_text, text=self.word['English'], fill='white')
        self.canvas.itemconfigure(self.canvas_image_card, image=self.image_card_back)


if __name__ == '__main__':
    FlashCards()
