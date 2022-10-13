#

password = input('wprowadz hasło')
if len(password) < 8 or len(password) > 24:
    print('długość hasła nieprawidłowa, oczekiwana pomiedzy 8, a 24 znaki')
if password.isdigit():
    print('musi skladac sie z litery')
if password.isalpha():
    print('musi zawierac cyfre')
if password.islower():
    print('haslo zawiera tylko male litery, a powinno zawierac conajmniej 1 duza litere')
if password.isupper():
    print('haslo zawiera tylko duze litery, a powinno zawierac conajmniej 1 małą litere')