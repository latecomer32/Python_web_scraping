import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36")
options=options


browser = webdriver.Chrome(r"C:\Users\Son\Desktop\IT공부\web-1\web1\05_web_scraping\03_saramin_selenium\chromedriver.exe") # "./chromedriver.exe"

wb = Workbook(write_only=True) 
k=0

url = "https://www.saramin.co.kr/zf_user/jobs/relay/view?isMypage=no&rec_idx=41364469&recommend_ids=eJxFj8sRw1AIA6vJHfHXOYW4%2Fy7Ci8f4uLMIgcNSW%2Fxqxae%2BLmSEx9WQg2NRZWN5o%2FWYtTCI4kHp9tZ8h5FF7uaxNFkLDZzNyBtzumYY%2F2GImbosKufI3CJGuedmTcmSB4WdztosbGS8RSU4%2Fz5onqX7kTAZ%2FWSH0HGukh8qvT%2F1&view_type=search&searchword=java&searchType=search&gz=1&t_ref_content=generic&t_ref=search&paid_fl=n#seq=0"
browser.maximize_window()
browser.get(url)
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

wrap_tbl_template= soup.find_all("body") #, attrs={"class":"tit"}
test=browser.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div[1]/div[1]/div/h1')

print("test:",test)


#print("wrap_tbl_template:",wrap_tbl_template)


with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(soup)







#/html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div
#/html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[1]/tbody/tr[2]/td
# link = cartoons[0].a["href"]
# print("https://comic.naver.com" + link)

# 만화 제목 + 링크 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

# 평점 구하기
#total_rates = 0
#cartoons = soup.find_all("div", attrs={"class":"rating_type"})
#for cartoon in cartoons:
#    rate = cartoon.find("strong").get_text()

#dd=browser.find_element_by_xpath('//*[@id="template_divisions_assign_task_nm_0"]/tbody').text()



