from enum import Enum
import mongoengine as mongoengine
import datetime
from typing import Dict
from src.scrappable import Scrappable

class UnitMark(Enum):
    ml = (0, 'мл')
    l = (1, 'л')
    g = (2, 'г')
    kg = (3, 'кг')
    pcs = (4, 'шт')
    bags = (5, 'пак')

    def __init__(self, id, title):
        self.id = id
        self.title = title


class Category(mongoengine.EmbeddedDocument):
    name = mongoengine.StringField(required=True)
    amount = mongoengine.FloatField(required=True)
    #parent_category = mongoengine.ObjectIdField(Category, default=None)
    units = mongoengine.DictField()
    standard_volume = mongoengine.FloatField(default=1000)
    meta = {
        'db_alias': 'core',
        'collection': 'category',
        'indexes': [
            'name',
            'amount',
            #'parent_category',
            'units',
            'standard_volume'
        ],
        'ordering': ['-name']
    }

class Korzina(mongoengine.Document):
    created = mongoengine.DateTimeField(default = datetime.datetime.now)
    year = mongoengine.IntField(required=True)
    price = mongoengine.FloatField()
    content = mongoengine.EmbeddedDocumentListField(Category)
    meta = {
        'db_alias': 'core',
        'collection': 'korzina',
        'indexes': [
            'created',
            'year',
            'price',
            'content',
        ],
        'ordering': ['-year']
    }

class ProductItem(mongoengine.EmbeddedDocument):
    name = mongoengine.StringField(required=True)
    category = mongoengine.StringField(required=True)
    price = mongoengine.FloatField(required=True)
    volume = mongoengine.FloatField(required=True)
    real_price = mongoengine.FloatField(required=True)
    link = mongoengine.StringField()
    meta = {
        'db_alias': 'core',
        'collection': 'product_item',
        'indexes': [
            'name',
            'category',
            'price',
            'volume',
            'real_price',
            'link,'
        ],
        'ordering': ['-name']
    }

class Scan(mongoengine.Document):
    created = mongoengine.DateTimeField(default = datetime.datetime.now)
    store = mongoengine.StringField()
    status = mongoengine.BooleanField(default = False)
    content = mongoengine.EmbeddedDocumentListField(ProductItem)

    meta = {
        'db_alias':'core',
        'collection':'scan',
        'indexes': [
            'created',
            'store',
            'status',
            'content',
        ],
        'ordering':['-created']
    }

class Stat(mongoengine.Document):
    created = mongoengine.DateTimeField(default = datetime.datetime.now)
    store = mongoengine.ObjectIdField()
    korzina = mongoengine.ObjectIdField()
    minimal_korzina_price = mongoengine.FloatField(required=True)
    average_price_per_cat = mongoengine.DictField()
    share_per_cat = mongoengine.DictField()
    meta = {
        'db_alias': 'core',
        'collection': 'stat',
        'indexes': [
            'created',
            'store',
            'korzina',
            'minimal_korzina_price',
            'average_price_per_cat',
            'share_per_cat',
        ],
        'ordering': ['-created']
    }

class Store(mongoengine.Document):
    name = mongoengine.StringField(required=True)
    url = mongoengine.StringField(required=True)
    category_urls = mongoengine.DictField(required=True)
    scrapper: Scrappable

    meta = {
        'db_alias' : 'core',
        'collection' : 'store',
        'indexes' : [
            'name',
            'url',
            'category_urls',
        ],
        'ordering' : ['name']
    }
