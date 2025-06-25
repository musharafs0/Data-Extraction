
import scrapy

class BayutItem(scrapy.Item):
    property_id = scrapy.Field()
    property_url = scrapy.Field()
    purpose = scrapy.Field()
    type = scrapy.Field()
    added_on = scrapy.Field()
    furnishing = scrapy.Field()
    price = scrapy.Field()
    location = scrapy.Field()
    bed_bath_size = scrapy.Field()
    permit_number = scrapy.Field()
    agent_name = scrapy.Field()
    primary_image_url = scrapy.Field()
    breadcrumbs = scrapy.Field()
    amenities = scrapy.Field()
    description = scrapy.Field()
    property_image_urls = scrapy.Field()
