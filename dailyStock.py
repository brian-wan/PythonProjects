from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Stock:
    def __init__(self):
        pass

    def get_prices(self):
        browser = webdriver.Firefox()
        stocks = ['netflix', 'costco', 'nasdaq', 'intel', 'voo']
        for stock in stocks:
            browser.get('http://google.com')
            searchElem = browser.find_element_by_name('q')
            searchElem.send_keys(stock + ' price')

            enterElem = browser.find_element_by_name('btnK')
            enterElem.submit()
            time.sleep(3)

            priceElem = browser.find_element_by_class_name(
                "gsrt")
            print(stock + ': ' + priceElem.text)
        browser.quit()


browser = webdriver.Firefox()
stocks = ['netflix', 'costco', 'nasdaq', 'intel', 'voo']
for stock in stocks:
    browser.get('http://google.com')
    searchElem = browser.find_element_by_name('q')
    searchElem.send_keys(stock + ' price')

    enterElem = browser.find_element_by_name('btnK')
    enterElem.submit()
    time.sleep(3)

    priceElem = browser.find_element_by_class_name(
        "gsrt")
    print(stock + ': ' + priceElem.text)
browser.quit()
