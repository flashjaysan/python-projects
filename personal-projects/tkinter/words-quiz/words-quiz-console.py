import word
import dictionary


class WordsQuizConsole:
    def __init__(self):
        self.dictionary = dictionary.Dictionary()

    def main(self):
        print('Welcome in Words Quiz.')
        print('Chargement du dictionnaire.')
        self.dictionary.load_dictionary('japonais.csv')
        end = False
        while not end:
            random_word = self.dictionary.get_random_word()
            print(random_word.native)
            print(random_word.alternate)
            print(random_word.latin)
            translation = input('Traduction : ')
            if translation == random_word.translation:
                print('Correct !')
            else:
                print(f'Faux ! La traduction était: {random_word.translation}.')


if __name__ == '__main__':
    WordsQuizConsole().main()
