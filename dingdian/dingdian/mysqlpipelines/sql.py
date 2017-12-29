import pymysql
from dingdian import settings

MYSQL_HOSTS = '127.0.0.1'
MYSQL_USER =  'root'
MYSQL_PASSWORD = ''
MYSQL_PORT = '3306'
MYSQL_DB = 'db3'

class Sql:
    @classmethod
    def insert_dd_name(cls,item):
        db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='db3', charset='utf8')
        cursor = db.cursor()
        print(item['name'],'--------------------')
        print(type(item['name']))
        print(item['name'][0])
        print(item['name'].__len__())
        print(len(item['name']))
        for i in range(len(item['name'])):
            sql = "INSERT IGNORE INTO dd_name (xs_name,xs_author,category,name_id) VALUES ('{0}','{1}','{2}','{3}')".format(item['name'][i],item['author'][i],item['category'][0],item['name_id'])
            cursor.execute(sql)
        db.commit()
        db.close()