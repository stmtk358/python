#! python3
# 機能
#  Google検索結果を別タブで開く
# 使い方
#  1.Pythonを実行する
# 実行コマンド
#  python google_search_tab.py 検索ワード
#  python google_search_tab.py Python
#  python google_search_tab.py Python 入門

import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import logging

# webdriver_managerのログを抑止する
logging.disable(logging.INFO)

# 検索する
def search(driver, keywords, search_count):
    results = []

    # 検索数まで検索結果を取得する
    while len(results) <= search_count:
        if len(results) == 0:
            # キーワードで検索する
            driver.get("http://google.com/search?q=" + " ".join(keywords))
        else:
            # 次ページがあれば遷移する
            elements = driver.find_elements_by_css_selector("#pnnext")
            if len(elements) == 0:
                break
            elements[0].click()
        time.sleep(3)

        # 検索結果のリンクを取得する
        elements = driver.find_elements_by_css_selector(".g .yuRUbf > a")
        if len(elements) == 0:
            break

        # URLとタイトルを取得する
        for element in elements:
            url = element.get_attribute("href")
            title = element.find_elements_by_css_selector("h3")[0].text
            results.append({"url": url, "title": title})

    return results[:search_count]


# 検索結果を別タブで開く
def search_tab(keywords, search_count):
    # 実行後にブラウザを閉じないようにする
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # 検索する
    results = search(driver, keywords, search_count)

    # 別タブで開く
    for result in results:
        driver.execute_script("window.open(arguments[0], '_blank')", result["url"])


if len(sys.argv) < 2:
    sys.exit("使い方：python google_search_tab.py 検索ワード")

# 検索する（最大20件）
search_tab(sys.argv[1:], 20)
