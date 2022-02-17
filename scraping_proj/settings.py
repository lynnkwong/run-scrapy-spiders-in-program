# Reference:
# - https://docs.scrapy.org/en/latest/topics/settings.html

BOT_NAME = "scraping_proj"

SPIDER_MODULES = ["scraping_proj.spiders"]
NEWSPIDER_MODULE = "scraping_proj.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Global settings:
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s : %(levelname)s : %(message)s"
# Send the logs to this file, rather than the screen.
LOG_FILE = "/tmp/scrapy.log"
