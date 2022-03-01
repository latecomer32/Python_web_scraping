import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

search_words=['임베디드']
wb = Workbook(write_only=True) 

k=0
for search_word in search_words:
    
    k+=1
    browser = webdriver.Chrome(r"C:\Users\Son\Desktop\IT공부\web-1\web1\05_web_scraping\03_saramin_selenium\chromedriver.exe") # "./chromedriver.exe"
    browser.maximize_window()
    url="https://www.saramin.co.kr/zf_user/"
    browser.get(url)
    
    ws = wb.create_sheet(str(k)+"_"+search_word,k)
    ws.append(['순번','브라우저 타이틀', '모집 타이틀','com_sales','employees','company_type','Enterprise_type','establishment_date','모집 분야', 'views_count' ,'지원자 수', 'Career', 'work_type', 'locate', 'assign_title', 'assign_task', 'assign_task_1', 'assign_task_2',  'qualification', 'qualification_1', 'qualification_2', 'divisions_pre', 'divisions_pre_1', 'divisions_pre_2', 'divisions_pre_3', 'apply_period', 'company_name', 'Salary', 'work_hour', 'academic_background'])  #엑셀 1행

    time.sleep(0.1)
    browser.find_element_by_xpath('//*[@id="search_open"]/span').click()
    time.sleep(0.1)
    browser.find_element_by_xpath('//*[@id="ipt_keyword_recruit"]').click()
    time.sleep(0.1)
    browser.find_element_by_xpath('//*[@id="ipt_keyword_recruit"]').send_keys(search_word)
    time.sleep(0.1)
    browser.find_element_by_xpath('//*[@id="search_form_recruit"]/div/div[2]/label').click() #지역클릭 
    time.sleep(0.5)
    try:
        elem_busan = WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="panel_area"]/div[2]/div[1]/div[2]/div/ul[1]/li[4]/button')))
    except:
        pass
    time.sleep(0.5)
    browser.find_element_by_xpath('//*[@id="panel_area"]/div[2]/div[1]/div[2]/div/ul[1]/li[4]/button').click()#부산클릭

    time.sleep(0.1)
    browser.find_element_by_xpath('//*[@id="panel_area"]/div[2]/div[2]/div[2]/div/div/button[2]').click() #지역초기화 클릭
    time.sleep(0.1)
    browser.find_element_by_xpath('//*[@id="panel_area"]/div[2]/div[2]/div[2]/div/ul/li[1]/label').click() #부산 전지역 클릭
    time.sleep(0.1)
    browser.find_element_by_xpath('//*[@id="search_form_recruit"]/div/div[3]/label').click() #직업 클릭
    time.sleep(0.5)
    try:
        elem_develop = WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="panel_area"]/div[2]/div[1]/div[2]/div/ul[1]/li[4]/button')))
    except:
        pass
    time.sleep(0.7)
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

    browser.find_element_by_xpath('//*[@id="search_btn"]').click() #검색버튼 클릭



    browser.find_element_by_xpath('//*[@id="recruit_info"]/div[2]/div/div[3]/button').click() #업체 보이는 개수 버튼
    time.sleep(0.1)
    browser.find_element_by_xpath('//*[@id="recruit_info"]/div[2]/div/div[3]/div/ul/li[1]/button').click() #업체 보이는 개수100개 설정
    
    
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

    try:
        browser.find_element_by_xpath('//*[@id="recruit_info_list"]/div[2]/div/a').click() #채용정보 더보기 클릭
        more_pages=True
    except:
        more_pages=False
    if more_pages:
        pages=browser.find_elements_by_xpath('//*//*[@id="recruit_info_list"]/div[2]/div/a') #페이지 요소 리스트
    else:
        pages=[]
    print("more_pages:",more_pages)
    print("pages:",pages)
    print("len_pages:",len(pages))
    
    for j in range(1,len(pages)+2):
        try:
            page=browser.find_element_by_link_text(str(j)).click()   #1,2,3..번 페이지 클릭
        except:
            pass    
        time.sleep(0.5)
        browser.get(browser.current_url)                     #새 조건으로 변경된 브라우저 URL정보에 따른 변경
        curr_handle = browser.current_window_handle          # 현재 윈도우 핸들 정보

        sel_info_lists=''                                                                                #info_lists 초기화
        sel_info_lists = browser.find_elements_by_css_selector('#recruit_info_list > div.content > div') # 모든 모집 정보요소를 selenium방식으로 찾아서 리스트화
        print("sel_info_lists len:", len(sel_info_lists))


        soup_info_lists =''                                                                              #soup info_lists 초기화
        soup = BeautifulSoup(browser.page_source, "html")                                                #soup 생성
        soup_info_lists = soup.find_all("div", attrs={"class":"item_recruit"})                           #모든 모집 정보요소를 soup방식으로 찾아서 리스트화 생성
        print("soup_info_lists len:", len(soup_info_lists))

        i=0
        for sel_info,soup_info in zip(sel_info_lists,soup_info_lists):
            sel_info.find_element_by_partial_link_text('').click()                                   #info의 하위 하이퍼링크 클릭
            i+=1;
            job_condition_text=soup_info.find("div", attrs={"class":"job_condition"}).get_text()
            job_tit=soup_info.find("a", attrs={"class":"data_layer"})
            time.sleep(0.1)
            handles = browser.window_handles # 모든 핸들 정보
            print(i)
            print(job_tit.get_text())
            print(job_condition_text)
            
            browser.switch_to.window(handles[1]) # 각 핸들로 이동해서
            soup = BeautifulSoup(browser.page_source, "html")
            Volunteer=''
            try:
                Volunteer =soup.find("dl", attrs={"class":"total"}).dd.get_text()
            except:
                pass
            print("지원자수 : ",Volunteer)
            time.sleep(0.1)
            print(browser.title) # 출력해보면 현재 핸들 (브라우저) 의 제목 표시
            try:
                company_name = browser.find_element_by_css_selector('#content > div.wrap_jview > div > div.wrap_jv_cont > div.wrap_jv_header > div > a').text  
            except:
                company_name="없음"
            try:  
                Career = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/dl[1]/dd/strong').text
            except:
                Career ="없음"

            try:  
                views_count = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/ul/li[1]/strong').text
            except:
                views_count ="없음"

            try:
                Salary = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/dl[1]/dd').text
            except:
                Salary ="없음"

            try:
                work_hour = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/dl[2]/dd').text
            except:
                work_hour ="없음"

            try:
                academic_background = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/dl[2]/dd/strong').text
            except:
                academic_background ="없음"

            try:
                work_type = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/dl[3]/dd/strong').text
            except:
                work_type ="없음"

            try:
                locate = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/dl[3]/dd').text
            except:
                locate="없음"


            browser.switch_to.frame('iframe_content_0') # ID값으로 frame 전환

            try:
                assign_title =  browser.find_element_by_xpath('/html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/div/strong').text
            except:
                assign_title="없음"

            try:
                assign_task = browser.find_element_by_xpath('/html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[1]/tbody/tr[1]/td/strong').text
            except:
                assign_task ="없음"
            try:
                assign_task_1 = browser.find_element_by_xpath('/html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[1]/tbody/tr[2]/td').text
            except:
                assign_task_1 ="없음"

            try:
                assign_task_2 = browser.find_element_by_xpath('/html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[1]/tbody/tr[3]/td').text

            except:
                assign_task_2 ="없음"

            try:
                qualification = browser.find_element_by_xpath('/html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[2]/tbody/tr[1]/td/strong').text

            except:
                qualification ="없음"
            try:
                qualification_1 = browser.find_element_by_xpath('/html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[2]/tbody/tr[2]/td/span').text

            except:
                qualification_1 ="없음"
            try:
                qualification_2 = browser.find_element_by_xpath('/html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[2]/tbody/tr[3]/td/span').text

            except:
                qualification_2 ="없음"

            try:
                divisions_pre = browser.find_element_by_xpath('/html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[3]/tbody/tr[1]/td/strong').text

            except:
                divisions_pre = "없음"
            try:
                divisions_pre_1 = browser.find_element_by_xpath('/html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[3]/tbody/tr[2]/td/table/tbody/tr[1]/td').text

            except:
                divisions_pre_1 = "없음"
            try:
                divisions_pre_2 = browser.find_element_by_xpath('/html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[3]/tbody/tr[2]/td/table/tbody/tr[2]/td').text

            except:
                divisions_pre_2 = "없음"
            try:
                divisions_pre_3 = browser.find_element_by_xpath('/html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/table[3]/tbody/tr[2]/td/table/tbody/tr[3]/td').text

            except:
                divisions_pre_3 = "없음"
            try:
                apply_period = browser.find_element_by_xpath('/html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[4]/td/div/table/tbody/tr[1]/td/span[4]').text
            except:
                apply_period = "없음"

            browser.switch_to.default_content() # 상위로 빠져 나옴
            
            


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

            Enterprise_type=browser.find_element_by_xpath('//*[@class="info"]/dl[1]/dd').text
            employees =  browser.find_element_by_xpath('//*[@class="info"]/dl[2]/dd').text
            company_type =  browser.find_element_by_xpath('//*[@class="info"]/dl[3]/dd').text
            establishment_date =  browser.find_element_by_xpath('//*[@class="info"]/dl[4]/dd').text
            com_sales=browser.find_element_by_xpath('//*[@class="info"]/dl[5]/dd').text
            row=[i,browser.title,job_tit.get_text(),com_sales,employees,company_type,Enterprise_type,establishment_date, job_condition_text,views_count,Volunteer, Career, work_type, locate, assign_title, assign_task, assign_task_1, assign_task_2, qualification, qualification_1, qualification_2, divisions_pre, divisions_pre_1, divisions_pre_2, divisions_pre_3, apply_period , company_name, Salary, work_hour, academic_background]
            
            
            browser.close()
            time.sleep(0.1)
            
            browser.switch_to.window(curr_handle)

            print('-'*30)
            #row.extend([])
            try:
                ws.append(row)
            except:
                pass
    time.sleep(1)
    browser.quit()
wb.save('사람인 웹 스크래핑.xlsx')

