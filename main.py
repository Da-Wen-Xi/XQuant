from google import genai
import os
import akshare as ak


# os.environ["http_proxy"] = "http://127.0.0.1:7897"
# os.environ["https_proxy"] = "http://127.0.0.1:7897"

if __name__ == '__main__':


    # 2、获取股价在1-30元这个区间的股票代码
    stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20260101", end_date='20260224',
                                            adjust="")
    print(stock_zh_a_hist_df)
    # 3、获取股价在1-30元这个区间的股票代码，获取这些股票代码60天的历史交易数据
    # 4、调用gemini-3-flash-preview模型，分析历史数据，获得当天值得购买的股票信息


    # The client gets the API key from the environment variable `GEMINI_API_KEY`.
    # client = genai.Client(api_key="AIzaSyDJpDBbSDKLHJ5vSbqm7FvV-cvcppsmq9Y")
    # response = client.models.generate_content(
    #     model="gemini-3-flash-preview", contents="Explain how AI works in a few words，用中文解释"
    # )




