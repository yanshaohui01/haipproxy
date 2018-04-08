#!/usr/bin/env python
#encoding=utf-8
import logging
import threading
import time
from random import choice

from selenium import webdriver
from client.py_cli import ProxyFetcher

args = dict(host='127.0.0.1', port=6379, password='', db=0)
fetcher = ProxyFetcher('zhihu', strategy='greedy', redis_args=args)
# 获取一个可用代理
# print(fetcher.get_proxy())
# # 获取可用代理列表
# print(fetcher.get_proxies()) # or print(fetcher.pool)

class MyThread(threading.Thread):
    def __init__(self, number, logger):
        threading.Thread.__init__(self)
        self.number = number
        self.logger = logger

    def run(self):
        # logger.debug('Calling doubler')
        # doubler(self.number, self.logger)
        url = 'https://www.toutiao.com/ugc/share/thread/1584830061497358/?app=&iid=28571295067&target_app=13&tt_from=weixin&utm_source=weixin&utm_medium=toutiao_ios&utm_campaign=client_share&wxshare_count=1'
        try:
            refresh_html(url)
        except:
            refresh_html(url)



def get_logger():
    logger = logging.getLogger("threading_example")
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler("threading_class.log")
    fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    return logger

def doubler(number, logger):
    logger.debug('doubler function executing')
    result = number * 2
    logger.debug('doubler function ended with: {}'.format(
        result))

def refresh_html(jianshu_url):
    args = dict(host='127.0.0.1', port=6379, password='', db=0)
    fetcher = ProxyFetcher('zhihu', strategy='greedy', redis_args=args)
    while True:
        chromedriverq = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        # 设置chrome代理
        chrome_options = webdriver.ChromeOptions()
        print('--proxy-server={}'.format(choice(fetcher.get_proxies())))
        chrome_options.add_argument('--proxy-server={}'.format(choice(fetcher.get_proxies())))
        browser = webdriver.Chrome(executable_path=chromedriverq, chrome_options=chrome_options)
        browser.get(jianshu_url)
        time.sleep(10)
        # browser.close()
        browser.refresh()

if __name__ == '__main__':
    logger = get_logger()
    thread_names = ['ThreadNum01', 'ThreadNum02', 'ThreadNum03','ThreadNum04', 'ThreadNum05', 'ThreadNum06','ThreadNum07',
                    'ThreadNum08', 'ThreadNum09','ThreadNum10', 'ThreadNum11', 'ThreadNum12','ThreadNum13', 'ThreadNum14',
                    'ThreadNum15','ThreadNum16','ThreadNum17', 'ThreadNum18', 'ThreadNum19','ThreadNum20',]
    for i in range(20):
        thread = MyThread(i, logger)
        thread.setName(thread_names[i])
        thread.start()