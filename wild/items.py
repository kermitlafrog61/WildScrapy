import re

import scrapy
from itemloaders.processors import MapCompose


def extract_int(s: str):
    # Finding every appearance of an integer in the string
    int_groups = re.findall(r'\d+', s)

    if not int_groups:
        return 0

    int_value = int(''.join(int_groups))

    return int_value


class WildItem(scrapy.Item):
    title = scrapy.Field()
    brand = scrapy.Field()
    price = scrapy.Field(
        input_processor=MapCompose(extract_int))
    old_price = scrapy.Field(
        input_processor=MapCompose(extract_int))
    rating = scrapy.Field(input_processor=MapCompose(float))
    review_count = scrapy.Field(
        input_processor=MapCompose(extract_int))
