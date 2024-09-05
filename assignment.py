import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

service_obj = Service("/home/cbnits/Downloads/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.facebook.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@name='email']").send_keys("sayanii.sengupta.6@gmail.com")  # use your mail
driver.find_element(By.XPATH, "//input[@name='pass']").send_keys("Sayani@6")  # use your password
driver.find_element(By.XPATH, "//button[@name='login']").click()
driver.find_element(By.XPATH, "//div[@class='alzwoclg om3e55n1']").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//span[text()='Settings & privacy']").click()
driver.find_element(By.XPATH, "//span[text()='Settings & privacy']").click()
# time.sleep(3)
driver.find_element(By.XPATH, "//span[text()='Settings']").click()
# driver.find_element(By.XPATH, "//span[@xpath='41']").click()
# time.sleep(2)

# click mobile
driver.find_element(By.XPATH, "//span[normalize-space()='Mobile']").click()
# switch to the iframe

# time.sleep(2)

driver.find_element(By.XPATH, "//span[contains(text(),'Blocking')]").click()
# time.sleep(2)
# click logout
driver.find_element(By.XPATH, "//*[local-name()='image']").click()
# time.sleep(1)
driver.find_element(By.XPATH, "//*[local-name()='image']").click()

driver.close()