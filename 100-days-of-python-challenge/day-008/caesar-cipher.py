alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    if cipher_direction == 'decode':
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            position %= len(alphabet)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f'Here\'s the {cipher_direction}d result: {end_text}')


def cipher():
    direction = input('Type \'encode\' to encrypt, type \'decode\' to decrypt:\n')
    text = input('Type your message:\n').lower()
    shift = int(input('Type the shift number:\n'))
    shift %= len(alphabet)
    print(f'Shift value: {shift}')
    caesar(text, shift, direction)


import art

print(art.logo)
loop = True
while(loop):
    cipher()
    loop_answer = input('Do you want to continue? Yes or no:\n').lower()
    if loop_answer == 'no':
        loop = False
        