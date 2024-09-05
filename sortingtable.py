from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
browserSortedVeggitables =[]
service_obj = Service("/home/cbnits/Downloads/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
#click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
# collect all veggie names -> BrowserSortedveggieList ( A,B, C)
browserveggitables = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in browserveggitables:
    browserSortedVeggitables.append(ele.text)

originalBrowserSortedList = browserSortedVeggitables.copy()

# Sort this BrowserSortedveggieList => newSortedList -> (A,B,C)
browserSortedVeggitables.sort()

assert browserSortedVeggitables== originalBrowserSortedList
print("Elements are in sorted order")