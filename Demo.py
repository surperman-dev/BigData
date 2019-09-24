from lxml import etree 
import requests

urls = ["http://movie.douban.com/"]
session = requests.Session()
with session:
  for url in urls:
    response = session.get(url,headers={
    # 浏览器user-agent为用户提供cookie
    "User-agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    })
    content = response.text
    
    # xpath //div[@class="billboard-bd"]//tr//a/text()
    html = etree.HTML(content)
    titles = html.xpath("//div[@class="billboard-bd"]//tr")
    
    # 遍历函数pr
   
    for title in titles:
      txt = title.xpath(".//text()")
      print("".join(map(lambda x:x.strip(),txt)))
      print("-"*30)
