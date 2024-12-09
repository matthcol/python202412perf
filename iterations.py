# iterable objects

from itertools import chain


cities = [
    'Toulouse',
    'Grenoble',
    'Aix-en-Provence',
    'Montpellier',
]

cities2 = [
    'Bayonne',
    'Marseille',
    'Lyon',
    'Bordeaux',
]

# instruction for
for city in cities:
    print(city)

# expression for: list comprehension
cities_u = [ city.upper() for city in cities ]
print(cities_u)

# expression for: generator expression
length_generator = (len(city) for city in cities)
# repr: <generator object <genexpr> at 0x0000022F5D474040>
letter_count = sum(length_generator)
print(letter_count)

# same thing
letter_count = sum(len(city) for city in cities)
print(letter_count)

letter_count = sum((len(city) for city in cities), start=1000)
print(letter_count)

# expression for: dict comprehension
city_length_dict = { city: len(city) for city in cities }
print(city_length_dict) # {'Toulouse': 8, 'Grenoble': 8, 'Aix-en-Provence': 15, 'Montpellier': 11}

# enumerate:
print()
for i, city in enumerate(cities):
    print(f"#{i}# {city}")

print()
for i, city in enumerate(cities, start=1):
    print(f"#{i}# {city}")

# ! avoid index indirection:
print()
for i in range(len(cities)):
    print(f"#{i}# {cities[i]}")

# iterate with zip
print()
for city, n, letter in zip(cities, range(1,1000), 'abcdefghijklmnopqrstuvwxyz'):
    print(f"#{city}#{n}#{letter}")

# chain of iterables (module itertools)
print()
for city in chain(cities, cities2):
    print(city)

# Recap: builtin functions with arg iterable
# list, tuple, dict
# map, filter
# sum, min, max
# any, all
# enumerate, zip, 
# reversed, sorted
# iter (-> iterator)
print()
print(
    "are all city lengths > 5:",
    all(len(city) > 5 for city in cities)
)
print(
    "is any city with length > 10",
    any(len(city) > 10 for city in cities)
)

print()
city_d = dict([
    ('name', 'Toulouse'),
    ('population', 477_000),
    ('zipcode', '31000')
])
print(city_d)

city_d = dict(
    name='Toulouse',
    population=477_000,
    zipcode='31000'
)
print(city_d)
# {'name': 'Toulouse', 'population': 477000, 'zipcode': '31000'}