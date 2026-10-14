import requests
import argparse

class Brewery:
    id: str
    name: str
    brewery_type: str
    address_1: str | None
    address_2: str | None
    address_3: str | None
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: float | None
    latitude: float | None
    phone: str | None
    website_url: str | None
    state: str
    street: str | None

    def __init__(self, brewery_data: dict):
        self.id = brewery_data.get("id")
        self.name = brewery_data.get("name")
        self.brewery_type = brewery_data.get("brewery_type")
        self.address_1 = brewery_data.get("address_1")
        self.address_2 = brewery_data.get("address_2")
        self.address_3 = brewery_data.get("address_3")
        self.city = brewery_data.get("city")
        self.state_province = brewery_data.get("state_province")
        self.postal_code = brewery_data.get("postal_code")
        self.country = brewery_data.get("country")
        self.longitude = brewery_data.get("longitude")
        self.latitude = brewery_data.get("latitude")
        self.phone = brewery_data.get("phone")
        self.website_url = brewery_data.get("website_url")
        self.state = brewery_data.get("state")
        self.street = brewery_data.get("street")

    def __str__(self):
        return f'''
        Unique identifier for the brewery: {self.id}
        Brewery name: {self.name}
        Type of brewery: {self.brewery_type}
        Primary street address: {self.address_1}
        Secondary address line: {self.address_2}
        Third address line: {self.address_3}
        City name: {self.city}
        State or province: {self.state_province}
        Postal or ZIP code: {self.postal_code}
        Country name: {self.country}
        Longitude coordinate: {self.longitude}
        Latitude coordinate: {self.latitude}
        Contact phone number: {self.phone}
        Brewery website URL: {self.website_url}
        State abbreviation or name: {self.state}
        Street address: {self.street}
        '''

parser = argparse.ArgumentParser()
parser.add_argument("--city")
args = parser.parse_args()

params = {
    "page": 1,
    "per_page": 20
}

if args.city:
    params["by_city"] = args.city

res = requests.get("https://api.openbrewerydb.org/v1/breweries", params=params)
json = res.json()

brewery_list = []

for brewery_data in json:
    brewery = Brewery(
        brewery_data
    )

    brewery_list.append(brewery)

    print(brewery)