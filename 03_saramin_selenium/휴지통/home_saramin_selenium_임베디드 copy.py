import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36")
options=options
url="https://www.saramin.co.kr/"

browser = webdriver.Chrome(r"C:\Users\Son\Desktop\IT공부\web-1\web1\05_web_scraping\03_saramin_selenium\chromedriver.exe") # "./chromedriver.exe"
browser.maximize_window()

browser.get(url)


time.sleep(0.1)
browser.find_element_by_xpath('//*[@id="search_open"]/span').click()
time.sleep(0.1)
browser.find_element_by_xpath('//*[@id="ipt_keyword_recruit"]').click()
time.sleep(0.1)
browser.find_element_by_xpath('//*[@id="ipt_keyword_recruit"]').send_keys("IT")
time.sleep(0.1)
browser.find_element_by_xpath('//*[@id="search_form_recruit"]/div/div[2]/label').click() #지역클릭 
time.sleep(0.1)
try:
  elem_busan = WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="panel_area"]/div[2]/div[1]/div[2]/div/ul[1]/li[4]/button')))
except:
  pass
browser.find_element_by_xpath('//*[@id="panel_area"]/div[2]/div[1]/div[2]/div/ul[1]/li[4]/button').click()#부산클릭

time.sleep(0.1)
browser.find_element_by_xpath('//*[@id="panel_area"]/div[2]/div[2]/div[2]/div/div/button[2]').click() #지역초기화 클릭
time.sleep(0.1)
browser.find_element_by_xpath('//*[@id="panel_area"]/div[2]/div[2]/div[2]/div/ul/li[1]/label').click() #부산 전지역 클릭
time.sleep(0.1)
browser.find_element_by_xpath('//*[@id="search_form_recruit"]/div/div[3]/label').click() #직업 클릭
time.sleep(0.1)
try:
  elem_develop = WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="panel_area"]/div[2]/div[1]/div[2]/div/ul[1]/li[4]/button')))
except:
  pass
browser.find_element_by_xpath('//*[@id="panel_category"]/div[2]/div[1]/button[6]').click() #IT 개발 데이터 클릭

time.sleep(0.1)
browser.find_element_by_xpath('//*[@id="panel_category"]/div[1]/div[2]/button').click() #선택 초기화 클릭
time.sleep(0.1)
browser.find_element_by_xpath('//*[@id="panel_category"]/div[2]/div[2]/div[2]/div[1]/label').click() #개발 데이터 전체 선택 클릭
time.sleep(0.1)
browser.find_element_by_xpath('//*[@id="btn_search_recruit"]').click() #검색 클릭
time.sleep(0.1)

browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[1]/div[1]/button').click() #경력 선택
time.sleep(0.1)
new=browser.find_element_by_xpath('//*[@id="zero_experience"]') #신입
if new.is_selected() == False:
  browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[1]/div[1]/div/div[1]/div[1]/label').click()
else:
    pass
time.sleep(0.1)
new1=browser.find_element_by_xpath('//*[@id="no_experience"]') #경력무관
if new1.is_selected() == False:
    browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[1]/div[1]/div/div[1]/div[3]/label').click()
else:
    pass
time.sleep(0.1)
browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[1]/div[1]/div/div[3]/button[2]').click()#닫기

browser.find_element_by_xpath('//*[@id="recruit_info"]/div[2]/div/div[3]/button').click() #업체 보이는 개수 버튼
time.sleep(0.1)
browser.find_element_by_xpath('//*[@id="recruit_info"]/div[2]/div/div[3]/div/ul/li[7]/button').click() #업체 보이는 개수100개 설정

time.sleep(0.1)

browser.find_element_by_xpath('//*[@id="recruit_info_list"]/div[2]/div/a').click() #채용정보 더보기 클릭




curr_handle = browser.current_window_handle
print(curr_handle) # 현재 윈도우 핸들 정보

wb = Workbook(write_only=True) 
ws = wb.create_sheet('임베디드')
ws.append(['순번','브라우저 타이틀', '지원자 수', '모집 타이틀','모집 분야'])



  
sel_info_lists=''
sel_info_lists = browser.find_elements_by_css_selector('#recruit_info_list > div.content > div')
print("sel_info_lists len:", len(sel_info_lists))

soup_info_lists =''
soup = BeautifulSoup(browser.page_source, "lxml")
soup_info_lists = soup.find_all("div", attrs={"class":"item_recruit"})
print("soup_info_lists len:", len(soup_info_lists))

i=0
for sel_info,soup_info in zip(sel_info_lists,soup_info_lists):
  sel_info.find_element_by_partial_link_text('').click()
  i+=1;
  job_condition_text=soup_info.find("div", attrs={"class":"job_condition"}).get_text()
  job_tit=soup_info.find("a", attrs={"class":"data_layer"})
  time.sleep(0.1)
  handles = browser.window_handles # 모든 핸들 정보
  print(i)
  print(job_tit.get_text())
  print(job_condition_text)
  
  browser.switch_to.window(handles[1]) # 각 핸들로 이동해서
  soup = BeautifulSoup(browser.page_source, "lxml")
  people=''
  try:
    people =soup.find("dl", attrs={"class":"total"}).dd.get_text()
  except:
    pass
  print("지원자수 : ",people)
  time.sleep(0.1)
  print(browser.title) # 출력해보면 현재 핸들 (브라우저) 의 제목 표시
  row=[i,browser.title]
  browser.close()
  time.sleep(0.1)
  browser.switch_to.window(curr_handle)
  print('-'*30)
  row.extend([people, job_tit.get_text(), job_condition_text])
  ws.append(row)

    


time.sleep(1)
#browser.quit()
wb.save('임베디드.xlsx')
'''
browser_pages=browser.find_elements_by_xpath('//*[@id="recruit_info_list"]/div[2]/div/a')

print("browser_pages2 len:",len(browser_pages))


for browser_page in browser_pages:
  print("browser_page:", browser_page.text)
  try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="recruit_info_list"]/div[2]/div/a')))
    # 성공했을 때 동작 수행    
    print(elem.text) # 첫번째 결과 출력
  finally:
    browser.quit()
  browser_page.click()
'''