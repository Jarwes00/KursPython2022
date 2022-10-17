#  W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.
# """Szybko, zbudź się, szybko, wstawaj
# Szybko, szybko, stygnie kawa
 #Szybko, zęby myj i ręce

txt = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

txt = txt.lower()
txt = txt.replace(',', '')
txt = txt.split()

uniq_word = set(txt)
for word in uniq_word:
    print(f"{word} -> {txt.count(word)}")


