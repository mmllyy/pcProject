# 配置
# 配置请求头
headers = {
    'User-Agent':'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}

# 配置代理
proxies = {
    'http':'123.57.207.2:3128',
    'https':'123.57.207.2:3128'
}

# 配置爬虫的起始位置
start_url = 'https://www.qiushibaike.com'

# 配置xpath路径
author_path = '//div[starts-with(@class,"author")]'
home_path = './a/@href'
src_path = './a/img/@src'
name_path = './a/h2/text()'
next_page_path = '//ul[@class="pagination"]/li[last()]/a/@href'
age_path = './div/text()'
#配置数据库
DATABASE = {
    #参考pymysql.connect()函数中的参数
    'default':{
        'host':'10.35.163.12',
        'port':3306,
        'user':'root',
        'password':'root',
        'db':'qiubai',
        'charset':'utf8'
    }
}
