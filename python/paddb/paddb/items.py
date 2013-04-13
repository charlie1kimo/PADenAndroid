# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class PaddbItem(Item):
	# define the fields for your item here like:
	# name = Field()
	pass

class MonsterItem(Item):
	# Monsters items are defined here
	ID = Field()
	name = Field()
	altName = Field()
	imgLink = Field()

class MonsterInfo(MonsterItem):
	# Monster info objects are defined here
	imgLarge = Field()
	jp_name = Field()
	type = Field()
	element = Field()
	rarity = Field()
	Cost = Field()
	level = Field()
	hp = Field()
	atk = Field()
	rcv = Field()
	as_feeder = Field()
	power_up = Field()
	skill = Field()
	leader_skill = Field()
	minSkillLv = Field()
	maxSkillLv = Field()
	minSkillTurns = Field()
	maxSkillTurns = Field()
	wayToGet = Field()
	evolveMaterials = Field()
	evolveToID = Field()

