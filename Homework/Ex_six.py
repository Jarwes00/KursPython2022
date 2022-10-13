# 6.Przekopiuj zawartość import this do zmiennej.
s = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# Policz liczbę wystąpień słowa better.
print(s.count('better')
      )
# Usuń z tekstu symbol gwiazdki.
final_s = s.replace("*", ""
                    )
print(final_s
      )

# Zamień jedno wystąpienie explain na understand

final_replace = s.replace('explain', 'understand', 1
                          )
print(final_replace
      )

# Usuń spacje i połącz wszystkie słowa myślnikiem

final_spacebar = s.replace(' ', '-')

print(final_spacebar)

# Podziel tekst na osobne zdania za pomocą kropki

