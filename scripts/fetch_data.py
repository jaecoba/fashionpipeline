from pytrends.request import TrendReq
import pandas as pd


def fetch_trends(keywords):

    pytrends = TrendReq(hl='US', tz=360)

    pytrends.build_payload(keywords, cat=0, timeframe='today 1-m', geo='US', gprop='')

    data = pytrends.interest_over_time()

    return data

if __name__ == "__main__":
    #'cargo pants', 'dress pants', 'blue jeans', 'black jeans', 
    keywords = ['dress pants', 'blue jeans', 'black jeans', 'dress pants','straight jeans', 'baggy jeans', 'bootcut jeans']
    trend_data = fetch_trends(keywords)
    trend_data.to_csv('data/trend_data.csv', index=False)