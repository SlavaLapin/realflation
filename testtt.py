from src.scanner import Scanner
from external_data.store_urls.stores_list import perekrestok
from external_data.korzina.korzina import korzina2019


test = Scanner(perekrestok, korzina2019)
test.scan().save()

'''
!!!ABANDONED CODE!!!
r_kebbs4
мл л кг г шт пак

 vol = re.search(r'.?.?.?мл', full_title)
        if vol is not None:
            vol = vol.group()
            vol = re.sub(r'мл', '', vol)
        else:
            vol = re.search(r'\dл', full_title)
            if vol is not None:
                vol = vol.group()
                vol = re.sub(r'л', '', vol)
                vol += '000'
            else:
                vol = re.search(r'.?.?.?кг', full_title)
                if vol is not None:
                    vol = vol.group()
                    vol = re.sub(r'кг', '', vol)
                    vol += '000'
                else:
                    vol = re.search(r'.?.?.?г', full_title)
                    if vol is not None:
                        vol = vol.group()
                        vol = re.sub(r'г', '', vol)
                    else:
                        vol = re.search(r'.?.?шт', full_title)
                        if vol is not None:
                            vol = vol.group()
                            vol = re.sub(r'шт', '', vol)
                        else:
                            vol = re.search(r'.?.?пак', full_title)
                            if vol is not None:
                                vol = vol.group()
                                vol = re.sub(r'пак', '', vol)
                                vol *= 2
                            else:
                                vol = self.standard_volume
        vol = float(vol)
        return vol
'''
