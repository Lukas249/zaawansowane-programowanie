from zad_3.Property import Property


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
