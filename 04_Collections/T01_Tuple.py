#Stwórz krotkę zawierającą dane twojego pupila (rodzaj zwierzecia, rasa, jak się wabi).
# Następnie rozpakuj tę krotkę na pojedyńcze zmienne.
# Wykorzystaj zmienne do wyświetlenia f-stringa, tak by mogło powstać zdanie np. “Mój pies, rasy border collie wabi się Dyzio”.

dogs = ("pies", "border collie", "dyzio")
(zwierze, rasa, nazwa) = dogs

print(f"Moj {zwierze} rasy {rasa} wabi sie {nazwa}")


