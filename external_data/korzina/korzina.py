from src.data.models import Korzina, Category, UnitMark

dry_goods_units_of_measure = {str(UnitMark.g.title) : 1.0, str(UnitMark.kg.title) : 1000.0}
liquid_goods_units_of_measure = {str(UnitMark.ml.title) : 1.0, str(UnitMark.l.title) : 1000.0}

korzina2019 = Korzina()
korzina2019.name = 'korzina2019'
korzina2019.year = 2019
korzina2019.price = 5193
korzina2019.content = [
    # Grains
    Category('Beans', 6, dry_goods_units_of_measure, 1000),
    Category('Wheat Flour', 6, dry_goods_units_of_measure, 1000),
    Category('Rice', 3, dry_goods_units_of_measure, 1000),
    Category('Other Flour', 5.5, dry_goods_units_of_measure, 1000),
    Category('Whey Bread', 67.9, dry_goods_units_of_measure, 1000),
    Category('Rhye Bread', 72.9, dry_goods_units_of_measure, 1000),
    Category('Pasta', 9, dry_goods_units_of_measure, 1000),
    #
    Category('Potatoes', 100.5, dry_goods_units_of_measure, 1000),
    # veggies
    Category('Cabbage', 6, dry_goods_units_of_measure),
    Category('Tomatoes and Cucumbers', 5, dry_goods_units_of_measure, 1000),
    Category('Edible Roots', 42.6, dry_goods_units_of_measure, 1000), # Svekla, morkov', pasternak, koren' sel'derei i drugie
    Category('Other Vegetables', 25, dry_goods_units_of_measure, 1000),
    Category('Fruits', 118.1, {**dry_goods_units_of_measure, **{str(UnitMark.pcs.title) : 100.0}}, 1000),
    # Sugar and confectionaries
    Category('Sugar', 21, dry_goods_units_of_measure, 1000),
    Category('Sweets', 2, {**dry_goods_units_of_measure, **{str(UnitMark.pcs.title) : 100.0}}, 1000),
    Category('Biscuits', 3.5, {**dry_goods_units_of_measure, **{str(UnitMark.pcs.title) : 100.0}}, 1000),
    # Meat
    Category('Beef', 16.5, dry_goods_units_of_measure, 1000),
    Category('Lamb', 0.8, dry_goods_units_of_measure, 1000),
    Category('Pork', 9.8, dry_goods_units_of_measure, 1000),
    Category('Poultry', 31.6, dry_goods_units_of_measure, 1000),
    # fish
    Category('Fresh Fish', 18, dry_goods_units_of_measure, 1000),
    Category('Herring', 1, dry_goods_units_of_measure, 1000),
    # dairy
    Category('Milk', 134.6, {**dry_goods_units_of_measure, **liquid_goods_units_of_measure}, 1000), # and Kefir
    Category('Sour Cream', 3, {**dry_goods_units_of_measure, **liquid_goods_units_of_measure}, 1000),
    Category('Cottage Cheese', 14.6, dry_goods_units_of_measure, 1000),
    Category('Butter', 5.5, dry_goods_units_of_measure, 1000),
    Category('Cheese', 4.5, dry_goods_units_of_measure, 1000),
    #
    Category('Eggs', 210, {UnitMark.pcs.title : 1.0}, 10),
    # Oils
    Category('Margerine', 1, {**dry_goods_units_of_measure, **liquid_goods_units_of_measure}, 1000),
    Category('Plant seed oil', 10.5, {**dry_goods_units_of_measure, **liquid_goods_units_of_measure}, 1000),
    # Other
    Category('Salt', 3.7, dry_goods_units_of_measure, 1000),
    Category('Tea', 0.5, {**dry_goods_units_of_measure, **{str(UnitMark.bags.title) : 2.0}}, 100),
    Category('Spices', 0.7, dry_goods_units_of_measure, 10),
    ]

print(korzina2019.content.__len__())
