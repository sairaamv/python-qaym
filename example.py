#!/usr/bin/env python
# -*- coding: utf-8 -*-

from qaym.api import Api
import os

# getting the API key
QAYM_KEY = os.environ.get('QAYM_KEY')

api = Api(key=QAYM_KEY)

# retrieve a list of countries
countries = api.GetCountries()
print repr(countries[0])

# retrieve a country information
info = api.GetCountryInfo(230)
print repr(info)

# retrieve a list cities for a given country
cities = api.GetCities(178)
print cities

# retrieve a city information
city = api.GetCityInfo(290)
print repr(city)

# retrieve a list of restaurants in a city
items = api.GetItems(290)
for item in items:
    print repr(item)

# retrieve the top 50 restaurants in a city
top_items = api.GetItems(290, top=True)
for item in top_items:
    print item.item_name, item.item_id, item.score

top = [(item.item_name, int(item.score), item.item_id) for item in top_items]
for i in sorted(top, key=lambda x: x[1], reverse=True):
    print i[0], i[1], i[2]

i = api.GetItem(43)
print repr(i)

# retrieve locations of a restaurant
l = api.GetLocations(43)
print l

# retrieve reviews of a restaurant
r = api.GetReviews(43)
print r

# retrieve uploaded images of a restaurant
images = api.GetImages(43)
print images
print len(images)

# retrieve (up/down) votes of a restaurant
votes = api.GetVotes(43)
print votes
print len(votes['up']), len(votes['down'])

# retrieve tags
tags = api.GetTags()
print tags

# retrieve a list of tagged restaurant
items = api.GetItemsByTag(59)
print items
print len(items)

