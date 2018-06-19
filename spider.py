import ssl
from urllib import request
import os
from db import DBHelp
from item import UserItem
from lxml import etree
import settings


class QiuBaiSpider():
    def __init__(self):
        self.db = DBHelp()
        ssl._create_default_https_context = ssl._create_unverified_context
        print('爬虫开始行动了。。。')
    def __del__(self):
        print('感谢有你，我要走了。。。')
        self.db.close()

    def run(self):
        next_url = settings.start_url
        while True:
            html = self.request(next_url)
            # self.parse(html)
            next_url = self.parse(html)
            if not next_url:
                break


    def request(self,url):
        print('路径',url)
        req = request.Request(url,headers=settings.headers)
        resp = request.urlopen(req)
        if resp.status == 200:
            print('ok')
            html = resp.read().decode()
            # print(html)
            return html

    def parse(self,html):
        et = etree.HTML(html)
        authors = et.xpath(settings.author_path)
        #print(authors)
        for author in authors:
            try:
                home = author.xpath(settings.home_path)[0]
                #print(home)
                id = home.split('/')[-2]
                name = author.xpath(settings.name_path)[0]
                age = author.xpath(settings.age_path)[0]
                img = 'http:'+author.xpath(settings.src_path)[0].split('?')[0]
            except:
                pass
                #print('ddd')
            else:
                item = UserItem(id,name,age,img,home)
                # 将数据存入数据库
                self.db.save(item)
                self.saveImg(img,id)

        # 读取下一页的连接
        try:
            next_url = settings.start_url+et.xpath(settings.next_page_path)[0]
        except:
            return False
        else:
            return next_url


    def saveImg(self,url,id):
        filename = './head/{}.{}'.format(id,url.split('.')[-1])
        if os.path.exists(filename):
            return
        request.urlretrieve(url,filename=filename)
        print(filename,'图片下载成功')

if __name__ == '__main__':
    QiuBaiSpider().run()