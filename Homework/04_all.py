# Napisz grę - kamień (k) / papier (p) / nożyce (n).

import random

kpn = ['kamien', 'papier', 'nożyce']

komputer = random.choice(kpn)


while True:
    gracz = input('wybierz kamień (k) / papier (p) / nożyce (n)')
    if gracz == "k":
        gracz = 'kamień'
        break
    elif gracz == 'p':
        gracz = "papier"
        break
    elif gracz == 'n':
        gracz = 'nożyce'
        break

if komputer == gracz:
    print('remis')
elif komputer == 'kamień' and gracz == 'nożyce':
    print('wygrywa komputer')
elif komputer == 'kamień' and gracz == 'papier':
    print('wygrywasz!')
elif komputer == 'papier' and gracz == 'kamień':
    print('wygrywa komputer')
elif komputer == 'papier' and gracz == 'nożyce':
    print('wygrywasz!')
elif komputer == 'nożyce' and gracz == 'kamień':
    print('wygrywasz!')
elif komputer == 'nożyce' and gracz == 'papier':
    print('komputer wygrywa')