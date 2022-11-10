def sum_naturals_for(n):
    sum_numbers = 0
    for nr in range(1, n+1):
        sum_numbers = sum_numbers + nr

    return sum_numbers

def sum_naturals_while(n):
    sum_numbers = 0
    while n > 0:
        sum_numbers = sum_numbers + n
        n = n - 1

    return sum_numbers

print(sum_naturals_while(10))