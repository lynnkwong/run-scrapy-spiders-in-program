import scrapy

from scraping_proj.items import AuthorItem


class AuthorSpider(scrapy.Spider):
    name = "authors"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        author_page_links = response.xpath(
            './/small[@class="author"]/following-sibling::a'
        )
        yield from response.follow_all(author_page_links, self.parse_author)

        pagination_links = response.xpath('.//li[@class="next"]/a')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response):
        def extract_with_xpath(query):
            """A help function to reduce code redundancy."""
            return response.xpath(query).get(default="").strip()

        author = AuthorItem(
            name=extract_with_xpath('.//h3[@class="author-title"]/text()'),
            birth_date=extract_with_xpath(
                './/span[@class="author-born-date"]'
            ),
            country=extract_with_xpath(
                './/span[@class="author-born-location"]'
            ),
        )
        yield author
