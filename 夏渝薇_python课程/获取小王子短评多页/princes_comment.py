#抓取小王子短评多页

import sys
import requests
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")
url="https://book.douban.com/subject/1084336/comments/hot?p="
try:
    for i in range(1,5):
        r=requests.get(url+str(i),timeout=30)
        r.raise_for_status()
        r.edncoding=r.apparent_encoding
        soup=BeautifulSoup(r.text,'lxml')
        pattern=soup.find_all('span','short')
        print("page "+str(i))
        for item in pattern:
            print(item.string)
except:
    print("error")
