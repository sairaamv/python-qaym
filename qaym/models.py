# -*- coding: utf-8 -*-


class QaymModel(object):
    """
    base class from which all Qaym models will initiate
    """
    def __init__(self, **kwargs):
        self.param_defaults = {}

    @classmethod
    def from_json(cls, data, **kwargs):
        """
        Create a new instance from a JSON dict
        """
        data_copy = data.copy()
        if kwargs:
            for key, value in kwargs.items():
                data_copy[key] = value

        c = cls(**data_copy)
        c._json = data
        return c


class Country(QaymModel):
    """
    A class representation of the Country component
    """
    def __init__(self, **kwargs):
        self.param_defaults = {
            'name': None,
            'country_id': None,
            'added_by': None,
            'addition_timestamp': None,
            'latitude': None,
            'longitude': None,
            'zoom': None
        }
        for param, default in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))

    def __repr__(self):
        return "Country (ID={country_id}, Name={name})".format(country_id=self.country_id,
                                                               name=self.name.encode('utf8'))


class City(QaymModel):
    """
    A class representation of the City component
    """
    def __init__(self, **kwargs):
        self.param_defaults = {
            'city_id': None,
            'name': None,
            'added_by': None,
            'addition_timestamp': None,
            'latitude': None,
            'longitude': None,
            'zoom': None
        }
        for param, default in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))

    def __repr__(self):
        return "City (ID:{city_id}, Name={name})".format(city_id=self.city_id,
                                                         name=self.name.encode('utf8'))


class Item(QaymModel):
    """
    A class representation of the Item/Restaurant component
    """
    def __init__(self, **kwargs):
        self.param_defaults = {
            "item_id": None,
            "item_name": None,
            "score": None,
            "weighted_score": None,
            "ratio": None,
            "tags": None,
            "total_number_of_votes": None,
            "number_of_positive_votes": None,
            "number_of_negative_votes": None,
            "username": None,
            "user_id": None,
            "category_main_id": None,
            "category_sub_id": None,
            "category_main": None,
            "category_sub": None,
            "views": None,
            "vote_count": None,
            "url": None,
            "url_twitter": None,
            "url_facebooj": None,
            "item_desc": None,
            "exclusive_city_id": None
        }
        for param, default in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))

    def __repr__(self):
        return "Item (ID:{item_id}, Name={item_name})".format(item_id=self.item_id,
                                                              item_name=self.item_name.encode('utf8'))


class Location(QaymModel):
    """
    A class representation of the Location component
    """
    def __init__(self, **kwargs):
        self.param_defaults = {
            "location_id": None,
            "score": None,
            "country": None,
            "country_id": None,
            "address": None,
            "user_id": None,
            "latitude": None,
            "longitude": None,
            "title": None,
            "phone": None,
            "tiny_thumb_file_detail_id": None,
            "username": None,
            "city_id": None,
            "city": None
        }
        for param, default in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))

    def __repr__(self):
        return "Location (ID:{location_id}, Address={address})".format(location_id=self.location_id,
                                                                       address=self.address.encode('utf8'))


class Review(QaymModel):
    """
    A class representation of the Review component
    """
    def __init__(self, **kwargs):
        self.param_defaults = {
            "username": None,
            "title": None,
            "user_id": None,
            "score": None,
            "time": None,
            "number_of_posts": None,
            "last_poster_id": None,
            "last_post_time": None,
            "text": None,
            "last_edit_user_id": None,
            "last_edit_time": None
        }
        for param, default in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))

    def __repr__(self):
        return "Review (User:{username}, text={text})".format(username=self.username.encode('utf8'),
                                                              text=self.text.encode('utf8'))


class Image(QaymModel):
    """
    A class representation of the Image component
    """
    def __init__(self, **kwargs):
        self.param_defaults = {
            "user_id": None,
            "file_detail_id": None,
            "title": None,
            "username": None
        }
        for param, default in self.param_defaults.items():
            if param == 'file_detail_id':
                url = kwargs.get(param, default)
                if url:
                    url = 'http://www.qaym.com/%s.jpg' % url
                setattr(self, 'url', url)
            else:
                setattr(self, param, kwargs.get(param, default))

    def __repr__(self):
        return "Image (User:{username}, URL={url})".format(username=self.username.encode('utf8'), url=self.url)


class Vote(QaymModel):
    """
    A class representation of the Vote component
    """
    def __init__(self, **kwargs):
        self.param_defaults = {
            "vote": None,
            "user_id": None,
            "username": None
        }
        for param, default in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))

    def __repr__(self):
        return "Vote (User:{username}, Vote={vote})".format(username=self.username.encode('utf8'), vote=self.vote)


class Tag(QaymModel):
    """
    A class representation of the Tag component
    """
    def __init__(self, **kwargs):
        self.param_defaults = {
            "tag_def_id": None,
            "tag": None
        }
        for param, default in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))

    def __repr__(self):
        return "Tag (ID:{tag_def_id}, Name:{tag})".format(tag_def_id=self.tag_def_id, tag=self.tag.encode('utf8'))