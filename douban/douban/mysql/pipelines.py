from .sql import Sql
from douban.items import DoubanItem

class DoubanPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,DoubanItem):
            Sql.insert_dd_name(item)
        return item
