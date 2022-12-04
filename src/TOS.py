import requests
import json
from src.config import consumerKey

class TOS:
    #contants
    authUrl = 'https://api.tdameritrade.com/v1/oauth2/token'
    quoteBaseURL = 'https://api.tdameritrade.com/v1/marketdata/'

    def get_quote(self, ticker):
        url = "{}{}{}".format(self.quoteBaseURL,ticker, '/quotes')
        quote = requests.get(url=url, params= {'apikey': consumerKey})
        return ((quote.json()[str(ticker)])['lastPrice'])
    def get_price(self,ticker):
        url = "{}{}{}".format(self.quoteBaseURL,ticker, '/pricehistory')
        param = {
            'apikey' : consumerKey,
            'periodType' : 'year',
            'period' : 3,
            'frequencyType' : 'daily',
            'frequency' : 1
        }
        quote = requests.get(url=url, params=param)
        return (quote.json()['candles'])
    def get_adv(self,ticker):
        price_data = self.get_price(ticker)
        totalVolume = 0;
        for day in price_data:
            totalVolume += day['volume']
        totalVolume = totalVolume / len(price_data)
        return totalVolume

