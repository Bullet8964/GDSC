	# 先導入後面會用到的套件
import requests
from bs4 import BeautifulSoup
import time
import os


# 要爬的股票
stock = ["1101", "2330", "1102"]


# 從 GitHub Secrets 取得 Telegram Bot Token
token = os.environ.get("TELEGRAM_BOT_TOKEN")

# 從 GitHub Secrets 取得 Telegram Chat ID
chat_id = os.environ.get("TELEGRAM_CHAT_ID")


if not token:
    raise RuntimeError("找不到 TELEGRAM_BOT_TOKEN")

if not chat_id:
    raise RuntimeError("找不到 TELEGRAM_CHAT_ID")


# Yahoo Finance Headers
headers = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/131.0 Safari/537.36"
    )
}


for stockid in stock:

    print(f"正在取得 {stockid} 股價...")

    # Yahoo Finance 網址
    url = f"https://tw.stock.yahoo.com/quote/{stockid}.TW"

    try:
        # 發送請求
        r = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        r.raise_for_status()

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
            print(f"{stockid}：找不到股價")
            continue

        price = price_element.get_text(strip=True)

        print(f"{stockid}：{price}")

        # Telegram 訊息
        message = f"股票 {stockid} 即時股價為 {price}"

        # Telegram API
        telegram_url = (
            f"https://api.telegram.org/"
            f"bot{token}/sendMessage"
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

        print(f"{stockid}：Telegram 通知成功")

    except Exception as e:

        print(
            f"{stockid}：發生錯誤：{e}"
        )

    # 每支股票等待 3 秒
    time.sleep(3)
