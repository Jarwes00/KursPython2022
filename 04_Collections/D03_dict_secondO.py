#  W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.
# """Szybko, zbudź się, szybko, wstawaj
# Szybko, szybko, stygnie kawa
# Szybko, zęby myj i ręce

txt = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

txt = txt.lower()
txt = txt.replace(',', '')
txt = txt.split()

counting_dict = {}

for w in txt:
    if w not in counting_dict:
        counting_dict[w] = 1
    else:
        counting_dict[w] += 1

for k, v in counting_dict.items():
    print(k, ":", v)


