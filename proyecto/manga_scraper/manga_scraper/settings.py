# Scrapy settings for manga_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'manga_scraper'

SPIDER_MODULES = ['manga_scraper.spiders']
NEWSPIDER_MODULE = 'manga_scraper.spiders'
ITEM_PIPELINES = ['manga_scraper.pipelines.MangaScraperPipeline',]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'manga_scraper (+http://www.yourdomain.com)'
