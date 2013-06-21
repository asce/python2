# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from manga_scraper.items import MangaScraperItem
from scrapy.http import Request
import re
import urllib2
import os

class MySpider(CrawlSpider):

    name = 'mangahere_spider'
    #def __init__(self, *args, **kwargs):                                            #super(CrawlSpider, self).__init__(*args, **kwargs)
    allowed_domains = ['mangahere.com']
    #chapter_url = 'http://www.mangahere.com/manga/naruto/v63/c635/'
    #start_urls = [chapter_url]
    rules = (Rule(SgmlLinkExtractor(allow=('naruto/v\d+/c\d+/\d+\.html')), follow = True ,callback='parse_manga'),)

    def __init__(self, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
#self.allowed_domains = ["mangahere.com"]
        s_url = kwargs.get('start_url')
        if(not not s_url):
            self.manga_chapter,manga_url=self.parse_main_manga_page(s_url)
            self.start_urls = [manga_url]
            self.process_first_url(manga_url)

    def parse_manga(self,response):
        item = MangaScraperItem()
        item['manga_chapter'] = self.manga_chapter
        self.log(' \n\nURL: %s \n' % response.url)
        hxs = HtmlXPathSelector(response)
        item['img_url'] = hxs.select('//section[@class="read_img"]//@src').extract()[0]
        print item,"\n\n"
        return item

    def process_first_url(self,url):
        item = MangaScraperItem()
        item['manga_chapter'] = self.manga_chapter
        self.log(' \n\nPARSE2\n\n\nURL: %s \n' % url)
        html_content = urllib2.urlopen(url).read()
        hxs = HtmlXPathSelector(text = html_content)
        item['img_url'] = hxs.select('//section[@class="read_img"]//@src').extract()[0]
        
        if not os.path.exists(item['manga_chapter']):
            os.makedirs(item['manga_chapter'])
        img_content = urllib2.urlopen(item['img_url']).read()
        f = open(os.path.join(item['manga_chapter'],"%s.jpg" % "{0:03d}".format(0)),"w")
        f.write(img_content)
        f.close()
        
        return item


    def parse_main_manga_page(self, main_manga_url):
        #response = Request(main_manga_url)
        response_html = urllib2.urlopen(main_manga_url).read()
        hxs = HtmlXPathSelector(text = response_html)
        last_manga = hxs.select('//ul[@class="footer_chapters clearfix"]//a')
        manga_name = last_manga.select('./text()').extract()[0]
        manga_url = last_manga.select('./@href').extract()[0]
        manga_name = re.sub('\s','_',manga_name)
        #print "\n\n\n\n",manga_name,manga_url,"\n\n\n\n\n\n\n"
        return manga_name,manga_url

        


      #rules = (Rule(SgmlLinkExtractor(allow=('v\d+/c\d+/(\d+\.html)?')), follow = True ,callback='parse_manga'),)
