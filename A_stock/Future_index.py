#! -*- coding:utf-8 -*-
import datetime
import time

import pymysql
import requests
from lxml import etree
from selenium import webdriver

driver = webdriver.Chrome()
# 把find_elements 改为　find_element
def get_first_page():

    url = 'http://q.stock.sohu.com/cn/600064/lshq.shtml'
    driver.get(url)
    driver.find_element_by_xpath('<li class="current">历史行情<em></em></li>').click()
    driver.find_element_by_xpath('//*[@id="BIZ_lshq_sd"]').click()
    driver.find_element_by_xpath('//*[@id="title_year"]').send_keys("2013") #选择日期
    driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div[2]/div/div[1]/form/input[7]').click()
    html = driver.page_source
    return html





# 把首页和翻页处理？

def next_page():
    for i in range(1,32):  # selenium 循环翻页成功！
        driver.find_element_by_xpath('//*[@id="resultList"]/div[55]/div/div/div/ul/li[last()]/a').click()
        time.sleep(1)
        html = driver.page_source
        return html



def parse_html(html):  # 正则专门有反爬虫的布局设置，不适合爬取表格化数据！
    big_list = []
    selector = etree.HTML(html)
    time = selector.xpath('//*[@id="BIZ_hq_historySearch"]/tbody/tr/td[1]')
    link = selector.xpath('//*[@id="BIZ_hq_historySearch"]/tbody/tr/td[3]/text()')
    long_tuple = (i for i in zip(time[1:], link[0:]))
    for i in long_tuple:
        big_list.append(i)
    return big_list


        # 存储到MySQL中

def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                 db='JOB',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany('insert into GoTo_j1 (jobs,link,firms) values (%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration:
        pass




#
# if __name__ == '__main__':
#         html = get_first_page()
#         content = parse_html(html)
#         time.sleep(1)
#         insertDB(content)
#         while True:
#             html = next_page()
#             content = parse_html(html)
#             insertDB(content)
#             print(datetime.datetime.now())
#             time.sleep(1)

html = get_first_page()
content = parse_html(html)
print(content)

# #
# create table GoTo_j1(
# id int not null primary key auto_increment,
# jobs varchar(80),
# link varchar(88),
# firms varchar(80)
# ) engine=InnoDB  charset=utf8;