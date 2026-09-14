import requests
from bs4 import BeautifulSoup
import time
import os


# 股票代號
stock = ["1101", "2330", "1102"]


# Telegram 設定
token = os.environ["TELEGRAM_BOT_TOKEN"]
chat_id = os.environ["TELEGRAM_CHAT_ID"]


headers = {
    "User-Agent": "Mozilla/5.0"
}


for stockid in stock:

    print(f"正在取得 {stockid} 股價...")

    # Yahoo Finance
    url = f"https://tw.stock.yahoo.com/quote/{stockid}.TW"

    try:

        # 取得網頁
        r = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        # 解析 HTML
        soup = BeautifulSoup(
            r.text,
            "html.parser"
        )

        # 找股價
        price_element = soup.find(
            "span",
            class_=[
                "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)",
                "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)",
                "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)"
            ]
        )

        if price_element is None:
            print(f"{stockid} 找不到股價")
            continue

        price = price_element.get_text(strip=True)

        # Telegram 訊息
        message = f"股票 {stockid} 即時股價為 {price}"

        # Telegram API
        telegram_url = (
            f"https://api.telegram.org/bot{token}/sendMessage"
        )

        response = requests.get(
            telegram_url,
            params={
                "chat_id": chat_id,
                "text": message
            },
            timeout=10
        )

        response.raise_for_status()

        print(f"{stockid} Telegram 傳送成功")

    except Exception as e:

        print(f"{stockid} 發生錯誤：{e}")

    # 下一支股票等待 3 秒
    time.sleep(3)
