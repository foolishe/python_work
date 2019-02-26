# -*- coding: utf-8 -*-
import scrapy
import datetime
import socket

from scrapy.loader.processors import MapCompose, Join
from scrapy.loader import ItemLoader
from .. import items

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls = ['http://web:9312/properties/property_000000.html',]



    def parse(self, response):
        """ This function parses a property page.

        @url http://web:9312/properties/property_000000.html
        @returns items 1
        @scrapes title price description address image_urls
        @scrapes url project spider server date

        """

        l = ItemLoader(item=Item(),response=response)

        l.add_xpath('title','//*[@itemprop="name"][1]/text()',
            MapCompose(unicode.strip,unicode.title))

        l.add_xpath('price','.//*[@itemprop="price"][1]/text()',
        MapCompose(lambda i:i.replace(',',''),float),re='[,\.0-9]+')

        l.add_xpath('description','//*[@itemprop="description"][1]/text()',
            MapCompose(unicode.strip),Join())

        l.add_xpath('address','//*[@itemprop="address"][1]/text()',
            MapCompose(unicode.strip))

        l.add_xpath('image_urls','//*[@itemprop="image"][1]/@src',
            MapCompose(lambda i: urlparse.usrljoin(response.url,i)))


        l.add_value('url',reponse.url)
        l.add_value('project',self.settings.get('BOT_NAME'))
        l.add_value('spider',self.name)
        l.add_value('server',socket.gethostname())
        l.add_value('date',datetime.datetime.now())

        return l.load_item()
