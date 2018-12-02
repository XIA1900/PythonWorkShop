#读取热门音乐人，锚文本的形式
import sys
import requests
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')
url='https://music.douban.com/artists/'
try:
    r=requests.get(url,timeout=30)
    r.raise_for_status()
    r.edncoding=r.apparent_encoding
except:
    print('error')

soup=BeautifulSoup(r.text,'lxml')
demo=soup.find_all('span','artist-name')
print("Hot musicians")
for i in demo:
    demo1=i.select('a')[0].text
    print(demo1)
