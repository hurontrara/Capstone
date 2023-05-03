from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from copy import deepcopy

def add_check(studentNum, password): # 아디 / 비번 받아서 로그인 가능한가 + 기존에 가입되어 있지 않은 회원인가(DB)
    global driver

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # try:   
    driver = webdriver.Chrome('/home/ubuntu/Capstone/chromedriver', chrome_options=chrome_options)  # 경로 수정 필요
    # except:
    #     driver = webdriver.Chrome('C:/Users/Study/Desktop/Projects/Capstone/source/chromedriver.exe', chrome_options=chrome_options)
    
    driver.get('https://wis.hufs.ac.kr/src08/jsp/index.jsp')  # 종정시 로그인 페이지
    driver.find_element_by_xpath('/html/body/div/form[3]/div[2]/div/div[2]/div/input[1]').send_keys(f'{studentNum}')
    driver.find_element_by_xpath('/html/body/div/form[3]/div[2]/div/div[2]/div/input[2]').send_keys(f'{password}')
    driver.find_element_by_xpath('/html/body/div/form[3]/div[2]/div/div[2]/div/a').click() # log-in

    try:
        driver.current_url
        window_handles = driver.window_handles
        for handle in window_handles:
            driver.switch_to.window(handle)
            driver.close()

        return True
    
    except:
        driver.close()
        return False
    

def refresh():
    driver.refresh()

def close():
    global driver

    window_handles = driver.window_handles
    for handle in window_handles:
        driver.switch_to.window(handle)
        driver.close()



def entranceSystem(id, password):   # 아디 빌려서 체크
    global driver

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # try:   
    driver = webdriver.Chrome('/home/ubuntu/Capstone/chromedriver', chrome_options=chrome_options)  # 경로 수정 필요
    # except:
    #     driver = webdriver.Chrome('C:/Users/Study/Desktop/Projects/Capstone/source/chromedriver.exe', chrome_options=chrome_options)

    driver.get('https://wis.hufs.ac.kr/src08/jsp/index.jsp')  # 종정시 로그인 페이지
    driver.find_element_by_xpath('/html/body/div/form[3]/div[2]/div/div[2]/div/input[1]').send_keys(f'{id}')
    driver.find_element_by_xpath('/html/body/div/form[3]/div[2]/div/div[2]/div/input[2]').send_keys(f'{password}')
    driver.find_element_by_xpath('/html/body/div/form[3]/div[2]/div/div[2]/div/a').click() # log-in

    try:
        driver.find_element_by_xpath('/html/body/div[2]/form/div[2]/button[2]').click()  # 비밀번호 변경
    except:
        pass

    time.sleep(1)

    tabs = driver.window_handles
    try:
        driver.switch_to.window(tabs[1])      # 팝업창 닫기
        driver.close()
    except:
        pass

    driver.switch_to.window(tabs[0])

    time.sleep(1)

def getName():
    driver.switch_to.default_content()
    frame1 = driver.find_element_by_xpath('/html/frameset/frameset/frame[1]')
    driver.switch_to.frame(frame1)

    name = driver.find_element_by_xpath('/html/body/div/table[1]/tbody/tr/td/div[2]/table/tbody/tr[2]/td').text[2:]

    return name


def getMajor():
    pageMoveToMajorManagement()

    frame = driver.find_element_by_xpath('/html/frameset/frameset/frame[2]')
    driver.switch_to.frame(frame)
    major = driver.find_element_by_xpath('/html/body/div/form/div/table/tbody/tr[2]/td[3]').text # 국제통상 (International Economics and Law)
    minor = driver.find_element_by_xpath('/html/body/div/form/div/table/tbody/tr[3]/td[3]').text # AI융합전공(Software&AI) (Artificial Intelligence Convergence(Software&AI) )
    double_major = (driver.find_element_by_xpath('/html/body/div/form/div/table/tbody/tr[3]/td[2]').text == '이중전공')  # T : 이중전공 F : 부전공 => 전공심화는 일단 배제

    return major, minor, double_major

def getClassNumberList():
    pageMoveToScoreGraduateManagement()

    frame1 = driver.find_element_by_xpath('/html/frameset/frameset/frame[2]')
    driver.switch_to.frame(frame1)
    frame2 = driver.find_element_by_xpath('/html/frameset/frame[2]')
    driver.switch_to.frame(frame2)
    credit = list(map(float, [i.text for i in driver.find_element_by_xpath('/html/body/div/form/div[1]/table/tbody/tr[2]').find_elements_by_tag_name('td')][1:]))

    return credit

def getClassList():
    pageMoveToScoreGraduateManagement()

    frame1 = driver.find_element_by_xpath('/html/frameset/frameset/frame[2]')
    driver.switch_to.frame(frame1)
    frame2 = driver.find_element_by_xpath('/html/frameset/frame[3]')
    driver.switch_to.frame(frame2)
    tr_tag_list = driver.find_element_by_xpath('/html/body/div/form/div[2]/table/tbody').find_elements_by_tag_name('tr') # Tag Name : <tr> list  -> iter 

    class_info = [] # 2차원 배열 # [['국제통상학과','D02103',' Mathematics for Economics (Mathematics for Economics)','1전공','3','A+','', '', '', "2018 - 1"], ... ]
    finished_semester = 0
    semeter = None
    for tr_tag in tr_tag_list:
        td_tag_list = tr_tag.find_elements_by_tag_name('td')
        if len(td_tag_list) < 3:
            if (len(td_tag_list) == 1) and (int(td_tag_list[0].get_attribute('colspan')) == 9):  # 2018 - 1
                finished_semester += 1
                semester = td_tag_list[0].text            # "2018 - 1"
        else:  # general case
            class_info.append([i.text for i in td_tag_list] + [semester])
    
    return class_info, finished_semester

