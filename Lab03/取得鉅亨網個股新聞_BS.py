import requests
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
import time

def yahoo_stock(stock_id):
    url = f'https://news.cnyes.com/search?q={stock_id}'
    # 使用 requests 取得網頁內容
    response = requests.get(url)
    html = response.content

    # 使用 BeautifulSoup 解析網頁內容
    soup = BeautifulSoup(html, 'html.parser')
    # 使用 find 與 find_all 定位元素
    # time_element = soup.find('section', \
    #     {'class': 'c1hsmoin'}).find('time')                
    table_soups = soup.find('div',\
        {'class': 'v1xx1i5q'}).find('ul').find_all('li')   

    #fields= []
    datas = []
    for table_soup in table_soups:
        table_datas = table_soup.find_all('div')
        for num, table_data in enumerate(table_datas):
            if table_data.text == '':
                continue
            if num % 2 == 1:
                datas.append(table_data.text)
    
    # 建立 DtaFrame
    df = pd.DataFrame([datas])

    # 回傳 DataFrame
    return df

# 取得台積電股票資訊
df = yahoo_stock('2330')
print(df)

# 練習：抓損益表，資產負債表、現金流量表及季報表