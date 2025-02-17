from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')       # 不顯示瀏覽器
chrome_options.add_argument('--no-sandbox')     # 以最高權限運行

# 透過 options 設定 driver
driver = webdriver.Chrome(options=chrome_options)
data2 = [] # 表格數據

# 目前網址
url=f"https://news.cnyes.com/search?q=2330"
driver.get(url)

# 模擬滑動滑鼠滾輪的行為，用於加截更多內容
scroll_pause_time = 2   # 等待時間
last_height = driver.execute_script("return document.body.scrollHeight") # 網頁高度
