# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import os
import urllib2

class MangaScraperPipeline(object):
    index = 1
    def process_item(self, item, spider):
        if not os.path.exists(item['manga_chapter']):
            os.makedirs(item['manga_chapter'])
        img_content = urllib2.urlopen(item['img_url']).read()
        f = open(os.path.join(item['manga_chapter'],"%s.jpg" % "{0:03d}".format(self.index)),"w")
        f.write(img_content)
        f.close()
        self.index+=1

        return item
