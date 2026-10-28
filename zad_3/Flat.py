from zad_3.Property import Property


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
