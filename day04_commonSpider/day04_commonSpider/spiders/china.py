# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from day04_commonSpider.items import NewsItem
from day04_commonSpider.loader import ChinaLoader


class ChinaSpider(CrawlSpider):
    name = 'china'
    allowed_domains = ['tech.china.com']
    start_urls = ['http://tech.china.com/articles/']

    rules = (
        Rule(LinkExtractor(allow='article\/.*\.html', restrict_xpaths='//*[@id="left_side"]//div[@class="con_item"]'),
             callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//div[@id="pageStyle"]//a[contains(.,"下一页")]'))
    )

    def parse_item(self, response):
        loader = ChinaLoader(item=NewsItem(), response=response)
        loader.add_xpath('title', '//*[@id="chan_newsTitle"]/text()')
        loader.add_value('url', response.url)
        loader.add_xpath('text', '//*[@id="chan_newsDetail"]/text()')
        loader.add_xpath('datetime', '//*[@id="chan_newsInfo"]/text()', re='(\d+-\d+-\d+:\d+:\d+)')
        loader.add_xpath('datetime', '//*[@id="chan_newsInfo"]/text()', re='来源:(.*)')
        loader.add_value('website', '中华网')
        yield loader.load_item()
        # def parse_item(self, response):
        #     item = NewsItem()
        #     item['title'] = response.xpath('//*[@id="chan_newsTitle"]').extract_first()
        #     item['url'] = response.url
        #     item['text'] = ''.join(response.xpath('//div[@id="chan_newsDetail"]//text()').extract()).strip()
        #     item['datetime'] = response.xpath('//div[@id="chan_newsInfo"]/text()').re_first('(\d+-\d+-\d+ \s\d+:\d:\d+)')
        #     item['source'] = response.xpath('//div[@id="chan_newsInfo"]/text()').re_first('来源:(.*)').strip()
        #     item['website'] = '中华网'
        #     yield item
