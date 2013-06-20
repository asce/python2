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


class MySpider(CrawlSpider):
    name = 'dame_post'
    allowed_domains = ['osl.ugr.es']
    start_urls = ['http://osl.ugr.es/']
    rules = (
        Rule(SgmlLinkExtractor(allow=('/page/\d+/')), callback='parse_item'),
        #Rule(SgmlLinkExtractor(allow=('/page/\d+/')), callback='parse_item')
        )
    """rules = (
        # Extraer enlaces que coincidan con 'category.php' (pero que no coincidan con 'subsection.php') y seguir esos enlaces (si no indicamos callback significa que debe seguir por defecto)
        Rule(SgmlLinkExtractor(allow=('http://osl\.ugr\.es/page/',)),callback='parse_item'),

        Rule(SgmlLinkExtractor(allow=('http://osl\.ugr\.es/page/\d+/',)),callback='parse_item'),

        # Extraer los enlaces que coincidan con 'item.php' y analizarlos con el método parse_item de los spiders
        #Rule(SgmlLinkExtractor(allow=('item\.php', )), callback='parse_item'),
        )"""

def parse_item(self, response):
    self.log('Hola!, esta es una página tipo item! %s' % response.url)
    hxs = HtmlXPathSelector(response)
    posts = hxs.select('//div[contains(@id, "post")]') # Obtenemos todos los 'div' del documento.
    #print divs.extract()$x('//div[contains(@id, "post")]')
    #raw_input("")
    
    elemento = Item()
    for post in posts: # Con este modo extraemos todos los <p> de cada <div>
        elemento['title'] = post.select('/h2//text()')
        elemento['author'] = post.select('//address[@class="author vcard"]/a/text()').extract()
        elemento['content'] = post.select('/div[@class="entry-content"]/p')[1].extract()
        elemento['category_list'] = post.select('/p/span[@class="entry-categories"]/a/text()').extract()
        elemento['tag_list'] = post.select('/p/span[@class="entry-tags"]/a/text()').extract()
        #raw_input("")


    return elemento



