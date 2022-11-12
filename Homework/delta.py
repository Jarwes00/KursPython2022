# Stwórz moduł, który przechowuje wzór na deltę. Skorzystaj z wbudowanego modułu math.
# W nowym pliku wykorzystaj moduł.

import math

def get_parameters():
    a = int(input("bok a > "))
    b = int(input("bok b > "))
    c = int(input("bok c > "))
    return a, b, c

# Return the value of X raised to the power of X (POW)

def calculate_delta(a, b, c):
    delta = pow(b, 2) - 4 * a * c
    return delta

def main():
    x, y, z = get_parameters()
    result = calculate_delta(x, y, z)
    print(result)

if __name__ == '__main__':
    main()