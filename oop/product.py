class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name},{self.price}"

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __int__(self):
        return self.price


if __name__ == '__main__':
    p1 = Product("Dell Laptop", 60000)
    p2 = Product("Dell Laptop", 60000)
    print(p1)  # str(p1)  -> p1.__str__()
    print(p1 >= p2)
    print( int(p1) + int(p2))
