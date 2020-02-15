import urllib.request, urllib.error
from bs4 import BeautifulSoup

def scraping():

    # アクセスするURLを設定
    url = input("アクセスしたいurlを入力してください:")

    # URLにアクセスする
    html = urllib.request.urlopen(url)

    # htmlをBeautifulSoupでがちゃがちゃする
    soup = BeautifulSoup(html, "html.parser")

    # タイトル要素を取得
    title_tag = soup.title

    # 要素の文字列を取得
    title = title_tag.string

    # タイトル要素を出力
    print(title_tag)
    print(title)

#############################
#           MAIN            #
#############################
scraping()
