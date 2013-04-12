# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class PaddbItem(Item):
	# define the fields for your item here like:
	# name = Field()
	pass

class MonstersItem(Item):
	# Monsters items are defined here
	ID = Field()
	name = Field()
	altName = Field()
	imgLink = Field()
