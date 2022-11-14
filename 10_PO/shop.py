class Shop:
    def __init__(self, items: list) -> None:
        self.items = items

    def show_product(self, item_id):
        try:
            product, size = self.items[item_id]
            print(f"{product} - rozmiar {size}")
        except (IndexError, TypeError):
            print('Nie ma produktu o takim id')

    def try_product(self, item_id, user_size):
        try:
            product, size = self.items[item_id]
            if size == user_size:
                print("Rozmiar pasuje")
            else:
                print("To nie ten rozmiar")
        except (IndexError, TypeError):
            print("Nie ma produktu o takim id")

#            VVV Do analizy VVV

    def buy_product(self, item_id):
        try:
            print(self.items[item_id])
            product, size = self.items[item_id]
            self.items.pop(product)
        except (IndexError, TypeError):
            print("Nie ma takiego produktu")

    def return_product(self, product):
        if len(product) == 2:
            self.items.append(product)
            print("Dokonano zwrotu!")
        else:
            "to nie jest produkt"


fashionshop = Shop([
    ["tshirt", "S"],
    ["dress", "L"],
    ["shorts", "M"]
])

fashionshop.show_product(2)
fashionshop.try_product(2, 'XL')