# C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit Źle

fahr = 0
while fahr <= 200:
    celc = 5 / 9 * (fahr - 32)
    celc = round(celc, 2)
    print(f"{celc} st C ->  {fahr} st Fahrenheit'a")
    fahr += 20

for fahr in range(0, 201, 20):
    celc = 5 / 9 * (fahr - 32)
    celc = round(celc, 2)
    print(f"{celc} st C ->  {fahr} st Fahrenheit'a")
