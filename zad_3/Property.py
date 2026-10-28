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
