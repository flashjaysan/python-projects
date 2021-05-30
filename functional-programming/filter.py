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

# crée un iterator qui ne sélectionne que les scientifiques ayant un prix Nobel
nobel_scientists = filter(lambda x: x.nobel, scientists)

for scientist in nobel_scientists:
    print(scientist)

print(next(nobel_scientists)) # provoque une exception StopITeration


def filter_rewrite(function, iterable):
    return [item for item in iterable if function(item)]
