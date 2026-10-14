import requests

class Brewery(object):
    id: str
    name: str
    brewery_type: str
    address_1: str
    address_2: str
    address_3: str
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: float
    latitude: float
    phone: str
    website_url: str
    state: str
    street: str

    def __init__(self, brewery_data: dict):
        self.id = brewery_data["id"]
        self.name = brewery_data["name"]
        self.brewery_type = brewery_data["brewery_type"]
        self.address_1 = brewery_data["address_1"]
        self.address_2 = brewery_data["address_2"]
        self.address_3 = brewery_data["address_3"]
        self.city = brewery_data["city"]
        self.state_province = brewery_data["state_province"]
        self.postal_code = brewery_data["postal_code"]
        self.country = brewery_data["country"]
        self.longitude = brewery_data["longitude"]
        self.latitude = brewery_data["latitude"]
        self.phone = brewery_data["phone"]
        self.website_url = brewery_data["website_url"]
        self.street = brewery_data["street"]

    def __str__(self):
        return str(self.__dict__)



res = requests.get("https://api.openbrewerydb.org/v1/breweries?page=1&per_page=20")
json = res.json()

brewery_list = []

for brewery_data in json:
    brewery = Brewery(
        brewery_data
    )

    brewery_list.append(brewery)

    print(brewery)