def getExamPapers():
    pageMoveToExamPapersManagement()

    frame1 = driver.find_element_by_xpath('/html/frameset/frameset/frame[2]')
    driver.switch_to.frame(frame1)
    tr_tag_list = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody').find_elements_by_tag_name('tr')[1:]  # tr -> td
    graduate_exam_papers = []  # 2차원 배열 # [['1', '제1전공', '국제통상학과', '-', '-', '-', '-', '미완료', '-'], ['2', '이중전공', 'AI융합전공(Software&AI)', '-', '-', '-', '-', '미완료', '-']]
    for tr_tag in tr_tag_list:
        graduate_exam_papers.append([i.text for i in tr_tag.find_elements_by_tag_name('td')])

    return graduate_exam_papers

def getForeignOthers():
    pageMoveToExamPapersManagement()

    frame1 = driver.find_element_by_xpath('/html/frameset/frameset/frame[2]')
    driver.switch_to.frame(frame1)
    tr_tag_list = driver.find_element_by_xpath('/html/body/div/div[2]/table/tbody').find_elements_by_tag_name('tr')[1:]  # tr -> td
    graduate_foreign_others = [] # 2차원 배열 # [['1', '-', '-', '-', '미완료', '-']]
    for tr_tag in tr_tag_list:
        graduate_foreign_others.append([i.text for i in tr_tag.find_elements_by_tag_name('td')])

    return graduate_foreign_others

def getCultures():
    pageMoveToCultureManagement()   

    frame1 = driver.find_element_by_xpath('/html/frameset/frameset/frame[2]')
    driver.switch_to.frame(frame1)
    tbody_tag = driver.find_element_by_xpath('/html/body/div[1]/div/table/tbody')
    tr_tags = tbody_tag.find_elements_by_tag_name('tr')

    culture_list = []  # [['인성교육', '0', '0', '(None)'], ['세계시민교육', '0', '0', '(None)'], ...]
    for tr_tag in tr_tags:
        local_list = []  # ['미네르바인문', 2, 6, '취득과목보기']
        td_tags = tr_tag.find_elements_by_tag_name('td')
        if len(td_tags) == 4:
            for td_tag in td_tags:
                local_list.append(td_tag.text)
            
            culture_list.append(local_list)

    return culture_list

def pageMoveToMajorManagement():

    driver.switch_to.default_content()   # frame 초기화

    frame1 = driver.find_element_by_xpath('/html/frameset/frameset/frame[1]')
    driver.switch_to.frame(frame1)
    frame2 = driver.find_element_by_xpath('/html/body/div/div[2]/div/iframe')
    driver.switch_to.frame(frame2)
    
    driver.find_element_by_xpath('/html/body/div/a[2]').click()
    time.sleep(.5)
    driver.find_element_by_xpath('/html/body/div/div[2]/a[1]').click()             # 페이지 이동됨

    driver.switch_to.default_content()   # frame 초기화


def pageMoveToScoreGraduateManagement():    # 성적 취득 현황
    driver.switch_to.default_content()   # frame 초기화

    frame1 = driver.find_element_by_xpath('/html/frameset/frameset/frame[1]')
    driver.switch_to.frame(frame1)
    frame2 = driver.find_element_by_xpath('/html/body/div/div[2]/div/iframe')
    driver.switch_to.frame(frame2)
    driver.find_element_by_xpath('/html/body/div/a[4]').click()
    time.sleep(.5)
    driver.find_element_by_xpath('/html/body/div/div[4]/a[2]').click()

    driver.switch_to.default_content()   # frame 초기화

def pageMoveToCultureManagement():
    driver.switch_to.default_content()   # frame 초기화

    frame1 = driver.find_element_by_xpath('/html/frameset/frameset/frame[1]')
    driver.switch_to.frame(frame1)
    frame2 = driver.find_element_by_xpath('/html/body/div/div[2]/div/iframe')
    driver.switch_to.frame(frame2)
    driver.find_element_by_xpath('/html/body/div/a[4]').click()
    time.sleep(.5)
    driver.find_element_by_xpath('/html/body/div/div[4]/a[4]').click()

    driver.switch_to.default_content()   # frame 초기화

def pageMoveToExamPapersManagement():   # 졸시 / 논문 

    driver.switch_to.default_content()

    frame1 = driver.find_element_by_xpath('/html/frameset/frameset/frame[1]')
    driver.switch_to.frame(frame1)
    frame2 = driver.find_element_by_xpath('/html/body/div/div[2]/div/iframe')
    driver.switch_to.frame(frame2)
    driver.find_element_by_xpath('/html/body/div/a[4]').click()
    time.sleep(.5)
    driver.find_element_by_xpath('/html/body/div/div[4]/a[3]').click()

    driver.switch_to.default_content()   # frame 초기화

