from src.data.models import Store, Korzina, ProductItem
from typing import List
from src.data.models import Scan

class Scanner():
    def __init__(self, store: Store, potreb_korzina: Korzina):
        self.store = store
        self.korzina = potreb_korzina

    def scan(self) -> Scan:
        result = Scan(self.store.name)
        all_products = []
        pager = 0
        total_cats = 33
        for category in self.korzina.content:
            cat_low = category.name.lower()
            print(cat_low)
            print(total_cats)
            #input()
            cat_products, pages = self.store.scrapper.scrape_category(self.store.category_urls[cat_low],
                                                                category.standard_volume,
                                                                category.units)
            pager+=pages
            print(pager)
            if type(cat_products) is list:
                all_products+=cat_products
                total_cats -= 1
            else:
                print('Failed at '+cat_low)

        if total_cats == 0:
            result.status = True
        result.content = all_products
        return result

