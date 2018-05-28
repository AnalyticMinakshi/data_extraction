# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ProductCategoryItem(Item):
    item_id = Field()
    category_name = Field()
    category_reference = Field()
    item_name = Field()
    quantity = Field()
    price = Field()
    offer = Field()
    old_price = Field()
