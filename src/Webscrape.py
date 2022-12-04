from selenium.webdriver import Chrome
from bs4 import BeautifulSoup

class Webscrape():
    #constants
    chromeDriver ='C:\Program Files\Google\Chrome\Application\chromedriver.exe'
    tableXPath = '/html/body/form/div[3]/section/ul'
    scrapeURL = 'https://www.earningswhispers.com/calendar?sb=p&d=1&t=all'

    def get_tickers(self):
        tickers = []
        # Setup selenium and grab page to scrape
        driver = Chrome(executable_path=self.chromeDriver)
        driver.get(self.scrapeURL)
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Find the table of earnings tickers
        # itterate over each ticker and load into table
        table = soup.find_all('div',class_='ticker')
        for row in table:
            tickers.append(row.text.strip())
        driver.quit()
        return tickers