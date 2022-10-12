#Dla podanej liczby w systemie dwójkowym bin_num = 1001111
#Zamianę z systemu binarnego na dziesiętny napisz samodzielnie (nie korzystaj z metody wbudowanej).

s = bin(int(input('zapisz liczbę w systemie dziesiętnym'))
          )
s = s.lstrip('-0b')
print(s)