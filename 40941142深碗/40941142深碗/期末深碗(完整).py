from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#定義a為城市及代碼
a=" 1 基隆市  2 臺北市  3 新北市  4 桃園市  5 新竹市\n 6 新竹縣  7 苗栗縣  8 臺中市  9 彰化縣 10 南投縣\n11 雲林縣 12 嘉義市 13 嘉義縣 14 臺南市 15 高雄市\n16 屏東縣 17 宜蘭縣 18 花蓮縣 19 臺東縣 20 澎湖縣\n21 金門縣 22 連江縣"
#定義b為城市網址代碼
b=['0','10017','63','65','68','10018','10004','10005','66','10007','10008','10009','10020','10010','67','64','10013','10002','10015','10014','10016','09020','09007']
while True:
    print("\n     ★☆★☆★代碼對應的城市如下★☆★☆★")
    print("------------------------------------------------")
    print(a)
    c=eval(input("請輸入縣市代碼："))
    #輸入錯誤的代碼
    if c<1 or c>22:print("\n-----ERROR------請輸入正確的代碼------ERROR-----")
    else:break
#自動化搜尋中央氣象局網站的城市天氣資料
google_path = Options()
google_path.add_argument("--disable-notifications")        
driver = webdriver.Chrome('./chromedriver', chrome_options=google_path)
#進入網站
driver.get("https://www.cwb.gov.tw/V8/C/W/County/County.html?CID=%s"%b[c])
while 1:
    #抓取網站資訊，今日白天溫度
    z1=driver.find_element_by_xpath("/html/body/div[2]/main/div/div[2]/div[3]/div/div[1]/div[1]/table/tbody/tr[1]/td[1]/p/span[1]")
    #抓取網站資訊，今日晚上溫度
    z2=driver.find_element_by_xpath("/html/body/div[2]/main/div/div[2]/div[3]/div/div[1]/div[1]/table/tbody/tr[2]/td[1]/p/span[1]")
    #抓取網站資訊，今日體感溫度
    z4=driver.find_element_by_xpath("/html/body/div[2]/main/div/div[2]/div[3]/div/div[1]/div[1]/table/tbody/tr[3]/td[1]/span[1]")
    #抓取網站資訊，明日白天溫度
    z5=driver.find_element_by_xpath("/html/body/div[2]/main/div/div[2]/div[3]/div/div[1]/div[1]/table/tbody/tr[1]/td[2]/p/span[1]")
    #抓取網站資訊，明日晚上溫度
    z6=driver.find_element_by_xpath("/html/body/div[2]/main/div/div[2]/div[3]/div/div[1]/div[1]/table/tbody/tr[2]/td[2]/p/span[1]")
    #抓取網站資訊，明日體感溫度
    z8=driver.find_element_by_xpath("/html/body/div[2]/main/div/div[2]/div[3]/div/div[1]/div[1]/table/tbody/tr[3]/td[2]/span[1]")
    #抓取網站資訊，降雨機率
    ss =driver.page_source.split('<i title="降雨機率" class="icon-umbrella" aria-hidden="true"></i>')[1:3]
    z3="";z7=""
    for i in range(2):
        for j in ss[i]:
            if j != '<':
                if i==0:z3 += j
                elif i == 1:z7+=j
            else:break
    if z1 != "" and  z2 != "" and  z3 != "" and z4 != "" and z5 != "" and z6 != "" and z7 != "" and z8 != "":break
print("今日白天溫度：%s℃"%(z1.text))
print("今日晚上溫度：%s℃"%(z2.text))
print("今日降雨機率：%s"%(z3))
print("今日體感溫度：%s℃"%(z4.text))
print("----------------------")
print("明日白天溫度：%s℃"%(z5.text))
print("明日晚上溫度：%s℃"%(z6.text))
print("明日降雨機率：%s"%(z7))
print("明日體感溫度：%s℃"%(z8.text))
driver.quit()