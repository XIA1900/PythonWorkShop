#当直接使用requests时，知乎拒绝访问，无法获取页面，从user-agent判断出是个bot，就直接被拒了
#更改user-agent为普通浏览器，则获取到的是登录页面
import sys
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os


reload(sys)
sys.setdefaultencoding('utf-8')
url='https://www.zhihu.com/'
# browser=webdriver.Chrome()
# browser.get(url)
try:
    kv={'user-agent':'Mozilla/5.0'}
    r=requests.get(url,timeout=30)#,headers=kv)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    text=r.text
except:
    print('error')

file=open('/Users/user/Desktop/'+'text'+'.txt','w')
file.write(text)



# soup=BeautifulSoup('r.text','lxml')
# demo=soup.find(attrs={'class':'SignFlowHeader-slogen'})
# print(demo)
