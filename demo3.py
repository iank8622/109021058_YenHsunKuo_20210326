import requests
from bs4 import BeautifulSoup
# 執行請用命令窗輸入 python3 demo.py 方式執行

# 先判斷網頁是否存在 存在顯示200 錯誤顯示404
req = requests.get(
    "http://isrc.ccs.asia.edu.tw/www/myjournal/myjournal.htm")

# 為服務全球受眾 轉為utf8編碼
req.encoding = "big5"

# req.status_code如為存在(200)
if req.status_code == 200:
    # 抓出其原始碼
    # print(req.text)

    ''' 
    1. 無法對req.text直接抓資料 將資料轉換成BeautifulSoup物件從湯中撈料
    2. "lxml"為解析器 在解析器（Parser）的部分可以使用lxml、html5lib等
       套件，或者是使用Python內建的html.parser來解析原始碼。
    3. 抓資料要找目標物(ul=沒有序列, li=list item, ol=oder list, class=專案)
    '''
    soup = BeautifulSoup(req.text, "lxml")
    # print(soup)

    # 找到程式碼中之內容(其實就是一般網頁中的文字搜尋功能) .find只找一個
    # find_all會找包在標籤中所有內容 可以輸入多個參數(同時從在才會載下)
    result1 = soup.find_all("span", lang='EN-US')


    # 將資料寫出 open("輸出檔名", "指令(寫出)", "輸出編碼")
    fp = open("out3.text", "w",encoding="utf8")

    

    #print(result1)

    # i當索引值
    # .text中自帶\n與"  " 用""與之替換
    i = 1
    for val in result1:

        # .replace("找到此參數", 替換為此參數)
        text2 = val.text.replace("\n", "")
        print(text2)

        # 將寫出資料自動換行才不會擠成一筆
        fp.write(text2 + "\n")
    #關掉才會寫    
    fp.close()

else:
    print("No page!")
