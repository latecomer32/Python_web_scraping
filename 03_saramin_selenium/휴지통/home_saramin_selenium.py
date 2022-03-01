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



time.sleep(0.5)
browser.find_element_by_xpath('//*[@id="search_open"]/span').click()
time.sleep(0.5)
browser.find_element_by_xpath('//*[@id="ipt_keyword_recruit"]').click()
time.sleep(0.5)
browser.find_element_by_xpath('//*[@id="ipt_keyword_recruit"]').send_keys("IT")
time.sleep(0.5)
browser.find_element_by_xpath('//*[@id="search_form_recruit"]/div/div[2]/label').click() #지역클릭 
time.sleep(0.5)
browser.find_element_by_xpath('//*[@id="panel_area"]/div[2]/div[1]/div[2]/div/ul[1]/li[4]/button').click() #부산클릭
time.sleep(0.5)
browser.find_element_by_xpath('//*[@id="panel_area"]/div[2]/div[2]/div[2]/div/div/button[2]').click() #지역초기화 클릭
time.sleep(0.5)
browser.find_element_by_xpath('//*[@id="panel_area"]/div[2]/div[2]/div[2]/div/ul/li[1]/label').click() #부산 전지역 클릭
time.sleep(0.5)
browser.find_element_by_xpath('//*[@id="search_form_recruit"]/div/div[3]/label').click() #직업 클릭
time.sleep(0.5)
browser.find_element_by_xpath('//*[@id="panel_category"]/div[2]/div[1]/button[6]').click() #IT 개발 데이터 클릭
time.sleep(0.5)
browser.find_element_by_xpath('//*[@id="panel_category"]/div[1]/div[2]/button').click() #선택 초기화 클릭
time.sleep(0.5)
browser.find_element_by_xpath('//*[@id="panel_category"]/div[2]/div[2]/div[2]/div[1]/label').click() #개발 데이터 전체 선택 클릭
time.sleep(0.5)
browser.find_element_by_xpath('//*[@id="btn_search_recruit"]').click() #검색 클릭
time.sleep(0.5)
browser.find_element_by_xpath('//*[@id="recruit_info_list"]/div[2]/div/a').click()


sel_info_lists = browser.find_elements_by_css_selector('#recruit_info_list > div.content > div')

for sel_info in sel_info_lists:
    sel_info.find_element_by_partial_link_text('').click()

'''

soup = BeautifulSoup(browser.page_source, "html")

#info_lists = soup.find_all("div", attrs={"class":"item_recruit"})

print(len(info_lists))






for info in info_lists:
  

    





info_lists=browser.find_elements_by_css_selector('#recruit_info_list > div.content > div')

for info in info_lists:
  info_text=info.find("div", attrs={"class":"job_condition"}).get_text()
  print(info_text.text)

print(len(info_lists))
info.click()

//*[@id="recruit_info_list"]/div[1]/div[13]/div[1]/div[3]
#recruit_info_list > div.content > div.item_recruit > div.area_job > div.job_condition

#recruit_info_list > div.content > div.item_recruit.visited.has_similar_list > div.area_job > div.job_condition

curr_handle = browser.current_window_handle
time.sleep(0.5)
browser.find_element_by_xpath('//*[@id="recruit_info_list"]/div[1]/div[1]/div[1]/h2/a').click() #부산 전지역 클릭
//*[@id="recruit_info_list"]/div[1]/div[1]/div[1]/div[3]/span[2]

time.sleep(0.5)
browser.find_element_by_xpath('//*[@id="panel_area"]/div[2]/div[2]/div[2]/div/div/button[2]').click() #부산 전지역 클릭
time.sleep(0.5)
browser.find_element_by_xpath('//*[@id="panel_area"]/div[2]/div[2]/div[2]/div/div/button[2]').click() #부산 전지역 클릭
time.sleep(0.5)
browser.find_element_by_xpath('//*[@id="panel_area"]/div[2]/div[2]/div[2]/div/div/button[2]').click() #부산 전지역 클릭
time.sleep(0.5)
browser.find_element_by_xpath('//*[@id="panel_area"]/div[2]/div[2]/div[2]/div/div/button[2]').click() #부산 전지역 클릭
time.sleep(0.5)
browser.find_element_by_xpath('//*[@id="panel_area"]/div[2]/div[2]/div[2]/div/div/button[2]').click() #부산 전지역 클릭
'''
