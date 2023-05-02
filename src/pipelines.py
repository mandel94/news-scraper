from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags
import json
from itemadapter import ItemAdapter

from items import ArticleItem

class ArticleLoader(ItemLoader):
    default_item_class = ArticleItem
    default_output_processor = TakeFirst()

    title_in = MapCompose(remove_tags, str.strip)
    title_out = Join()

    url_in = MapCompose(remove_tags, str.strip)
    url_out = Join()

    description_in = MapCompose(remove_tags, str.strip)
    description_out = Join()

    image_src_in = MapCompose(remove_tags, str.strip)
    image_src_out = Join()

    content_in = MapCompose(remove_tags, str.strip)
    content_out = Join()

    author_in = MapCompose(remove_tags, str.strip)
    author_out = Join()

    category_in = MapCompose(remove_tags, str.strip)
    category_out = Join()

    tags_in = MapCompose(remove_tags, str.strip)
    tags_out = Join()

    publish_date_in = MapCompose(remove_tags, str.strip)
    publish_date_out = Join()


# Write pipeline to load into Database
class JsonWriterPipeline:

    def open_spider(self, spider):
        self.file = open('../items.jsonl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        return item