import time
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

def selenium():
    options = Options()

    # ヘッドレスモードで実行する場合は以下
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.google.co.jp/")
        # 簡易的にJSが評価されるまで待つ
        time.sleep(5)

        # aタグを抽出
        elem_list = driver.find_elements_by_tag_name("a")
        for elem in elem_list:
            # attributeの中からhrefを抽出して出力
            url = elem.get_attribute("href")
            print(url)

    except:
        traceback.print_exc()

    finally:
        # エラーが起きても起きなくてもブラウザを閉じる
        driver.quit()

#############################
#           MAIN            #
#############################
selenium()


