from src.data.models import Store
from src.scrapper import ScrapperPerekrestok

store_url = 'https://www.perekrestok.ru/catalog'
perekrestok = Store('Perekrestok', store_url)
perekrestok.scrapper = ScrapperPerekrestok(store_url)
perekrestok.category_urls =  {
        'milk':'/moloko-syr-yaytsa/moloko', # and kefir should be here too
        'beans':'/makarony-krupy-spetsii/krupy-i-bobovye?attr%5B1870%5D%5B%5D=bulgur&attr%5B1870%5D%5B%5D=goroh&attr%5B1870%5D%5B%5D=grechka&attr%5B1870%5D%5B%5D=kinoa&attr%5B1870%5D%5B%5D=kukuruznaya&attr%5B1870%5D%5B%5D=kuskus&attr%5B1870%5D%5B%5D=manka&attr%5B1870%5D%5B%5D=mash&attr%5B1870%5D%5B%5D=mnogozernovaya&attr%5B1870%5D%5B%5D=nut&attr%5B1870%5D%5B%5D=ovsyanaya&attr%5B1870%5D%5B%5D=perlovaya&attr%5B1870%5D%5B%5D=polba&attr%5B1870%5D%5B%5D=pshenichnaya&attr%5B1870%5D%5B%5D=psheno&attr%5B1870%5D%5B%5D=fasol&attr%5B1870%5D%5B%5D=chechevitsa&attr%5B1870%5D%5B%5D=yachmennaya',
        'wheat flour': '/makarony-krupy-spetsii/muka?attr[1589][]=pshenichnaya',
        'rice': '/makarony-krupy-spetsii/krupy-i-bobovye?attr[1870][]=ris',
        'other flour': '/makarony-krupy-spetsii/muka?attr[1589][]=grechnevaya&attr[1589][]=kukuruznaya&attr[1589][]=lnyanaya&attr[1589][]=mindalnaya&attr[1589][]=ovsyanaya&attr[1589][]=polbyanaya&attr[1589][]=rjanaya&attr[1589][]=risovaya',
        'whey bread': '/hleb-sladosti-sneki/hleb-lavash-lepeshki?attr[1853][]=hleb&attr[2132][]=0&attr[2255][]=baton&page=1&sort=rate_desc',
        'rhye bread': '/hleb-sladosti-sneki/hleb-lavash-lepeshki?attr[1853][]=hleb&attr[2132][]=0&attr[2255][]=hleb&page=1&sort=rate_desc',
        'pasta': '/makarony-krupy-spetsii/makaronnye-izdeliya',
        'potatoes': '/ovoschi-frukty-griby/ovoschi?attr[1930][]=kartofel',
        'cabbage': '/ovoschi-frukty-griby/ovoschi?attr[1930][]=kapusta',
        'tomatoes and cucumbers': '/ovoschi-frukty-griby/ovoschi?attr[1930][]=ogurets&attr[1930][]=tomat&attr[1930][]=tomat-cherri',
        'edible roots': '/ovoschi-frukty-griby/ovoschi?attr[1930][]=luk&attr[1930][]=morkov&attr[1930][]=redis&attr[1930][]=redka&attr[1930][]=repa&attr[1930][]=svekla&attr[1930][]=chesnok', # Svekla, morkov', pasternak, koren' sel'derei i drugie
        'other vegetables': '/ovoschi-frukty-griby/ovoschi?attr[1930][]=avokado&attr[1930][]=baklajan&attr[1930][]=brokkoli&attr[1930][]=goroh&attr[1930][]=kabachok&attr[1930][]=kukuruza&attr[1930][]=perets&attr[1930][]=redis&attr[1930][]=tykva&attr[1930][]=fasol',
        'fruits': '/ovoschi-frukty-griby/frukty',
        'sugar': '/kofe-chay-sahar/sahar',
        'sweets': '/hleb-sladosti-sneki/konfety',
        'biscuits': '/hleb-sladosti-sneki/pechene-kreker-vafli-pryaniki?attr[1853][]=pechene',
        'beef': '/myaso-ptitsa-delikatesy/govyadina',
        'lamb': '/myaso-ptitsa-delikatesy/baranina',
        'pork': '/myaso-ptitsa-delikatesy/svinina',
        'poultry': '/myaso-ptitsa-delikatesy/myaso-ptitsy',
        'fresh fish': '/ryba-i-moreprodukty/ryba-ohlajdennaya',
        'herring': '/ryba-i-moreprodukty/seld',
        'sour cream': '/moloko-syr-yaytsa/smetana',
        'cottage cheese': '/moloko-syr-yaytsa/tvorog-syrki?attr[1853][]=tvorog',
        'butter': '/moloko-syr-yaytsa/slivochnoe-maslo-i-margarin?attr[1853][]=maslo-slivochnoe',
        'cheese': '/moloko-syr-yaytsa/syry',
        'eggs': '/moloko-syr-yaytsa/yaytso',
        'margerine': '/moloko-syr-yaytsa/slivochnoe-maslo-i-margarin?attr[1853][]=margarin',
        'plant seed oil': '/makarony-krupy-spetsii/maslo-rastitelnoe',
        'salt': '/makarony-krupy-spetsii/sol',
        'tea': '/kofe-chay-sahar/chay',
        'spices': '/makarony-krupy-spetsii/spetsii-i-pripravy'
}
