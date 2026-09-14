Skip to content
Bullet8964
GDSC
Repository navigation
Code
Issues
Pull requests
Agents
Actions
Projects
Wiki
Security and quality
1
 (1)
Insights
Settings
Files
Go to file
t
T
.github/workflows
python-app.yml
README.md
test1.py
GDSC
/
test1.py
in
main

Edit

Preview
Indent mode

Tabs
Indent size

4
Line wrap mode

No wrap
Editing test1.py file contents
  1
  2
  3
  4
  5
  6
  7
  8
  9
 10
 11
 12
 13
 14
 15
 16
 17
 18
 19
 20
 21
 22
 23
 24
 25
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
	# 先導入後面會用到的套件
import requests # 請求工具
from bs4 import BeautifulSoup # 解析工具
import time # 用來暫停程式
 
# 要爬的股票
stock = ["1101","2330"]
	for i in range(len(stock)): # 迴圈依序爬股價

	    # 現在處理的股票

	    stockid = stock[i]

	    # 網址塞入股票編號

	    url = "https://tw.stock.yahoo.com/quote/"+stockid+".TW"

	    # 發送請求

	    r = requests.get(url)

	    # 解析回應的 HTML

	    soup = BeautifulSoup(r.text, 'html.parser')

	    # 定位股價

	    price = soup.find('span',class_=["Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)","Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)","Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)"]).getText()
     	    # 回報的訊息 (可自訂)

	    message = "股票 "+stockid+" 即時股價為 "+price

	    # 用 telegram bot 回報股價

	    # bot token

Use Control + Shift + m to toggle the tab key moving focus. Alternatively, use esc then tab to move to the next interactive element on the page.
Editing GDSC/test1.py at main · Bullet8964/GDSC
