from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service
service_obj = Service("/home/cbnits/Downloads/chromedriver")
# driver = webdriver.Chrome(executable_path="/home/cbnits/Downloads/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.tutorialspoint.com/index.htm")
driver.maximize_window()
print(driver.current_url)
print(driver.title)
print(driver.current_window_handle)
print(driver.command_executor)
driver.get("https://www.tutorialspoint.com/market/login.asp")
driver.back()
driver.refresh()
driver.forward()
driver.minimize_window()
driver.close()