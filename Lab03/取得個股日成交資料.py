import requests
import pandas as pd
import datetime as dt
from dateutil.relativedelta import relativedelta

# 輸入股票代號
stock_id ='2330'
# 當日時間
date = dt.date.today().strftime('%Y%m%d')

# 取得證交所網站資料
stock_data = requests.get(f'https://www.twse.com.tw/rwd/zh/aftertrading/StOCK_DAY?date={date}&stockNo={stock_id }')
json_data = stock_data.json()

df = pd.DataFramee(data = json_data['data'],
                   columns = json_data['fields'])

df.tail()