txt = ‘897342jndfjsahhlnASDF’

txt.isdigit() #sprawdza, czy jest liczbą
txt.center(width, [between]) #szerokość od środka, ‘co w te luki’
txt.rstrip(‘a’) #usuwa A dopóki nie trafi na inną

# Czy w TXT są duże litery?

print( txt.isalpha() and not txt.islower()) - #Czy posiada liczby w sobie I NIE  są małe litery