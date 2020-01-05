from bs4 import BeautifulSoup
from src.data.models import ProductItem
from src.scrappable import Scrappable
#adjusted to do only milk at this point
#url='https://www.perekrestok.ru/catalog/moloko-syr-yaytsa/moloko'


class ScrapperPerekrestok(Scrappable):

    def scrape_category(self, cat_url, standard_volume, units):
        count = 0
        url = self.store_url + cat_url + '&page=0'
        items = []
        # put the page into a soup
        while(url is not None) and (url!='#'):
            count += 1
            #print('Page:', count)
            print(url)
            page = self.get_page(url)
            soup = BeautifulSoup(page, 'html.parser')

            #print(soup.text)
            # determine the next page to be scrapped
            next_url = soup.find('a', 'xf-paginator__item js-paginator__next')
            #next_url = url.replace('&page='+str(count-1), '&page='+str(count))
            if (next_url is not None) and (next_url!=url):
                url = next_url.attrs['href']
            else:
                url = None

            # find each ProductItem block in catalog
            catalog = soup.find('ul', 'xf-catalog js-catalog')
            if catalog is not None:
                for item in catalog.findAll('div', 'xf-product js-product'):
                    title = item.find('a', 'xf-product-title__link js-product__title xf-product-title__link--additional').attrs['title']
                    #print(title)
                    link = item.find('a', 'xf-product-title__link js-product__title xf-product-title__link--additional').attrs['href']
                    #print(link)
                    cost = float(item.find('div', 'xf-price').attrs['data-cost'])
                    #print(cost)

                    vol = self.scrape_volume(title, units, standard_volume)
                    real_cost = (cost/vol)*standard_volume
                    #print(vol)
                    #print(real_cost)

                    product = ProductItem(title, link, cost, vol, real_cost)

                    items.append(product)

        return (items, count)
