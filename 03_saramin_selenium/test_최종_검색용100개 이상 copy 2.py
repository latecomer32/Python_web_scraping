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

browser = webdriver.Chrome(r"C:\Users\Son\Desktop\IT공부\web-1\web1\05_web_scraping\03_saramin_selenium\chromedriver.exe") # "./chromedriver.exe"

url = "https://www.saramin.co.kr/zf_user/jobs/relay/view?isMypage=no&rec_idx=41316799&recommend_ids=eJxNz8ERAzEIA8Bq8pdAGHinkOu%2Fizi5ibnnjjAWormb%2FCrrV75Fa1rlVeSPVCRqWEDHDFfIsXmnngHPoYLCGaYTxr0q77fJKvsT3RGKkxKSr0P3KmLSzm47rdBC4tBSu8dwrd3z8a%2FZmlW%2BQB%2FCre1xb6ipLz8UtD%2B9&view_type=search&searchword=%EC%9E%84%EB%B2%A0%EB%94%94%EB%93%9C&searchType=search&gz=1&t_ref_content=generic&t_ref=search&paid_fl=n#seq=0"

browser.get(url)
res = requests.get(url)
browser.maximize_window()


interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
for k in range(0,1):
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")






assing_title =  browser.find_element_by_xpath('//*[@class="info"]/dl[2]/dd')

print("(assing_title:",assing_title.text)


assing_title2 =  browser.find_element_by_xpath('//*[@class="info"]/dl[3]/dd')

print("(assing_title2:",assing_title2.text)

assing_title3 =  browser.find_element_by_xpath('//*[@class="info"]/dl[4]/dd')

print("(assing_title3:",assing_title3.text)

assing_title4 =  browser.find_element_by_xpath('//*[@class="info"]/dl[5]/dd')

print("(assing_title4:",assing_title4.text)

assing_title5 =  browser.find_element_by_xpath('//*[@class="info"]/dl[6]/dd')

print("(assing_title5:",assing_title5.text)
'''
time.sleep(4)
soup = BeautifulSoup(res.text, "lxml")
time.sleep(4)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(browser.page_source)


/html/body/div[3]/div/div/div[2]/div[1]/div[1]/div[5]/div[1]

#content > div.wrap_jview > div.jview.jview-0-41316799 > div.wrap_jv_cont > div.jv_cont.jv_company > div.jv_title
print("(assing_title:",assing_title.text)


print("assing_task:",assing_task.text)

print("apply_period:",apply_period.text)

네오텍 매출, 사원수 설립일

//*[@id="content"]/div[2]/div[1]/div[1]/div[9]/div[2]/div[2]/div[2]/dl[5]/dt
//*[@id="content"]/div[2]/div[1]/div[1]/div[9]/div[2]/div[2]/div[2]/dl[5]/dd/text()

//*[@id="content"]/div[2]/div[1]/div[1]/div[9]/div[2]/div[2]/div[2]/dl[2]/dt
//*[@id="content"]/div[2]/div[1]/div[1]/div[9]/div[2]/div[2]/div[2]/dl[2]/dd

//*[@id="content"]/div[2]/div[1]/div[1]/div[9]/div[2]/div[2]/div[2]/dl[4]/dt
//*[@id="content"]/div[2]/div[1]/div[1]/div[9]/div[2]/div[2]/div[2]/dl[4]/dd

오스템임플란트
//*[@class="info"]/dl[2]/dt

div class="info"



    //*[@id="template_divisions_assign_task_nm_0"]/tbody/tr[1]/td/strong
    //*[@id="template_divisions_qualification_title_0"]
젠투
담당 타이틀  : /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/div/strong  #tr ,class=recruit_division_0 tr_division
    담당업무:  /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[1]/tbody/tr[1]/td/strong
    1:        /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[1]/tbody/tr[2]/td

    지원자격 : /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[2]/tbody/tr[1]/td/strong
    1:        /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[2]/tbody/tr[2]/td/span

    우대사항 : /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[3]/tbody/tr[1]/td/strong
    1:        /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[3]/tbody/tr[2]/td/table/tbody/tr[1]/td
    2:        /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[3]/tbody/tr[2]/td/table/tbody/tr[2]/td
    접수기간 : /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[4]/td/div/table/tbody/tr[1]/td/span[4]

더블유시스템
담당 타이틀  : /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/div/strong
    담당업무 : /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[1]/tbody/tr[1]/td/strong
           1: /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[1]/tbody/tr[2]/td
           2:
           3:
    지원자격 : /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[2]/tbody/tr[1]/td/strong
           1: /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[2]/tbody/tr[2]/td/span[1]
           2:
           3:
    우대사항 :
           1: 
           2:
           3:
    접수기간 : /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[4]/td/div/table/tbody/tr[1]/td/span[4]

데이터에듀
담당 타이틀  : /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/div/strong
    담당업무 : /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[1]/tbody/tr[1]/td/strong
            1: /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[1]/tbody/tr[2]/td
            2:
            3:
    지원자격 : /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[2]/tbody/tr[1]/td/strong
            1: /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[2]/tbody/tr[2]/td/span[1]
            2:
            3:
    우대사항 :
            1: 
            2:
            3:


파나시아
담당 타이틀  : /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/div/strong
    담당업무 : /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[1]/tbody/tr[1]/td/strong/span[2]
            1: /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[1]/tbody/tr[1]/td/strong/span[3]
            2: /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[1]/tbody/tr[1]/td/strong/span[3]/span
            3:
    지원자격 : /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[1]/tbody/tr[1]/td/strong/span[4]
            1: /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[1]/tbody/tr[1]/td/strong/span[5]/span
            2:
            3:
    우대사항 : /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[1]/tbody/tr[1]/td/strong/span[6]/strong
            1: /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[1]/tbody/tr[1]/td/strong/span[7]
            2: /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[1]/tbody/tr[1]/td/strong/span[8]
            3:
    2담당업무 : /html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[1]/tbody/tr[1]/td/strong/span[10]/strong/span


에스피메드
/html/body/div/div/img



#with open("mygoogle.html", "w", encoding="utf8") as f:
#    f.write(res.text)
'''