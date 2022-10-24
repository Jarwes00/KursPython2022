# Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.

lista = [23, 23, 45, 45, 1, 2, 3]
new_list = []
dup_list = []
for i in lista:
    if i not in new_list:
        new_list.append(i)
    else:
        dup_list.append(i)
print("Duplikaty ->", dup_list)
