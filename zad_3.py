class Property:

    def __init__(self, area: float, rooms: int, price: float, address: str):
        self._area = area
        self._rooms = rooms
        self._price = price
        self._address = address

    def __str__(self):
        return f"""Property[
            Area: {self._area}
            Rooms: {self._rooms}
            Price: {self._price}
            Address: {self._address}
        ]"""

class House(Property):

    def __init__(self, area: float, rooms: int, price: float, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self._plot = plot

    def __str__(self):
        return f"""House[
            Area: {self._area}
            Rooms: {self._rooms}
            Price: {self._price}
            Address: {self._address}
            Plot: {self._plot}
        ]"""


class Flat(Property):

    def __init__(self, area: float, rooms: int, price: float, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self._floor = floor

    def __str__(self):
        return f"""Flat[
            Area: {self._area}
            Rooms: {self._rooms}
            Price: {self._price}
            Address: {self._address}
            Floor: {self._floor}   
        ]"""

house1 = House(100, 4, 300000, "ul. Niebieska 56", 40)
flat1 = Flat(80, 5, 150000, "ul. Zielona 4/6", 4)

print(house1)
print(flat1)
