import pandas

nato_alphabet_df = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet_dict = {row['letter']: row['code'] for (index, row) in nato_alphabet_df.iterrows()}

word = input('Enter a word: ')
nato_words = [nato_alphabet_dict[letter.upper()] for letter in word]
print(nato_words)
