class Library:

    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str) -> None:
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._open_hours = open_hours
        self._phone = phone

    def __str__(self):
        return f"""Library[
            City: {self._city}
            Street: {self._street}
            Zip Code: {self._zip_code}
            Opening Hours: {self._open_hours}
            Phone: {self._phone}
        ]"""
