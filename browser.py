from selenium import webdriver as wb
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time


class Chrome(object):
    def __init__(self):
        path = '/home/hero/utils/chromedriver'
        self.driver = wb.Chrome(path)

    def move(self, url):
        self.driver.get(url)
        time.sleep(5)

    def click_by_xpath(self, xpath):
        # 2가지 경우 빼고 raise 를 일으켜는 방식 고려******************
        try:
            self.driver.find_element_by_xpath(xpath).click()
            time.sleep(5)
            print(f'click {self.driver.current_url}')
        except ElementNotInteractableException:
            self.driver.find_element_by_xpath(xpath).send_keys(Keys.ENTER)
            time.sleep(5)
            print(f'click {self.driver.current_url}')
        # except NoSuchElementException:
        #     print('이런거 없음')
        # except Exception as ex:
        #     print(f'{type(ex)}: {ex}')
        #     print('click 할 수 없는 부분')
        # time.sleep(5)
        return
