import time
from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

service_obj = Service("/home/cbnits/Downloads/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

""""Handle Dynamic Check Box
    is_selected return true for success
    False for Failure"""
check_box = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(check_box))
for check in check_box:  
    if check.get_attribute("id") == "checkBoxOption2":
        check.click()
        #is_selected is used to check whether the box is selected or not
        assert check.is_selected()
        break

""""Handle Dynamic Radio Button
    is_selected return true for success
    False for Failure"""
# radios = driver.find_elements(By.XPATH, "//input[@class='radioButton']")
# print(len(radios))
# for radio in radios:
#     if radio.get_attribute("value") == "radio3":
#         radio.click()
#         #is_selected is used to check whether the box is selected or not
#         assert radio.is_selected()
#         break

""""Handle Radio Button when user knows that position is never changed
    is_selected return true for success
    False for Failure"""
radios = driver.find_elements(By.XPATH, "//input[@class='radioButton']")
radios[2].click()
radios[2].is_selected()

""""Handle Statis Dropdown Button"""
static_drop = Select(driver.find_element(By.ID, "dropdown-class-example"))
static_drop.select_by_value("option1")

""""way to use is_display() in selenium
    is_display return true for success
    False for Failure"""
assert driver.find_element(By.CLASS_NAME, "displayed-class").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.CLASS_NAME, "displayed-class").is_displayed()
driver.find_element(By.ID, "show-textbox").click()
assert driver.find_element(By.CLASS_NAME, "displayed-class").is_displayed()

""""Handle JavaScript Alert Popup
    to handle alert we have to switch to the alert using switch_to
    to click on okay botton use accept()
    and for cancel button use dismiss()"""
#Button 1
find_text = "Surbhi"
driver.find_element(By.ID, "name").send_keys(find_text)
driver.find_element(By.ID, "alertbtn").click()
alert_box = driver.switch_to.alert
alert_text = alert_box.text
print(alert_text)
assert find_text in alert_text
# wait = WebDriverWait(driver, 10)
# wait.until(expected_conditions.element_to_be_clickable((alert_box.accept())))
alert_box.accept()
#button 2
driver.find_element(By.ID, "name").send_keys(find_text)
driver.find_element(By.ID, "confirmbtn").click()
another_alert_box = driver.switch_to.alert
another_alert_text = another_alert_box.text
print(another_alert_text)
assert find_text in another_alert_text
another_alert_box.dismiss()


