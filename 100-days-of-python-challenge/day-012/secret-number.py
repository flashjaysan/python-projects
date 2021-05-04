import random

logo = '''
 _____                 _                    _           
|   __|___ ___ ___ ___| |_    ___ _ _ _____| |_ ___ ___ 
|__   | -_|  _|  _| -_|  _|  |   | | |     | . | -_|  _|
|_____|___|___|_| |___|_|    |_|_|___|_|_|_|___|___|_| 
'''


def secret_number():
    print(logo)
    
    number = random.randint(1, 100)
    print('I chose a number between 1 and 100. Guess it.')
    
    print('Select a difficulty:')
    print('\teasy\t(10 tries)')
    print('\tnormal\t(7 tries)')
    print('\thard\t(5 tries)')
    difficulty = input('Difficulty? ')
    if difficulty == 'easy':
        tries = 10
    elif difficulty == 'normal':
        tries = 7
    else:
        tries = 5
        
    gameover = False
    while not gameover:
        print(f'You have {tries} tries left.')
        guess = int(input('Your guess? '))
        if guess == number:
            print('You found the right number. You won.')
            gameover = True
        else:
            if guess > number:
                print('Too high.')
            else:
                print('Too low.')
            tries -= 1
            if tries == 0:
                print('You have no more tries left. You lost.')
                gameover = True


def main():
    keep_playing = True
    while keep_playing:
        secret_number()
        keep_playing_answer = input('Do you want to play again? \'y\' or \'n\': ')
        if keep_playing_answer != 'y':
            keep_playing = False


main()

