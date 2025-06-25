import scrapy

class BayutSpider(scrapy.Spider):
    name = "bayut_spider"
    allowed_domains = ["bayut.com"]
    start_urls = ["https://www.bayut.com/to-rent/property/dubai/"]

    def parse(self, response):
        listings = response.css('a[aria-label="Listing link"]::attr(href)').getall()
        for href in listings:
            full_url = response.urljoin(href)
            yield scrapy.Request(full_url, callback=self.parse_listing)

        next_page = response.css('a[aria-label="Next"]::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)


    def parse_listing(self, response):
        title = response.css('h1::text').get()
        price = response.css('span[aria-label="Price"]::text').get()

        yield {
            'title': title,
            'price': price,
            'url': response.url
        }


