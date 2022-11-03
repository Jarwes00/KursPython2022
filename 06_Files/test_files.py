#f = open("text.txt")
#print(f.readline())
#f.close()
#with open("zapis.txt", mode="a") as fw:
    #fw.write('changes')

f = 'tekst.txt'

with open(f, encoding="utf-8") as f:
    content = f.readlines()
    print(content)

