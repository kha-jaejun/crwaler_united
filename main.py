from selenium.common.exceptions import NoSuchElementException

import page
import browser
# import settings
import re


def count_xpath_children(xpath):
    if xpath[-3] == '[' and xpath[-1] == ']':
        xpath = xpath[:-3]
    return len(ch.driver.find_elements_by_xpath(xpath))




def add_xpath(xpath, idx_tail, subs, num, suffix_x):
    try:
        if idx_tail == num:
            xpath = xpath + suffix_x
            print(xpath, end='---')
            print('all filled!!')
            # **************************************************************
            # <category xpath 일 경우>
            # ch.click_by_xpath(pre_xpath)  # 최상위카테 눌러주고
            # con = ch.driver.find_element_by_xpath(xpath).text  # text 확인
            # print(con)
            # if: text 가 미리 정해둔 키워드일 경우: click 해서 들어간다
            # ch.click_by_xpath(xpath)
            # category_page 업무 수행 ***************************************
            # ch.driver.back()  # 뒤로가기

            # <product xpath 일 경우>
            # 클릭해서 상품페이지로 이동: 클릭이 안 될 경우(error) pass
            # ch.click_by_xpath(xpath)
            # print('click success!!!')
            # product page 업무 수행 *****************************************
            # ch.driver.back()
            return
        # print(f'add {idx_tail}-th tail..')
        # tail 을 붙인다
        added_xpath = xpath + '/' + subs[idx_tail]
        ch_num = count_xpath_children(added_xpath)
        if ch_num > 1:
            for idx in range(ch_num):
                d_added_xpath = added_xpath + f'[{idx + 1}]'
                # print(d_added_xpath)
                add_xpath(d_added_xpath, idx_tail + 1, subs, num, suffix_x)
        else:
            # print(added_xpath)
            add_xpath(added_xpath, idx_tail + 1, subs, num, suffix_x)

    except NoSuchElementException:
        print('Error 2 Crawling Product')
    except Exception as ex:
        print(f'{type(ex)}: {ex}')


def cir_xpath(static_x, mobile_x, suffix_x=''):
    print('cir_xpath method start')

    # 뒷부분(변하는 부분) (tail)
    dif = len(static_x) - len(mobile_x)
    tail = mobile_x[dif:]
    print(f'tail: {tail}')
    # index 부분을 없앤다 (p_tail)
    p_tail = re.compile('\\[\\d\\]').sub('', tail)
    print(f'processed tail: {p_tail}')
    # tag 별로 쪼갠다 (sub_tails)
    sub_tails = re.split('/', p_tail)
    print(f'sub_tails: {repr(sub_tails)}')
    num_tails = len(sub_tails)

    add_xpath(static_x, 1, sub_tails, num_tails, suffix_x)

    print('cir_xpath method end')
    return


# 사이트 입력
# site = input('사이트를 입력하세요!')
site = 'https://store-kr.uniqlo.com/'

# 사이트 등록
# enroll site
print('enroll site!')
# fill category
print('fill category!')
# init history
print('init history!')

# chrome browser
ch = browser.Chrome()
# main page
main_page = page.Page(site, ch)
ch.move(site)       # move to main page!

# 최상위 카테고리
first_depth_xpath = '/html/body/div[2]/div[1]/div[1]/div[1]/ul/li[1]'
stat = re.compile('/[^/]+$').sub('', first_depth_xpath)
# 최하위 카테고리
last_depth_xpath = '/html/body/div[2]/div[1]/div[1]/div[1]/ul/li[1]/div/div[3]/div[1]/ul/li[4]'

# move to category page
cir_xpath(stat, last_depth_xpath)

# cate_url = 'https://store-kr.uniqlo.com/display/displayShop.lecs?storeNo=83&siteNo=50706&displayNo=NQ1A01A12A03'
# ch.move(cate_url) : category page 에 접속했다는 가정 하에
stat = '//*[@id="content1"]'                        # 앞
mobile = '//*[@id="content1"]/div[3]/div/ul/li'     # 완성 예시
suffix = '/div[1]/p/a'                              # 뒤
cir_xpath(stat, mobile, suffix)

ch.driver.close()
