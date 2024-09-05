import time
from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

""""Activate headless mode"""
headless = webdriver.ChromeOptions()
headless.add_argument("headless")
service_obj = Service("/home/cbnits/Downloads/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=headless)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

""""Handle Javascript code using execute_script()"""
#to scroll page upto axis 0, 500
# driver.execute_script("window.scrollBy(0, 500);")
#to scroll page below
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
#taking screen shot
driver.get_screenshot_as_file("firstSS.png")

