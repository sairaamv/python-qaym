python-qaym: A simply Python wrapper for Qaym API
=================================================

Qaym website: `http://Qaym.com <http://www.qaym.com>`_

Basic Usage of python-qaym
--------------------------

.. code-block:: pycon

    >>> from qaym.api import Api
    >>> import os

    >>> # getting the API key
    >>> QAYM_KEY = os.environ.get('QAYM_KEY')

    >>> api = Api(key=QAYM_KEY)

    >>> # retrieve a list of countries
    >>> countries = api.GetCountries()
    >>> print repr(countries[1])
    Country (ID=756, Name=ألمانيا)

    >>> # retrieve a country information
    >>> info = api.GetCountryInfo(178)
    >>> print repr(info)
    Country (ID=178, Name=البحرين)

    >>> # retrieve a list cities for a given country
    >>> cities = api.GetCities(178)
    >>> print cities[0]
    City (ID:337, Name=مدينة حمد)

    >>> # retrieve a city information
    >>> city = api.GetCityInfo(290)
    >>> print city
    City (ID:290, Name=المنامة)
    >>> print city.latitude, city.longitude
    26.1927202164612 50.5360794067383

    >>> # retrieve a list of restaurants in a city
    >>> items = api.GetItems(290)
    >>> print items[0]
    Item (ID:662, Name=BYTES)

    >>> # retrieve the top 50 restaurants in a city
    >>> top_items = api.GetItems(290, top=True)
    >>> for item in top_items:
    >>>     print item.item_name, item.item_id, item.score

    >>> # retrieve a restaurant information
    >>> item = api.GetItem(43)
    >>> print repr(item)
    Item (ID:43, Name=دومينوز بيتزا السعودية -  Domino\'s Pizza KSA
    >>> print item.url_twitter
    u'http://twitter.com/DominosKSA'


    >>> # retrieve locations of a restaurant
    >>> locations = api.GetLocations(43)
    >>> print locations[0]
    Location (ID:18, Address=نهاية شارع الملك فهد غرباً (الستين سابقاُ))


    >>> # retrieve reviews of a restaurant
    >>> reviews = api.GetReviews(43)
    >>> print 'number of reviews', len(reviews)
    number of reviews: 194
    >>> print reviews[0].text.encode('utf8')[:145]
    review: من بين جميع مطاعم البيتزا التي جربتها في الرياض ، يظل دومينوز هو الأول دائماً ، ?


    >>> # retrieve uploaded images of a restaurant
    >>> images = api.GetImages(43)
    >>> print images[0]
    Image (User:Mahmoud1980, URL=http://www.qaym.com/117389.jpg)

    >>> # retrieve (up/down) votes of a restaurant
    >>> votes = api.GetVotes(43)
    >>> print 'up:', len(votes['up']), ', down:', len(votes['down'])
    up: 997 , down: 201

    >>> # retrieve tags
    >>> tags = api.GetTags()
    >>> print tags[0]
    Tag (ID:58, Name:شاورما)

    >>> # retrieve a list of tagged restaurant
    >>> items = api.GetItemsByTag(58)
    >>> print items[0]
    Item (ID:32, Name=ماما نورة Mama Noura)


