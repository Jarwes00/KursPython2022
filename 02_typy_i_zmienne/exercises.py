#1 Policz wszystkie znaki w napisie
quote = '"Honesty is the first chapter in the book of wisdom."'
print(len(quote)
    )
#2 Nie modyfikując zmiennej wyświetl słowo wisdom
print(quote[-7:-1])


#3 Wyświetl tylko pierwszą połowę tekstu ~źle

print(quote[0:len(quote)//2])

#4 Wyświetl tylko kropkę

print(quote[-1])

#5 Wyświetl od połowy tylko co trzecią literę cytatu ~ źle

print(quote[len(quote)//2: :3])

#6 Wyświetl ‘Hnsyi h is hpe ntebo fwso.’

print(quote[::2])

#7 Wyświetl cały cytat odwrotnie

print(quote[::-1])

#8 Zamień wisdom na słowo friendship
quote.replace('wisdom', 'friendship')

#9 Sprawdź czy podane zdanie jest palindromem (od tyłu daje to samo)

txt = input('wprowadź zdanie:'
              )
txt = txt.replace(" ", "")
txt = txt.lower()

print(txt == txt[::-1]
      )
