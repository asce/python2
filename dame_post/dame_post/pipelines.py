# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
"""
class DamePostPipeline(object):

    def process_item(self, item, spider):

        return item
"""
from scrapy import signals
from scrapy.contrib.exporter import XmlItemExporter

class DamePostPipeline(object):

    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
         pipeline = cls()
         crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
         crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
         return pipeline

    def spider_opened(self, spider):
        file1 = open('%s.xml' % spider.name, 'w+b')
        file2 = open('%s_without_tags.xml' % spider.name, 'w+b')

        self.files[spider] = [file1,file2]
        self.exporter1 = XmlItemExporter(file1)
        self.exporter2 = XmlItemExporter(file2)
        self.exporter1.start_exporting()
        self.exporter2.start_exporting()

    def spider_closed(self, spider):
        self.exporter1.finish_exporting()
        self.exporter2.finish_exporting()
        files = self.files.pop(spider)
        files[0].close()
        files[1].close()

    def process_item(self, item, spider):
        if not item['tag_list']:
            self.exporter2.export_item(item)
        else:
            self.exporter1.export_item(item)
        return item
