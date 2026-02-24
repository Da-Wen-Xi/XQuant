import os
import akshare as ak
import akshare_proxy_patch



# os.environ["http_proxy"] = "http://127.0.0.1:7897"
# os.environ["https_proxy"] = "http://127.0.0.1:7897"
if __name__ == '__main__':
    akshare_proxy_patch.install_patch("101.201.173.125", "", 30)
    stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="601700", period="daily", start_date="20240301", end_date='20240528',
                                            adjust="")
    print(stock_zh_a_hist_df)