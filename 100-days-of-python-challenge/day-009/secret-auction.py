logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


def clear():
    for _ in range(50):
        print()


print(logo)

bidders = []

new_bidder = True

while new_bidder:
    name = input('What is your name? ')
    bid = int(input('What is your bid? $'))
    bidders.append(
        {
          'name': name,
          'bid': bid,
        }
    )
    new_bidder_answer = input('Add a new bidder? Yes or no. ').lower()
    new_bidder = new_bidder_answer != 'no'
    clear()

max_bid = 0
max_bidder = None
for bidder in bidders:
    if bidder['bid'] > max_bid:
        max_bidder = bidder
        max_bid = bidder['bid']

print(f'The winner is {max_bidder["name"]} with a bid of ${max_bidder["bid"]}.')
