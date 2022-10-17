"""Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób, natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:

Dorota, Wellman, dziennikarka

Adam, Małysz, sportowiec

Robert, Lewandowski, piłkarz

Krystyna, Janda, aktorka"""

ludzie = [
    ["Dorota", "Welmmal", "dziennikarka"],
    ["Adam", "Małysz", "sportowiec"],
    ["robert", "Lewandowski", "piłkarz"],
    ["krystyna", "Janda", "aktorka"]
]
for row in ludzie:
    print(row[0], row[1], "-", row[2])

