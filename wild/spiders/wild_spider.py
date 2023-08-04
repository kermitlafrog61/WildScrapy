import scrapy
from itemloaders.processors import TakeFirst
from scrapy.http import Request
from scrapy.loader import ItemLoader
from scrapy.selector import Selector
from selenium import webdriver

from wild.items import WildItem


class MySpider(scrapy.Spider):
    name = "wild"
    start_urls = [
        # I chose Rubashki, but you can choose any other category
        "https://www.wildberries.ru/catalog/muzhchinam/odezhda/rubashki",
    ]

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        # We'll use Chrome driver. This will help us to fully load page
        self.driver = webdriver.Chrome()

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, self.parse, dont_filter=True)

    def parse(self, response):
        # Setting up driver
        self.driver.get(response.url)

        # Wait for the page to load
        self.load_page()

        sel = Selector(text=self.driver.page_source)
        for product in sel.css('div.product-card__wrapper'):
            # Simple scraping for every rubashka
            l = ItemLoader(item=WildItem(), selector=product)
            l.default_output_processor = TakeFirst()
            l.add_css('title', 'span.product-card__name::text')
            l.add_css('brand', 'span.product-card__brand::text')
            l.add_css('price', 'ins.price__lower-price::text')
            l.add_css('old_price', 'del::text')
            l.add_css('rating', 'span.address-rate-mini::text')
            l.add_css('review_count',
                      'span.product-card__count::text')
            yield l.load_item()

        next_page = sel.css(
            'a.pagination-next ::attr(href)').extract_first()
        if next_page is not None:
        # Adding new link to the queue
            yield response.follow(next_page, self.parse)

    def load_page(self):
        import time

        time.sleep(1.5)

        # Getting the initial scroll height of the page
        # We decrease height, because we don't need to scroll to the bottom
        page_height = self.driver.execute_script(
            "return document.body.scrollHeight")
        step = 100

        while step < page_height:
            self.driver.execute_script(f"window.scrollTo(0, {step});")
            time.sleep(0.1)

            if step == page_height:
                break

            page_height = self.driver.execute_script(
                "return document.body.scrollHeight") - 300
            step += 450

    def closed(self, reason):
        # Closing driver after scraping is done
        self.driver.close()
