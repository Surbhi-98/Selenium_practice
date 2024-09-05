import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/home/cbnits/Downloads/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

""""way to handle Autosuggest Dropdown"""
driver.find_element(By.ID, "autosuggest").send_keys("ind")
#Explicit Wait  
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//li[@class = 'ui-menu-item']/a[@class='ui-corner-all']")))
countries = driver.find_elements(By.XPATH, "//li[@class = 'ui-menu-item']/a[@class='ui-corner-all']")
print(len(countries))
for country in countries:
    country_name = country.text
    if country_name == "India":
        country.click()
        break

""""assert dynamic text using get_attribute
    get_attribute() return string"""
# print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
    
