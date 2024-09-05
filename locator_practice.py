from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/home/cbnits/Downloads/chromedriver")
driver = webdriver.Chrome(service=service_obj)

""""Login to page, type wrong email address and assert error message display as toaster"""
# driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("niccesurbhi@gmail.com")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("abcd@1234")
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("abcd@1234")
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@toast-component]/div[@role = 'alertdialog']")))
toaster_text = driver.find_element(By.XPATH, "//div[@toast-component]/div[@role = 'alertdialog']").text
print(toaster_text)
# if toaster_text.find("User Not found."):
#     print("assertion successfull")
# print("assertion successfull")
assert "Not found." in toaster_text
print("assertion successfull")