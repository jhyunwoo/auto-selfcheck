import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as pg

# open self check web site
driver = webdriver.Chrome(
    '/Volumes/T7 Touch/Programing/auto-selfcheck/chromedriver')
driver.get('https://hcs.eduro.go.kr/#/loginHome')
