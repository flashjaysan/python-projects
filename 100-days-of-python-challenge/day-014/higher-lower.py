import art
import game_data
import random


def higher_lower():
    print(art.logo)
    score = 0
    gameover = False
    while not gameover:
        option_a = random.choice(game_data.data)
        option_b = random.choice(game_data.data)
        while option_a == option_b:
            option_b = random.choice(game_data.data)
        print(f'Compare A: {option_a["name"]}, a {option_a["description"]}, from {option_a["country"]}.')
        #print(f'{option_a["follower_count"]}')
        print(art.vs)
        print(f'Against B: {option_b["name"]}, a {option_b["description"]}, from {option_b["country"]}.')
        #print(f'{option_b["follower_count"]}')
        answer = input('Who has more followers? Type \'A\' or \'B\': ').lower()
        if (option_a['follower_count'] > option_b['follower_count'] and answer == 'a') or (option_b['follower_count'] > option_a['follower_count'] and answer == 'b'):
            score += 1
            print(f'You\'re right! Current score: {score}.')
        else:
            print(f'Sorry, that\'s wrong. Final score: {score}.')
            gameover = True


def main():
    still_play = True
    while still_play:
        higher_lower()
        new_game_answer = input('Do you want to play again? \'y\' or \'n\': ')
        if new_game_answer != 'y':
            still_play = False


main()
