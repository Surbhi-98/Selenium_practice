from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("/home/cbnits/Downloads/chromedriver")
driver = webdriver.Chrome(service=service_obj)

#using attribute name
driver.get("https://rahulshettyacademy.com/angularpractice/")


driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("Surbhi")
driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("abcd@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(3) input").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "#exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR, "#inlineRadio2").click()
# driver.find_element(By.CSS_SELECTOR, "form div:nth-child(3) input").send_keys("123456")

""""Handle Static Dropdown using Select class"""
Gender = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
#by using select by index 
# Gender.select_by_index(1)
#by using select by text that display in page
Gender.select_by_visible_text("Female")

driver.find_element(By.CLASS_NAME, "btn-success").click()
message = driver.find_element(By.XPATH, "//div[@class = 'alert alert-success alert-dismissible']").text
print(message)
assert "Success!" in message

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Agrahari")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()




