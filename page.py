import browser
import requests as rq
from bs4 import BeautifulSoup as Bs
import urllib
import re
import time
import os


class Page(object):

    def __init__(self, url, ch: browser.Chrome):
        self.url = url
        self.ch = ch
        # Bs 사용 준비
        res = rq.get(self.url)
        self.html = Bs(res.content, 'html.parser')


class ListPage(Page):
    # page 가 여러개라면
    def nnn(self):
        print('nnnnn')
    # 그냥 스크롤을 내리는 사이트 (유니클로, 나이키?, 아디다스?)


class ProductPage(Page):

    def get_basic_info(self):
        return

    def save_image(self):
        return

    def get_size_info(self):
        t_head = ''
        t_body = ''
        return
