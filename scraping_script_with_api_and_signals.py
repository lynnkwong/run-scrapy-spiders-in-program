# Run the spider with the internal API of Scrapy:
from scrapy import signals
from scrapy.crawler import Crawler, CrawlerProcess
from scrapy.utils.project import get_project_settings

from scraping_proj.spiders.quotes import QuoteSpider

settings = get_project_settings()
process = CrawlerProcess(settings)
quote_crawler = Crawler(QuoteSpider, settings)


def handle_spider_opened(spider):
    print(f"Spider {spider.name} is started.")


def handle_item_scraped(item):
    print(f"Item scraped: {item}.")


def handle_spider_closed(spider):
    print(f"Spider {spider.name} is closed.")


quote_crawler.signals.connect(
    handle_spider_opened, signal=signals.spider_opened
)
quote_crawler.signals.connect(handle_item_scraped, signal=signals.item_scraped)
quote_crawler.signals.connect(
    handle_spider_closed, signal=signals.spider_closed
)

process.crawl(quote_crawler, tag="love")
process.start()
