from selenium.common.exceptions import NoSuchElementException
import browser
import page
import time
import re

# import numpy as np

url = 'https://store.musinsa.com/app/product/detail/1236270/0'
url2 = 'https://simage-kr.uniqlo.com/goods/31/11/76/04/sizeTable/413977_size.html'


def transpose(mat):
    t_mat = list(map(list, zip(*mat)))
    return


def get_size_from_table(t_head, t_body):
    # 그냥 일단 전부 가져와서 2차원배열로 만들자
    size_table = []
    # t_head part (맨 첫번째 row)
    h = ch.driver.find_elements_by_xpath(f'{t_head}/tr/th')
    num_of_col = len(h)  # column 수
    r1_text = [e.text for e in h]
    size_table.append(r1_text)
    print(f'r1_text: {r1_text}')

    # t_body part ( 나머지 row 들)
    row_body = f'{t_body}/tr'
    num_of_body_row = len(ch.driver.find_elements_by_xpath(row_body))  # body row 수

    # print(f'row: {num_of_body_row}개')
    for i in range(num_of_body_row):
        try:
            # th (가장 왼쪽 셀의 element) 를 row 에 넣어줌
            row = [ch.driver.find_element_by_xpath(f'{row_body}[{i + 1}]/th').text]
            # td (나머지 element) ********************************uniqlo 참고해야겠다
            # td 들을 일단 가져온다 -> row 에 append 해줌
            td_list = ch.driver.find_elements_by_xpath(f'{row_body}[{i + 1}]/td')
            for td in td_list:
                try:
                    c = td.get_attribute('colspan')
                    # print(f'c: {c}')
                    col_span = int(c)
                    for s in range(col_span):
                        row.append(td.text)
                except TypeError:
                    row.append(td.text)
                except Exception as ex:
                    print(f'{type(ex)}: {ex}')
            size_table.append(row[:num_of_col])
        except NoSuchElementException:
            pass
    for r in size_table:
        for c in r:
            print(c, end=' ')
        print('')
    return


ch = browser.Chrome()
ch.move(url)

# size 가 나온 table 의 xpath 를 찾아줘야한다.
# -- id 가 page_product_detail 인 태그를 찾아서 그 자식 노드 중 class 가 ~인 <table> 의 <thead>
t_head_x = '//*[@id="page_product_detail"]/descendant::table[@class="table_th_grey"]/thead'
# t_head_x = '//*[@id="areaContentPopup"]/div[1]/table/thead'
# 마찬가지로 검색해주는 xpath 를 작성해준다
t_body_x = '//*[@id="page_product_detail"]/descendant::table[@class="table_th_grey"]/tbody'
# t_body_x= '//*[@id="areaContentPopup"]/div[1]/table/tbody'

# size_information 가져와서 저장
get_size_from_table(t_head_x, t_body_x)

ch.driver.close()
