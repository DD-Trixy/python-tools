# coding:utf-8
import requests
from bs4 import BeautifulSoup
import webbrowser

r = requests.get('http://www.yxdown.com/')
r.encoding = 'gbk'

soup = BeautifulSoup(r.text, 'lxml')
tree = soup.find_all('li',class_="top")

newsData = []
linkData = []

for i,x in enumerate(tree):
# limit the amout of news to get correct info
  if i>31:
    break
  item = x.get_text()
  newsData.append(item[:-4])
  a = x.span.i.a
  linkData.append(a['href'])

def setData(l):
  if not newsData:
    return
  for m,n in enumerate(newsData):
    l.insert('end', n)
    if m%2 == 0:
      l.itemconfigure(m, background='#f0f0ff')
  l.bind('<<ListboxSelect>>', getIndex)

def query():
  link = linkData[index]
  webbrowser.open(link)


def about():
  webbrowser.open('www.chunqiuyiyu.com')

def getIndex(e):
  global index
  tmp = e.widget.curselection()
  index = tmp[0]
