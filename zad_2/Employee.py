class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: str, birth_date: str, city: str, street: str, zip_code: str, phone: str) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._hire_date = hire_date
        self._birth_date = birth_date
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._phone = phone

    def __str__(self) -> str:
        return f"""Employee[
            First Name: {self._first_name}
            Last Name: {self._last_name}
            Hire Date: {self._hire_date}
            Birth Date: {self._birth_date}
            City: {self._city}
            Street: {self._street}
            Zip Code: {self._zip_code}
            Phone: {self._phone}
        ]"""
