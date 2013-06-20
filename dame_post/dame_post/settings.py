# Scrapy settings for dame_post project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'dame_post'

SPIDER_MODULES = ['dame_post.spiders']
NEWSPIDER_MODULE = 'dame_post.spiders'
ITEM_PIPELINES = ['dame_post.pipelines.DamePostPipeline',]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'dame_post (+http://www.yourdomain.com)'
