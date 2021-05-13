from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ['Name', 'Number', 'Category']

table.add_row(['Bulbazaur', 1, 'Seed'])
table.add_row(['Ivysaur', 2, 'Seed'])
table.add_row(['Venusaur', 3, 'Seed'])
table.add_row(['Charmander', 4, 'Lizard'])
table.add_row(['Charmeleon', 5, 'Flame'])
table.add_row(['Charizard', 6, 'Flame'])
table.add_row(['Squirtle', 7, 'Tiny turtle'])
table.add_row(['Wartortle', 8, 'Turtle'])
table.add_row(['Blastoise', 9, 'Shellfish'])

print(table)
