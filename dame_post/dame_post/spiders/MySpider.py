#!/usr/bin/python
# -*- coding: utf-8 -*-
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from dame_post.items import DamePostItem


class MySpider(CrawlSpider):
    name = 'dame_post'
    allowed_domains = ['osl.ugr.es']
    start_urls = ['http://osl.ugr.es/']
    rules = (
        Rule(SgmlLinkExtractor(allow=('/page/\d+/')), follow = True ,callback='parse_item'),
        #Rule(SgmlLinkExtractor(allow=('/page/\d+/')), callback='parse_item')
        )


    def parse_item(self, response):
        self.log('Hola!, esta es una página tipo item! %s' % response.url)
        hxs = HtmlXPathSelector(response)
        posts = hxs.select('//div[contains(@id, "post")]') # Obtenemos todos los 'div' del documento.
    #print divs.extract()$x('//div[contains(@id, "post")]')
    #raw_input("")
    
        elemento = DamePostItem()
        for post in posts: # Con este modo extraemos todos los <p> de cada <div>
            
            elemento['title'] = post.select('h2//text()').extract()
            elemento['title'] = " ".join(elemento['title'])
            elemento['author'] = post.select('.//address[@class="author vcard"]/a/text()').extract()
            elemento['author'] = " ".join(elemento['author'])
            elemento['content'] = post.select('div[@class="entry-content"]/p').extract()
            elemento['content'] = " ".join(elemento['content'])
            elemento['category_list'] = post.select('p/span[@class="entry-categories"]/a/text()').extract()
            elemento['tag_list'] = post.select('p/span[@class="entry-tags"]/a/text()').extract()
        #raw_input("")


        return elemento



