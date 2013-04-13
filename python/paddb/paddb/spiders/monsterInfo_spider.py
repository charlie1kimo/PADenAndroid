import re
from scrapy.http import Request
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from paddb.items import MonsterInfo

class MonsterInfoSpider(BaseSpider):
	name = "monsterInfo"
	allowed_domains = ["www.puzzledragonx.com"]
	start_urls = [
		"http://www.puzzledragonx.com/en/monster.asp?n=%d" % \
		ID for ID in range(1, 604)
	]

	def make_requests_from_url(self, url):
		return Request(url, meta={'dont_redirect': True}, dont_filter=True)

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		monster = MonsterInfo()
		# I cheat...use the website url as ID identifier...
		thisID = response.url.split('=')[1]
		monster['ID'] = [thisID]
		# some easy patterns to extact...
		monster['name'] = hxs.select('//div[contains(@class, "avatar")]/img/@title').extract()
		monster['altName'] = hxs.select('//div[contains(@class, "avatar")]/img/@alt').extract()
		monster['imgLink'] = hxs.select('//div[contains(@class, "avatar")]/img/@src').extract()

		### break the response into sections to parse:
		#	section0 = name, type, element, rarity, cost
		#	section1 = basic stats: lv, hp, atk, rcv
		#	section2 = experience
		#	section3 = growth chart
		#	section4 = skills
		#	section5 = how to get it
		#	section6 = evolve to what
		#	section7 = blank (not useful)
		#	section8 = mob links (not useful)
		#	section9 = blank (not useful)
		sections = hxs.select('//tr/td[contains(@class, "section")]')
		for secIndex in range(len(sections)):
			sec = sections[secIndex]
			infoList = sec.select('.//tr')
			for infoIndex in range(len(infoList)):
				if infoIndex == 0:
					secName = infoList[infoIndex].select('.//text()').extract()[0]
					continue
				
				# some test section codes...
				### TO BE IMPLEMENTED ###
				
				parseResult = infoList[infoIndex].select('.//text()').extract()
				if len(parseResult) > 0:
					parseName = parseResult[0]
					parseName = re.sub('[\s-]', '_', parseName).lower()
					try:
						monster[parseName] = parseResult[1:]
					except KeyError, e:
						pass

		return monster 
