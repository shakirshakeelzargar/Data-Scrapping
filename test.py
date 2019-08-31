import requests
import bs4 as bs


res=requests.get('http://www.facebook.com')
pageData=res.text


soup=bs.BeautifulSoup(pageData,'lxml')
print(type(soup))


x=soup.select('title')
print(x)



