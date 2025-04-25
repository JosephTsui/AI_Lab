from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')       # 不顯示瀏覽器
chrome_options.add_argument('--no-sandbox')     # 以最高權限運行

stock_id = '2330' # 股票代號

# 透過 options 設定 driver
driver = webdriver.Chrome(options=chrome_options)
data2 = [] # 表格數據

# 目前網址
url=f"https://news.cnyes.com/search?q={stock_id}"
driver.get(url)

# 模擬滑動滑鼠滾輪的行為，用於加截更多內容
scroll_pause_time = 2   # 等待時間
last_height = driver.execute_script("return document.body.scrollHeight") # 網頁高度

while True:
    # 滾動到底部
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # 等待加載
    time.sleep(scroll_pause_time)
    # 計算新的網頁高度
    new_height = driver.execute_script("return document.body.scrollHeight")
    # 如果網頁高度沒有變化，則停止滾動
    if new_height == last_height:
        break
    last_height = new_height

elements = driver.find_elements("xpath", '/html/body/div[2]/main/div/div/div[1]')
#擷取網址和標題
for element in elements:
    link = element.get_attribute("href")
    title = element.text
    title = title.split("\n")
    data2.append([stock_id, title[1], title[0], link])

driver.quit() # 關閉瀏覽器
#使用 requests 前往網址擷取新聞內容
for link in data2:
    link_a = requests.get(link[3]).content
    link_b = BeautifulSoup(link_a, 'html.parser ')
    p_elements = link_b.find('div', {'class':'v1cp4m9y'})
    #取得段落內容
    link[3] = p_elements.text

#建立表格
df = pd.DataFrame(data2, columns=['股票代號', '日期', '標題'])
print(df.tail())