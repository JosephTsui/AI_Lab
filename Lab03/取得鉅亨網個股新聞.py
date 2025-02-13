from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')       # 不顯示瀏覽器
chrome_options.add_argument('--no-sandbox')     # 以最高權限運行

