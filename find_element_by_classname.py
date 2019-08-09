# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


##############
# ドライバーの準備
#
# driverを初期化
##############
op = Options()
# --headlessだけではOSによって動かない、プロキシが弾かれる、
# CUI用の省略されたHTMLが帰ってくるなどの障害が出ます。
# 長いですが、これら6行あって最強かつどんな環境でも動きますので、必ず抜かさないようにしてください。
# @see https://qiita.com/ryuta69/items/c84501993635c72540a7
op.add_argument("--disable-gpu")
op.add_argument("--disable-extensions")
op.add_argument("--proxy-server='direct://'")
op.add_argument("--proxy-bypass-list=*")
op.add_argument("--start-maximized")
op.add_argument("--headless")


# ドライバー定義（ブラウザ起動）
# chromedriverとchromeのバージョンを合わせないとエラーになるぞい
driver = webdriver.Chrome('C:\\Users\\jumpi\\Documents\\ChromeDriver\\chromedriver76.exe')

# 現在のwindowハンドルを取得
current_handle = driver.current_window_handle

# 指定したURLに遷移する
driver.get("https://www.google.co.jp")

try:
    # 存在しないClass名から取得
    element = driver.find_element_by_class_name("unko_tarou")
    from pprint import pprint
    pprint(element)

except NoSuchElementException:
    print("例外出たので中止ッス")


driver.quit()
