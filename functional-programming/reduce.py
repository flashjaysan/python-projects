import collections
import functools

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

# crée une unique valeur en appliquant une fonction à deux arguments sur les éléments de l'iterable
scientists_total_age = functools.reduce(lambda accumulator, scientist: accumulator + 2021 - scientist.born, scientists, 0)

# affiche la valeur
print(scientists_total_age)

def reducer(accumulator, scientist):
    accumulator[scientist.field].append(scientist.name)
    return accumulator

scientists_by_field = functools.reduce(reducer, scientists, {'math': [], 'physics': [], 'astronomy': [], 'chemistry': []})

print(scientists_by_field)
