import collections

Scientist = collections.namedtuple('Scientist', ['name', 'field', 'born', 'nobel'])

scientists = (
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
    Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False),
)

# crée un iterator qui applique la fonction à chaque élément de l'iterable
scientists_name_and_age = map(lambda scientist: (scientist.name, 2021 - scientist.born), scientists)

# utilise l'iterator pour afficher chaque nouvel élément généré
for scientist in scientists_name_and_age:
    print(scientist)

print(next(scientists_name_and_age)) # provoque une exception StopITeration
