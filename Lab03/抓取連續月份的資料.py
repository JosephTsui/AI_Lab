import requests
import pandas as pd
import datetime as dt
from dateutil.relativedelta import relativedelta

# 輸入股票代號
stock_id ='2330'

# 設定抓取幾個月資料
mon_num = 3
date_now = dt.datetime.now()

# 建立日期字串
date_list = [(date_now - relativedelta(months=i)).replace(day=1).\
    strftime('%Y%m') for i in range(mon_num)]

date_list.reverse()
all_df = pd.DataFrame()

# 使用迴圈抓取連續月份資料
for date in date_list:
    url = f'https://www.twse.com.tw/rwd/zh/aftertrading/StOCK_DAY?date={date}&stockNo={stock_id}'
    try:
        json_data = requests.get(url).json()
        df = pd.DataFrame(data=json_data['data'], columns=json_data['fields'])
        all_df = pd.concat([all_df, df], ignore_index=True)
    except Exception as e:
        print(f"無法取得{date}的資料，可能資料量不足")

all_df.head()