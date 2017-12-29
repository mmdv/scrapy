import pymysql
from douban import settings

MYSQL_HOSTS = '127.0.0.1'
MYSQL_USER =  'root'
MYSQL_PASSWORD = ''
MYSQL_PORT = '3306'
MYSQL_DB = 'scrapy'

class Sql:
    @classmethod
    #关于 @ classmethod这个是一个修饰符；作用是我们不需要初始化类就可以直接调用类中的函数使用
    def insert_dd_name(cls,item):
        db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='scrapy', charset='utf8')
        cursor = db.cursor()
        print(item['movie_name'])
        sql = "INSERT IGNORE INTO douban (movie_name,price,comment,rank,url) VALUES ('{0}','{1}','{2}','{3}','{4}')".format(item['movie_name'],item['price'],item['comment'],item['rank'],item['url'])
        cursor.execute(sql)
        db.commit()
        db.close()