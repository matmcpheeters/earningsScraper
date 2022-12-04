#!/usr/bin/python
from src.Webscrape import Webscrape
from src.TOS import TOS
def main():
    #init helper objects
    data = Webscrape()
    broker = TOS()

    tic = data.get_tickers()

    print("ticker,lastPrice,AverageDailyVolume")
    for t in tic:
        quote = str(broker.get_quote(t))
        adv = broker.get_adv(t)
        line = "{},{},{}".format(t,quote,adv)
        print(line)

if __name__ == "__main__":
   main()