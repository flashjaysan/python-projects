import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
display = list('_' * word_length)
letters_tried = []
end_of_game = False
lives = 6

print(hangman_art.logo)

print(f'Pssst, the solution is {chosen_word}.')

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in letters_tried:
        print(f'You have already tried {guess}.')
    else:
        letters_tried.append(guess)
        for position in range(word_length):
            letter = chosen_word[position]
            if guess == letter:
                display[position] = letter

        if guess in chosen_word:
            print(f'{guess} is in the word. Good job.')
        else:
            print(f'{guess} isn\'t in the word. You lost a life.')
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")

    print(''.join(display))

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
