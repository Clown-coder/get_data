import pandas as pd
import requests, json

year = '2024'
stock_no = '0050'

# 建立一個空的 DataFrame 來儲存所有月份的數據
all_data = pd.DataFrame()

# 迴圈遍歷1到12月
for month in range(1, 13):
    # 生成對應的日期格式，例如 '20230101', '20230201' 等
    date = f'{year}{month:02d}01'

    # 構建請求的 URL
    url = f'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={date}&stockNo={stock_no}'

    # 發送請求
    response = requests.get(url)

    # 檢查請求是否成功
    if response.status_code == 200:
        content = response.json()

        # 檢查是否有 'data' 和 'fields' 部分
        if 'data' in content and 'fields' in content:
            stock_data = content['data']
            col_name = content['fields']

            # 將數據轉換為 DataFrame
            df = pd.DataFrame(data=stock_data, columns=col_name)

            # 將每個月的數據追加到主 DataFrame 中
            all_data = pd.concat([all_data, df], ignore_index=True)

            print(f"Successfully retrieved data for {year}年{month}月")
        else:
            print(f"No data found for {year}年{month}月")
    else:
        print(f"Failed to retrieve data for {year}年{month}月. Status code: {response.status_code}")

# # 如果有數據，顯示所有數據
# if not all_data.empty:
#     print(all_data)
# else:
#     print("No data retrieved for any month.")
file_name = f'2024.csv'

all_data.to_csv(file_name,index=False,encoding='utf-8-sig')

print(f'Data saved to {file_name}')