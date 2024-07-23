from bs4 import BeautifulSoup
from selenium import webdriver as webdr
from selenium.webdriver.common.by import By
import time
import requests
import re

class PropertyParse:
    def __init__(self):
        None
        
    def Price(self, pages : int) -> str:
        browser = webdr.Chrome()
        browser.get("https://realty.ya.ru/moskva/kupit/kvartira/")
        browser.implicitly_wait(2)
        all_prices : list = []
        page_num = 0
        while page_num < pages:
            try:
                soup = BeautifulSoup(browser.page_source) 
            except Exception:
                browser.close()
                return None
            prices = soup.find_all("div", "OfferPriceLabel__priceWithTrend--1_AZI")
            for i in range(len(prices)):
                prices[i] = ''.join(((re.findall(r"\d+", str(prices[i])))[1:4]))
            for i in range(len(prices)):
                all_prices.append(int(prices[i]))
            page_num += 1
            pager_button = browser.find_element(By.LINK_TEXT, "Следующая")
            #print(pager_button.text)
            pager_button.click()
            browser.get(f"https://realty.ya.ru/moskva/kupit/kvartira/?page={page_num}")
            print(f"page {page_num} end")
            time.sleep(2)
            #browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            del prices
            del soup
        browser.close()
        return all_prices
    
    def Parse():
        req = requests.get("https://realty.ya.ru/moskva/kupit/kvartira/")
        src = req.text

if __name__ == "__main__":
    PropParse = PropertyParse()
    #print(PropParse.Price(10))
    #print(PropParse.Square(5))
