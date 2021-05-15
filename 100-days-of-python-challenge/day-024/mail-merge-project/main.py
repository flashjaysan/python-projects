with open('Input/Letters/starting_letter.txt') as file:
    starting_letter = file.read()
with open('Input/Names/invited_names.txt') as file:
    names = file.read().split('\n')
for name in names:
    new_letter = starting_letter.replace('[name]', name)
    with open(f'Output/ReadyToSend/letter_to_{name.lower()}.txt', 'w') as file:
        file.write(new_letter)
