#爬取豆瓣其他页面：第一次尝试爬取纪录片的简介；刚开始用 demo=soup.find('span','v:summary') ，失败了；后来换了方法成功了


import sys
import requests
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')
url="https://movie.douban.com/subject/30263943/"
try:
    r=requests.get(url,timeout=30)
    r.raise_for_status()
    r.edncoding=r.apparent_encoding
except:
    print('error')

soup=BeautifulSoup(r.text,'html.parser')
demo=soup.find(attrs={'property':'v:summary'})
print(demo.text)

#demo=soup.find('span','v:summary')   -> failure
