from lxml import etree  # 获取网页的定位
import requests  # 下载器
import pandas as pd
import time

for i in range(2015,2022): #用列表获取数据序列
    # %d 取整数  %s 取字符串 %f 取浮点数
    urls = ["https://ranking.promisingedu.com/%d-qs-all-undergraduate"%i]

    # 请求建立一个会话
    session = requests.Session()

    # 遍历urls 获取地址
    for url  in urls:
        # 使用get方法 获取响应
        response = session.get(url,headers={
            'User-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400'
        })
        # 将内容以文本显示
        content = response.text

    # 解析网页
    html = etree.HTML(content)
    time.sleep(1)
    # 品牌  价格   销量
    # /html/body/div[6]/div/div[3]/div[2]/table/tbody//td[2]

    University = html.xpath('//table[@id="rk"]//td[2]//text()')[:200]

    Country = html.xpath('//table[@id="rk"]//td[3]//text()')[:200]

    Rank = html.xpath('//table[@id="rk"]//td[1]//text()')[:200]

    Overall_Score = html.xpath('//table[@id="rk"]//td[10]//text()')[:200]

    Year = str(i).split()*200


    Content = {"Rank":Rank,"University":University,"Country":Country,"Overall_Score":Overall_Score,"Year":Year}
    New = pd.DataFrame(Content)
    New.to_csv("世界大学排名_%d.csv"%i)
    print(New)
