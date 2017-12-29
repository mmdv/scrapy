from .sql import Sql
from dingdian.items import DingdianItem

class DingdianPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,DingdianItem):
            Sql.insert_dd_name(item)
        return item
