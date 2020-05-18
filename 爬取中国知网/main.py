from selenium import webdriver

from lxml import etree

import time

from ways import get_data

import random


def pasre_page(driver):
    html = etree.HTML(driver.page_source)

    trs = html.xpath('//tr[@bgcolor]')

    for tr in trs:

        title = tr.xpath('./td//a[@class="fz14"]/text()')[0]

        authors = tr.xpath('./td[@class="author_flag"]/a[@class="KnowledgeNetLink"]//text()')

        authors = "|".join(authors)

        source = tr.xpath('./td//a[@target="_blank"]/text()')[1]

        times = tr.xpath('./td[@align="center"]/text()')[0].strip()

        database = tr.xpath('./td[@align="center"]/text()')[1].strip()

        counted = tr.xpath('./td//span[@class="KnowledgeNetcont"]/a/text()')

        if len(counted) == 0:

            counted = 0

        else:

            counted = counted[0]

        downloadCount = tr.xpath('./td//span[@class="downloadCount"]/a/text()')

        if len(downloadCount) == 0:

            downloadCount = 0

        else:

            downloadCount = downloadCount[0]

        data = {

            "title": title,

            "authors": authors,

            "source": source,

            "times": times,

            "database": database,

            "counted": counted,

            "downloadCount": downloadCount,

        }

        datas.append(data)

        print(title)

    time.sleep(random.uniform(2, 4))

    driver.switch_to.parent_frame()

    search_win = driver.find_element_by_id('expertvalue')

    search_win.clear()

    time.sleep(random.uniform(2, 4))


driver_path = r"C:\Users\FGHH\AppData\Local\Google\Chrome\Application\chrome.exe"

driver = webdriver.Chrome(executable_path=driver_path)

url = "https://www.cnki.net/"

driver.get(url)

home_page = driver.find_element_by_id('highSearch')

home_page.click()

driver.switch_to_window(driver.window_handles[1])

search_page = driver.find_element_by_id('1_3')

search_page.click()

datas = []

results = get_data()

for result in results:
    search_win = driver.find_element_by_id('expertvalue')

    search_win.send_keys(result)

    search_btn = driver.find_element_by_id('btnSearch')

    search_btn.click()

    iframe = driver.find_element_by_id('iframeResult')

    driver.switch_to.frame(iframe)

    time.sleep(random.uniform(2, 4))

    pasre_page(driver)
