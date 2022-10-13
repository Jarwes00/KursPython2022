my_list = ["Ada", "Ruby", "Julia", "Violetta"]

lenght = len(my_list)
for index in range(lenght):
    print(index, ":", my_list[index])

pa = ''
magic = 'hokuspokus'
for num in range(2, 10, 2):
    pa = pa + str(num) + magic[num]
    print(pa)