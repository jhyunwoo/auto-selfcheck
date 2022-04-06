import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as pg
import telegram
import datetime

# telegram setting
telegram_token = '5011939727:AAF9YItRZACFScdSY7Qr9E0uz1oXXuhuNtw'

telegram_chat_id = 757343637

bot = telegram.Bot(token=telegram_token)


def city():
    driver.find_element_by_id('sidolabel').click()
    # pg.moveTo(1000, 750)
    for i in range(12):
        pg.press('down')
    time.sleep(1)
    pg.press('enter')


def school_level():
    driver.find_element_by_id('crseScCode').click()
    for i in range(4):
        pg.press('down')
    pg.press('enter')


def school_name():
    driver.find_element_by_id('orgname').click()
    driver.find_element_by_id('orgname').send_keys('충남삼성고')
    pg.press('enter')
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a/p/a').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()


def name():
    driver.find_element_by_id('user_name_input').click()
    time.sleep(1)
    driver.find_element_by_id('user_name_input').send_keys('전현우')
    time.sleep(1)


def birth_date():
    driver.find_element_by_id('birthday_input').click()
    pg.write('050228')
    time.sleep(1)


def password_click():
    driver.find_element_by_xpath('//*[@id="password"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="password"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[4]/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[4]/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[9]/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[9]/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()


def survey():
    driver.find_element_by_xpath(
        '/html/body/app-root/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/dl[1]/dd/ul/li[1]/input').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '/html/body/app-root/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/dl[2]/dd/ul/li[1]/input').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '/html/body/app-root/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/dl[3]/dd/ul/li[1]/input').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '/html/body/app-root/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/dl[4]/dd/ul/li[1]/input').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '/html/body/app-root/div/div[1]/div[1]/ul/li/a/span').click()


def log_in():
    # input city name
    city()
    time.sleep(1)

    # change school level
    school_level()
    time.sleep(1)

    # input school name
    school_name()
    time.sleep(1)

    # input my name
    name()
    time.sleep(1)

    # input my birth day
    birth_date()
    pg.press('enter')
    time.sleep(3)

    # enter my password
    password_click()
    time.sleep(1)

    # move to main page of survey
    driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
    time.sleep(1)


while True:
    now = datetime.datetime.now()
    nowTime = now.strftime('%H:%M:%S')
    nowDate = now.strftime("(%m월 %d일)")
    if nowTime == '17:41:00':

        # open self check web site
        driver = webdriver.Chrome(
            '/Volumes/T7 Touch/Programing/auto-selfcheck/chromedriver')
        driver.get('https://hcs.eduro.go.kr/#/loginHome')
        time.sleep(1)

        try:
            # move to login page
            driver.find_element_by_id('btnConfirm2').click()
            time.sleep(2)
            driver.find_element_by_id('schul_name_input').click()
            time.sleep(1)
            log_in()
            time.sleep(2)

            html_source = driver.page_source
            if "정상" in html_source:
                bot.sendMessage(chat_id=telegram_chat_id,
                                text='자가진단을 완료하였습니다 '+nowDate)
                driver.close()
            else:
                # click survey page
                driver.find_element_by_xpath(
                    '//*[@id="container"]/div/section[2]/div[2]/ul/li[1]/a/span[1]').click()
                time.sleep(1)

                # enter my condition on survey
                survey()
                time.sleep(1)
                bot.sendMessage(chat_id=telegram_chat_id,
                                text='자가진단을 완료하였습니다 '+nowDate)
                driver.close()

        except:
            bot.sendMessage(chat_id=telegram_chat_id, text='자가진단 오류')
            driver.close()
            # open self check web site
            driver = webdriver.Chrome(
                '/Volumes/T7 Touch/Programing/auto-selfcheck/chromedriver')
            driver.get('https://hcs.eduro.go.kr/#/loginHome')
            time.sleep(1)
            # move to login page
            driver.find_element_by_id('btnConfirm2').click()
            time.sleep(2)
            driver.find_element_by_id('schul_name_input').click()
            time.sleep(1)
            log_in()
            time.sleep(2)

            html_source = driver.page_source
            if "정상" in html_source:
                bot.sendMessage(chat_id=telegram_chat_id,
                                text='자가진단을 완료하였습니다 ' + nowDate)
                driver.close()
            else:
                # click survey page
                driver.find_element_by_xpath(
                    '//*[@id="container"]/div/section[2]/div[2]/ul/li[1]/a/span[1]').click()
                time.sleep(1)

                # enter my condition on survey
                survey()
                time.sleep(1)
                bot.sendMessage(chat_id=telegram_chat_id,
                                text='자가진단을 완료하였습니다 '+nowDate)
                driver.close()
