import word
import random


class Dictionary:

    def __init__(self):
        self.words = []

    def add_word(self, new_word):
        if new_word not in self.words:
            self.words.append(new_word)

    def load_dictionary(self, filename):
        with open(filename, encoding='utf8') as file:
            lines = file.readlines()
            for line in lines:
                word_parts = line.split(',')
                native = word_parts[0]
                alternate = word_parts[1]
                latin = word_parts[2]
                translation = word_parts[3].strip()
                new_word = word.Word(native, alternate, latin, translation)
                self.add_word(new_word)

    def get_random_word(self):
        return random.choice(self.words)
