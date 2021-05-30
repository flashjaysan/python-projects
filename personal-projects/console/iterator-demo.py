# Une liste est un iterable
cities = ["Paris", "Lyon", "Marseille"]

# A partir d'un iterable, on crée un iterator
iterator_obj = iter(cities)

# On récupère l'élément suivant de l'iterable en utilisant la fonction next sur l'iterator
print(next(iterator_obj)) # affiche Paris
print(next(iterator_obj)) # affiche Lyon
print(next(iterator_obj)) # affiche Marseille

# la fonction next provoque une exception StopIteration lorsqu'il n'y a plus d'éléments à parcourir
print(next(iterator_obj)) # provoque une exception StopIteration
