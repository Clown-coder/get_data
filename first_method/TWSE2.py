import pandas as pd
import requests, json

# 設定日期和股票代號
date = '20240901'
stock_no = '0050'

# 構建正確的請求 URL，確保 date 參數正確傳遞
url = requests.get(f'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={date}&stockNo={stock_no}')

# 解析 JSON 回應
content = url.json()  # 使用 requests 自帶的 .json() 方法

# 提取所需的數據
stock_data = content['data']
col_name = content['fields']

# 將數據轉換為 DataFrame
df = pd.DataFrame(data=stock_data, columns=col_name)


# print(df)

output_data={
    'field': col_name,
    'data' : stock_data
}


file_name = f'stock_data_{stock_no}_{date}.csv'
df.to_csv(file_name,index=False,encoding='utf-8-sig')

print(f'Data saved to {file_name}')