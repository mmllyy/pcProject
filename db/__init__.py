import pymysql
import settings
from item import UserItem


class DBHelp():
    def __init__(self):
        self.db = pymysql.connect(**settings.DATABASE.get('default'))
        self.cursor = self.db.cursor()

    def save(self,item):
        if isinstance(item,UserItem):
            if self.exist('user',item.id):
                return
            self.cursor.execute('insert user(id,name,age,img,home) values(%s,%s,%s,%s,%s)',
                                args=(item.id,
                                      item.name,
                                      item.age,
                                      item.img,
                                      item.home))
        if self.cursor.rowcount:
            print(item.name,'数据保存成功')
            self.db.commit()

    def exist(self, tableName, id):
        self.cursor.execute('select id from {} where id=%s'.format(tableName),
                            args=(id))

        return self.cursor.rowcount >= 1


    def close(self):
        self.db.close()



