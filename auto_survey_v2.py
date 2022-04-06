# 패키지 불러오기
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import telegram
import datetime
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

# 크롬 드라이버 설정
s = Service('/Volumes/T7_Touch/Programing/auto-selfcheck/chromedriver')
driver = webdriver.Chrome(service=s)

# 텔레그램 설정
telegram_token = '5011939727:AAF9YItRZACFScdSY7Qr9E0uz1oXXuhuNtw'

telegram_chat_id = 757343637

bot = telegram.Bot(token=telegram_token)


"""def Area"""


def get_webpage():  # 자가진단 웹페이지 띄우기
    driver.get('https://hcs.eduro.go.kr/#/loginHome')
    time.sleep(1)
    driver.maximize_window()


def move_to_login_page():  # 로그인 페이지 이동
    driver.find_element(
        By.XPATH, '/html/body/app-root/div/div[1]/div/button').click()
    time.sleep(1)
    driver.find_element(By.ID, 'schul_name_input').click()
    time.sleep(1)


def city():  # 충청남도 입력
    driver.find_element(By.ID, 'sidolabel').click()
    time.sleep(1)
    driver.find_element(
        By.XPATH, '/html/body/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td/select/option[13]').click()
    time.sleep(1)


def school_level():  # 고등학교 입력
    driver.find_element(By.ID, 'crseScCode').click()
    time.sleep(1)
    driver.find_element(
        By.XPATH, '//*[@id="crseScCode"]/option[5]').click()
    time.sleep(1)


def school_name():  # 충남삼성고 입력 후 선택
    driver.find_element(By.ID, 'orgname').click()
    time.sleep(1)
    driver.find_element(By.ID, 'orgname').send_keys('충남삼성고')
    time.sleep(1)
    driver.find_element(
        By.XPATH, '/html/body/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click()
    time.sleep(1)
    driver.find_element(
        By.XPATH, '//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a/p/a').click()
    time.sleep(1)
    driver.find_element(
        By.XPATH, '//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()
    time.sleep(1)


def name():  # 이름 입력
    driver.find_element(By.ID, 'user_name_input').click()
    time.sleep(1)
    driver.find_element(By.ID, 'user_name_input').send_keys('전현우')
    time.sleep(1)


def birth_date():  # 생년월일 입력
    driver.find_element(By.ID, 'birthday_input').click()
    time.sleep(1)
    driver.find_element(
        By.XPATH, '/html/body/app-root/div/div[1]/div[2]/div/div[2]/div/div[1]/table/tbody/tr[3]/td/input').send_keys('050228')
    time.sleep(1)


def move_to_password_page():  # 비밀번호 입력 페이지로 이동
    driver.find_element(By.XPATH, '//*[@id="btnConfirm"]').click()
    time.sleep(1)


def password_step1():
    driver.find_element(By.XPATH, '//*[@id="password"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="password"]').click()
    time.sleep(3)


def password_step2():
    driver.find_element(
        By.XPATH, '/html/body/div[2]/div[1]/div[4]/a').click()
    time.sleep(1)
    driver.find_element(
        By.XPATH, '/html/body/div[2]/div[1]/div[4]/a').click()
    time.sleep(1)
    driver.find_element(
        By.XPATH, '/html/body/div[2]/div[1]/div[9]/a').click()
    time.sleep(1)
    driver.find_element(
        By.XPATH, '/html/body/div[2]/div[1]/div[9]/a').click()
    time.sleep(1)


def move_to_my_main_page():  # move to main page of survey
    driver.find_element(By.XPATH, '//*[@id="btnConfirm"]').click()
    time.sleep(1)


def move_to_survey_page():
    driver.find_element_by_xpath(
        '//*[@id="container"]/div/section[2]/div[2]/ul/li[1]/a/span[1]').click()
    time.sleep(1)


def survey():  # 설문조사 실행
    driver.find_element(
        By.XPATH, '/html/body/app-root/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/dl[1]/dd/ul/li[1]/input').click()
    time.sleep(1)
    driver.find_element(
        By.XPATH, '/html/body/app-root/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/dl[2]/dd/ul/li[1]/input').click()
    time.sleep(1)
    driver.find_element(
        By.XPATH, '/html/body/app-root/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/dl[3]/dd/ul/li[1]/input').click()
    time.sleep(1)
    driver.find_element(
        By.XPATH, '/html/body/app-root/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/dl[4]/dd/ul/li[1]/input').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="btnConfirm"]').click()
    time.sleep(1)
    driver.find_element(
        By.XPATH, '/html/body/app-root/div/div[1]/div[1]/ul/li/a/span').click()
    time.sleep(1)


# 프로그램 메인
feature_of_0 = '<a href="#none" class="transkey_div_3_2" onclick="tk.start(event,0);" role="button" tabindex="0" aria-label="0"></a>'
feature_of_9 = '<a href="#none" class="transkey_div_3_2" onclick="tk.start(event,11);" role="button" tabindex="0" aria-label="9"></a>'


count = 0
while True:
    # 시간 설정
    now = datetime.datetime.now()
    now_time = now.strftime('%H:%M:%S')
    now_date = now.strftime("(%m월 %d일)")

    if now_time == '00:00:00':
        count = 0

    if count == 0:
        get_webpage()

        # 본인인증 페이지 이동
        move_to_login_page()

        city()

        school_level()

        school_name()

        name()

        birth_date()

        move_to_password_page()

        while True:

            password_step1()

            html_source = driver.page_source

            if feature_of_0 in html_source and feature_of_9 in html_source:
                break
            else:
                driver.find_element(
                    By.XPATH, '/html/body/div[2]/div[1]/div[1]/a').click()

        password_step2()
        move_to_my_main_page()

        html_source = driver.page_source

        if "정상" in html_source:
            bot.sendMessage(chat_id=telegram_chat_id,
                            text='자가진단을 완료하였습니다 ' + now_date)
            driver.close()
            count = 1
            time.sleep(1)

        else:
            move_to_survey_page()
            survey()
            bot.sendMessage(chat_id=telegram_chat_id,
                            text='자가진단을 완료하였습니다 ' + now_date)
            count = 1
            driver.close()
            time.sleep(1)
        s = Service('/Volumes/T7_Touch/Programing/auto-selfcheck/chromedriver')
        driver = webdriver.Chrome(service=s)
        time.sleep(1)
        driver.minimize_window()
        time.sleep(1)
