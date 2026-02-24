import pandas as pd
import akshare as ak

# 1. 获取数据
df = ak.fund_portfolio_hold_em(symbol="018957", date="2025")

# 2. 定义中英文映射字典
column_mapping = {
    '股票代码': 'stock_code',
    '股票名称': 'stock_name',
    '占净值比例': 'weight_pct',
    '持股数': 'shares_held',
    '持仓市值': 'market_value',
    '季度': 'quarter'
}

# 3. 批量重命名列名
df = df.rename(columns=column_mapping)

# 4. 数据过滤与去重
df['weight_pct'] = pd.to_numeric(df['weight_pct'], errors='coerce')
df = df[df['weight_pct'] > 1].drop_duplicates(subset=['stock_code'], keep='first').sort_values(by='weight_pct', ascending=False)

# 6. 最终只保留需要的英文列
df_final = df[['stock_code', 'stock_name', 'weight_pct']].reset_index(drop=True)

# 打印结果
pd.set_option('display.max_rows', None)
print(df_final)