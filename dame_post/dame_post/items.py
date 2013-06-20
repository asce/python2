# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class DamePostItem(Item):
    # define the fields for your item here like:
    # name = Field()
    title = Field()
    author = Field()
    content = Field()
    category_list = Field()
    tag_list = Field()

