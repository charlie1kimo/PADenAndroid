from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from paddb.items import MonsterItem

class MonsterSpider(BaseSpider):
	name = "monster"
	allowed_domains = ["www.puzzledragonx.com"]
	start_urls = [
		"http://www.puzzledragonx.com/en/monsterbook.asp"
	]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		mobList = []
		monsters = hxs.select('//div[contains(@class, "indexframe")]')
		for monster in monsters:
			mobItem = MonsterItem()
			mobItem['imgLink'] = monster.select('.//a/img/@data-original').extract()
			mobItem['name'] = monster.select('.//a/img/@title').extract()
			mobItem['altName'] = monster.select('.//a/img/@alt').extract()
			mobItem['ID'] = monster.select('.//div[contains(@class, "iframenum")]/text()').extract()
			mobList.append(mobItem)

		return mobList

