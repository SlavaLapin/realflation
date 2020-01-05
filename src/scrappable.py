from abc import ABCMeta, abstractmethod, abstractproperty
import re, requests, time
from typing import List, Dict

class Scrappable():
    __metaclass__ = ABCMeta
    store_url: str

    def __init__(self, store_url):
        self.count = 0
        self.store_url = store_url

    def scrape_volume(self, full_title, units, standard_volume) -> float:
        for unit in units:
            vol = re.search('(\d+(?:\.\d+)?)'+unit, full_title)
            if vol is not None:
                vol = vol.group()
                vol = re.sub(unit, '', vol)
                vol = float(vol)
                vol *= units.get(unit)
                return vol
        return standard_volume

    def get_page(self, url):
        time.sleep(0.1)
        try:
            page = requests.get(url)
            print('Actual: '+page.url)
        except ConnectionError as e:
            print('An timeout occured when trying to request the page:' + url)
            print(type(e))
            time.sleep(10)
        else:
            return page.text

    @abstractmethod
    def scrape_category(self, cat_url: str, standard_volume: float, units):
        '''Get all ProductItems info in a given category'''
