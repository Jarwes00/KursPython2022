# POP - usuwa element z listy
# pamiętać o self.

class Queue:
    def __init__(self, fifo):
        self.fifo = fifo

    def __str__(self):
        return self.fifo

    def is_empty(self):
        return len(self.fifo) == 0

    def put(self, item):
        self.fifo.append(item)
        print(f"dodano {item}!")

    def get(self):
        return self.fifo.pop(0)


kolejka = Queue([3, 4, 5, 6, 7])

print(kolejka)



