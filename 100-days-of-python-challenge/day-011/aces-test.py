cards = [8, 8, 5, 11]
print(cards)

while sum(cards) > 21 and 11 in cards:
    index = cards.index(11)
    cards[index] = 1
    print('cards changed: ', cards)

print('end of loop: ', cards)
