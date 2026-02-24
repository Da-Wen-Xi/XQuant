import os

import pandas as pd
import akshare as ak

cache_file = "stock_zh_a_spot.csv"
cache_file_1_30 = "stock_zh_a_spot_1-30.csv"


if __name__ == '__main__':

# 获取当天大盘数据
    if os.path.exists(cache_file):
        print(f"检测到本地缓存，正在从 {cache_file} 读取数据...")
        # 从本地读取数据
        # index_col=0 是为了防止每次保存都多出一列索引
        stock_zh_a_spot_df = pd.read_csv(cache_file, index_col=0)
    else:
        print("本地无缓存，正在调用 AKShare 接口获取数据...")
        try:
            # 获取数据
            stock_zh_a_spot_df = ak.stock_zh_a_spot()

            # 2. 保存到本地
            # encoding='utf_8_sig' 可以防止在 Excel 中打开时中文乱码
            stock_zh_a_spot_df.to_csv(cache_file, encoding='utf_8_sig')
            print(f"数据已成功保存至本地：{cache_file}")
        except Exception as e:
            print(f"获取数据失败: {e}")
            stock_zh_a_spot_df = None
    stock_1_30 = stock_zh_a_spot_df[
        (stock_zh_a_spot_df['最新价'] >= 1) &
        (stock_zh_a_spot_df['最新价'] <= 30)
        ]
    stock_1_30.to_csv(cache_file_1_30, encoding='utf_8_sig')

    stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="sh601700", period="daily", start_date="20260101", end_date='20260224', adjust="")
    print(stock_zh_a_hist_df)
# 获取60天大盘历史数据
# 获取60天