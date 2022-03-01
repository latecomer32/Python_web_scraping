import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

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
browser.find_element_by_xpath('//*[@id="panel_area"]/div[2]/div[1]/div[2]/div/ul[1]/li[4]/button').click() #부산클릭
time.sleep(0.1)
browser.find_element_by_xpath('//*[@id="panel_area"]/div[2]/div[2]/div[2]/div/div/button[2]').click() #지역초기화 클릭
time.sleep(0.1)
browser.find_element_by_xpath('//*[@id="panel_area"]/div[2]/div[2]/div[2]/div/ul/li[1]/label').click() #부산 전지역 클릭
time.sleep(0.1)
browser.find_element_by_xpath('//*[@id="search_form_recruit"]/div/div[3]/label').click() #직업 클릭
time.sleep(0.1)
browser.find_element_by_xpath('//*[@id="panel_category"]/div[2]/div[1]/button[6]').click() #IT 개발 데이터 클릭
time.sleep(0.1)
browser.find_element_by_xpath('//*[@id="panel_category"]/div[1]/div[2]/button').click() #선택 초기화 클릭
time.sleep(0.1)
browser.find_element_by_xpath('//*[@id="panel_category"]/div[2]/div[2]/div[2]/div[1]/label').click() #개발 데이터 전체 선택 클릭
time.sleep(0.1)
browser.find_element_by_xpath('//*[@id="btn_search_recruit"]').click() #검색 클릭
time.sleep(0.1)
browser.find_element_by_xpath('//*[@id="recruit_info_list"]/div[2]/div/a').click()

curr_handle = browser.current_window_handle
print(curr_handle) # 현재 윈도우 핸들 정보

def handle_control():
  sel_info.find_element_by_partial_link_text('').click()
  time.sleep(0.1)
  handles = browser.window_handles # 모든 핸들 정보
  print(i)
  print(job_tit.get_text())
  print(job_condition_text)
  browser.switch_to.window(handles[1]) # 각 핸들로 이동해서
  time.sleep(0.1)
  print(browser.title) # 출력해보면 현재 핸들 (브라우저) 의 제목 표시
  #browser.close()
  time.sleep(0.1)
  browser.switch_to.window(curr_handle)
  print('-'*30)
  time.sleep(0.1)

sel_info_lists = browser.find_elements_by_css_selector('#recruit_info_list > div.content > div')

soup = BeautifulSoup(browser.page_source, "html")
soup_info_lists = soup.find_all("div", attrs={"class":"item_recruit"})



i=0
word1='신입'
word2='경력무관'
for sel_info,soup_info in zip(sel_info_lists,soup_info_lists):
  i+=1;
  job_condition_text=soup_info.find("div", attrs={"class":"job_condition"}).get_text()
  job_tit=soup_info.find("a", attrs={"class":"data_layer"})
  if word1 in job_condition_text:
    handle_control()
  elif word2 in job_condition_text:
    handle_control()
  elif word1 in job_tit.get_text():
    handle_control()
  elif word2 in job_tit.get_text():
    handle_control()


'''


browser.find_element_by_xpath('//*[@id="panel_area"]/div[2]/div[2]/div[2]/div/div/button[2]').click() #부산 전지역 클릭
time.sleep(0.1)
browser.find_element_by_xpath('//*[@id="panel_area"]/div[2]/div[2]/div[2]/div/div/button[2]').click() #부산 전지역 클릭
time.sleep(0.1)
browser.find_element_by_xpath('//*[@id="panel_area"]/div[2]/div[2]/div[2]/div/div/button[2]').click() #부산 전지역 클릭
time.sleep(0.1)
browser.find_element_by_xpath('//*[@id="panel_area"]/div[2]/div[2]/div[2]/div/div/button[2]').click() #부산 전지역 클릭
time.sleep(0.1)
browser.find_element_by_xpath('//*[@id="panel_area"]/div[2]/div[2]/div[2]/div/div/button[2]').click() #부산 전지역 클릭
'''
