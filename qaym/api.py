from models import Country, City, Item, Location, Review, Image, Vote, Tag
import requests

BASE_URL = 'http://api.qaym.com/0.1'


class Api(object):
    """
    A python interface to the Qaym API
    """
    def __init__(self, key=None, base_url=None):
        if base_url is None:
            self.base_url = BASE_URL
        else:
            self.base_url = base_url

        if key is None:
            raise ValueError("no QAYM_KEY variable was provided")
        else:
            self.key = key

    def GetCountries(self):
        url = '%s/countries/key=%s' % (self.base_url, self.key)
        data = requests.get(url).json()
        countries = []
        if type(data) == bool:
            return countries
        for country in data:
            countries.append(Country.from_json(country))

        return countries

    def GetCountryInfo(self, country_id):
        url = '%s/countries/%s/key=%s' % (self.base_url, str(country_id), self.key)
        data = requests.get(url).json()

        return Country.from_json(data)

    def GetCities(self, country_id=None):
        if country_id is None:
            url = '%s/cities/key=%s' % (self.base_url, self.key)
        else:
            url = '%s/countries/%s/cities/key=%s' % (self.base_url, str(country_id), self.key)
        data = requests.get(url).json()
        cities = []
        if type(data) == bool:
            return cities
        for city in data:
            cities.append(City.from_json(city))

        return cities

    def GetCityInfo(self, city_id):
        url = '%s/cities/%s/key=%s' % (self.base_url, str(city_id), self.key)
        data = requests.get(url).json()

        return City.from_json(data)

    def GetItems(self, city_id, top=False):
        if top:
            url = '%s/cities/%s/items/top/key=%s' % (self.base_url, str(city_id), self.key)
        else:
            url = '%s/cities/%s/items/key=%s' % (self.base_url, str(city_id), self.key)
        data = requests.get(url).json()
        items = []
        if type(data) == bool:
            return items
        for item in data:
            items.append(Item.from_json(item))

        return items

    def GetItem(self, item_id):
        url = '%s/items/%s/key=%s' % (self.base_url, str(item_id), self.key)
        data = requests.get(url).json()

        return Item.from_json(data)

    def GetLocations(self, item_id):
        url = '%s/items/%s/locations/key=%s' % (self.base_url, str(item_id), self.key)
        data = requests.get(url).json()
        locations = []
        if type(data) == bool:
            return locations
        for location in data:
            locations.append(Location.from_json(location))

        return locations

    def GetReviews(self, item_id):
        url = '%s/items/%s/reviews/key=%s' % (self.base_url, str(item_id), self.key)
        data = requests.get(url).json()
        reviews = []
        if type(data) == bool:
            return reviews
        for review in data:
            reviews.append(Review.from_json(review))

        return reviews

    def GetImages(self, item_id):
        url = '%s/items/%s/images/key=%s' % (self.base_url, str(item_id), self.key)
        data = requests.get(url).json()
        images = []
        if data is None:
            return images
        if type(data) == bool:
            return images
        for image in data:
            images.append(Image.from_json(image))

        return images

    def GetVotes(self, item_id):
        url = '%s/items/%s/votes/key=%s' % (self.base_url, str(item_id), self.key)
        data = requests.get(url).json()
        ups = []
        downs = []
        votes = {'up': ups, 'down': downs}
        if data is None:
            return votes
        if type(data) == bool:
            return votes
        for up in data.get('up', []):
            ups.append(Vote.from_json(up))
        votes['up'] = ups
        for down in data.get('down', []):
            downs.append(Vote.from_json(down))
        votes['down'] = downs

        return votes

    def GetTags(self):
        url = '%s/tags/key=%s' % (self.base_url, self.key)
        data = requests.get(url).json()
        tags = []
        if type(tags) == bool:
            return tags
        for tag in data:
            tags.append(Tag.from_json(tag))

        return tags

    def GetItemsByTag(self, tag_id):
        url = '%s/tags/%s/items/key=%s' % (self.base_url, str(tag_id), self.key)
        data = requests.get(url).json()
        items = []
        if type(data) == bool:
            return items
        for item in data:
            items.append(Item.from_json(item))

        return items