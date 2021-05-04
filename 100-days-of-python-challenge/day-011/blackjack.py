import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def draw_card():
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(deck)


def blackjack():
    print(logo)
    
    player_cards = []
    player_cards.append(draw_card())
    player_cards.append(draw_card())
    player_score = sum(player_cards)
    if player_score > 21:
        player_cards[0] = 1
        player_score = sum(player_cards)
    print(f'Your current hand: {player_cards}')
    print(f'Your current score: {player_score}')
    
    dealer_cards = []
    dealer_cards.append(draw_card())
    dealer_cards.append(draw_card())
    dealer_score = sum(dealer_cards)
    if dealer_score > 21:
        dealer_cards[1] = 1
        dealer_score = sum(dealer_cards)
    print(f'Dealer\'s first card: [{dealer_cards[0]}]')
    
    if player_score == 21:
        if dealer_cards[0] != 11:
            print('Blackjack! You win!')
        else:
            print('Let\'s see the dealer\'s next card...')
            print(f'Dealer\'s second card: [{dealer_cards[1]}]')
            print(f'Dealer\'s score: {dealer_score}')
            if dealer_score == 21:
                print('It\' a draw!')
            else:
                print('Blackjack! You win!')
    else:
        new_card = True
        while new_card:
            get_new_card = input('Type \'y\' to get another card or \'n\' to pass: ')
            if get_new_card == 'y':
                player_cards.append(draw_card())
                player_score = sum(player_cards)
                if player_score > 21:
                    if 11 in player_cards:
                        player_cards[player_cards.index(11)] = 1
                        player_score = sum(player_cards)
                    else:
                        new_card = False
            else:
                new_card = False
                
        print(f'Your final hand: {player_cards}')
        print(f'Your final score: {player_score}')
        if player_score > 21:
            print('Busted! You lose.')
        else:
            if dealer_score < 17:
                dealer_cards.append(draw_card())
                dealer_score = sum(dealer_cards)
            if dealer_score > 21:
                if 11 in dealer_cards:
                    dealer_cards[dealer_cards.index(11)] = 1
                    dealer_score = sum(dealer_cards)
            print(f'Dealer\'s final hand: {dealer_cards}')
            print(f'Dealer\'s final score: {dealer_score}')
            if dealer_score > 21:
                print('Dealer\'s Busted! You win!')
            else:
                if dealer_score < player_score:
                    print('You\'re closer to 21. You win.')
                elif dealer_score > player_score:
                    print('Dealer\'s closer to 21. You lose.')
                else:
                    print('It\'s a draw.')


def main():
    exit_game = False
    while not exit_game:
        play = input('Do you want to play a game of Blackjack? Type \'y\' or \'n\': ')
        if play == 'y':
            blackjack()
        else:
            exit_game = True
            print('Good bye.')


main()
