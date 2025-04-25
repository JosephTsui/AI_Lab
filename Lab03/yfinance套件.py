import yfinance as yf
import datetime as dt

#指定要下載的股票代碼，上市為 .TW，上櫃為 .TWO
#stock_id='2330.TW'
#支持多檔股票資料下載 (例如台積電、聯電、聯發科)
stock_id=['2330.TW','2303.TW','2454.TW']

#設定開始與結束時間
end = dt.date.today()
start = end - dt.timedelta(days=365)

#下載指定股票的資料
#stock_data = yf.download(stock_id, start=start, end=end)
#下載最近三個月的資料
#stock_data = yf.download(stock_id, period='3mo')
#下載不同時間頻率的資料(1分K)
#stock_data = yf.download(stock_id, interval='1m')
#stock_data.tail()

#取得公司的基本資料、市值、營收等財報資訊
stock = yf.Ticker(stock_id[0])
#info可以獲取公司的基本資料
#stock.info
#infancials 可以取得公司的財報資訊
#financials = stock.financials
#financials.tail()
#法人持股資訊
institutional_holders = stock.institutional_holders
institutional_holders.tail()

