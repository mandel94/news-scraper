from dataclasses import dataclass
from scrapy import Field

@dataclass
class ArticleItem:
    title = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()
    content = scrapy.Field()
    image_src = scrapy.Field()
    publish_date = scrapy.Field()
    author = scrapy.Field()
    category = scrapy.Field(defalut="NULL")
    tags = scrapy.Field(default="NULL")