from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import requests

#constants
chromeDriver ='C:\Program Files\Google\Chrome\Application\chromedriver.exe'
tableXPath = '/html/body/form/div[3]/section/ul'
scrapeURL = 'https://www.earningswhispers.com/calendar?sb=p&d=1&t=all'

def get_tickers():
    tickers = []
    # Setup selenium and grab page to scrape
    driver = Chrome(executable_path=chromeDriver)
    driver.get(scrapeURL)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Find the table of earnings tickers
    # itterate over each ticker and load into table
    table = soup.find_all('div',class_='ticker')
    for row in table:
        tickers.append(row.text.strip())
    driver.quit()
    return tickers

tic = get_tickers()
for t in tic:
    print(t)
