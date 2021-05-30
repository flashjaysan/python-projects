import collections

# crée un nouveau type de donnée immutable
Scientist = collections.namedtuple('Scientist', ['name', 'field', 'born', 'nobel'])

# crée une instance immutable de ce nouveau type
ada = Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False)

# crée un tuple immutable de ce nouveau type immutable
scientists = (
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
    Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False),
)
