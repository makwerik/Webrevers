import time
import random
import csv

from bs4 import BeautifulSoup
from fake_useragent import UserAgent

import undetected_chromedriver as uc
from undetected_chromedriver.webelement import *
from undetected_chromedriver import ChromeOptions


class IndiaKek:
    def __init__(self):
        """Initializing the uc browser"""

        useragent = UserAgent()
        options = ChromeOptions()
        options.headless = False
        options.add_argument(f"User-Agent={useragent.random}")

        self.driver = uc.Chrome(options=options)

    def __writing_csv(self, data: dict):
        """Method for writing data to csv"""
        with open('result_india.csv', 'a', encoding='utf8') as f:
            write = csv.writer(f)
            write.writerow((data['name'],
                            data['price']))

    def get_data(self):
        """The method for getting the price and name"""

        self.driver.get('https://www.nseindia.com/')
        self.driver.find_element(By.CSS_SELECTOR, '#link_2').click()

        time.sleep(random.randint(2, 4))

        self.driver.find_element(By.CSS_SELECTOR,
                                 '#main_navbar > ul > li:nth-child(3) > div > div.container >'
                                 ' div > div:nth-child(1) > ul > li:nth-child(1) > a').click()

        time.sleep(random.randint(2, 4))

        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        tbody = soup.find('table', id='livePreTable').find('tbody')
        trs = tbody.find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            try:
                name = tds[1].find('a', class_='symbol-word-break').text
                price = tds[6].text
                data = {'name': name, 'price': price}
                self.__writing_csv(data)
            except AttributeError as e:
                break

    def imitation_of_a_human(self):
        """The method is imitation of a person"""

        y = 100
        for timer in range(0, 10):
            self.driver.execute_script("window.scrollTo(0, " + str(y) + ")")
            y += 100
            time.sleep(0.32)

        self.driver.find_element(By.CSS_SELECTOR, 'body > header > nav > div.container.top_logomenu > a > img').click()
        time.sleep(random.randint(2, 4))
        self.driver.find_element(By.CSS_SELECTOR, '#tabList_NIFTYBANK').click()
        time.sleep(random.randint(2, 4))

        y = 100
        for timer in range(0, 5):
            self.driver.execute_script("window.scrollTo(0, " + str(y) + ")")
            y += 100
            time.sleep(0.32)

        self.driver.find_element(By.CSS_SELECTOR, '#tab4_gainers_loosers > div.link-wrap > a').click()
        time.sleep(random.randint(4, 8))

        self.driver.find_element(By.CSS_SELECTOR, '#market-Svn-gold-bond').click()
        time.sleep(random.randint(4, 8))


if __name__ == '__main__':
    run = IndiaKek()
    run.get_data()
    run.imitation_of_a_human()
    run.driver.close()
    time.sleep(2)
