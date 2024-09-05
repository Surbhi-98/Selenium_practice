from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/home/cbnits/Downloads/chromedriver")
driver = webdriver.Chrome(service=service_obj)

""""Login to Spotify application"""
#using attribute name
driver.get("https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fopen.spotify.com%2F")
# driver.find_element(By.ID, "login-username").send_keys("smilysurbhi@gmail.com")
# driver.find_element(By.ID, "login-password").send_keys("surbhi@1998")
                        # driver.find_element(By.ID, "login-remember").click()
# driver.find_element(By.CLASS_NAME, "ButtonInner-sc-14ud5tc-0").click()
# driver.refresh()

#using xpath
#syntax - //tagname[@attributename = 'vale'] --> ex:- //input[@type='submit']
driver.find_element(By.XPATH, "//input[@id='login-username']").send_keys("smilysurbhi@gmail.com")
# driver.find_element(By.XPATH, "//input[@id='login-password']").send_keys("surbhi@1998")
                    # driver.find_element(By.XPATH, "//div[@class='ButtonInner-sc-14ud5tc-0']").click()
# driver.find_element(By.CLASS_NAME, "ButtonInner-sc-14ud5tc-0").click()

#using cssselector
#syntax - tagname[attributename = 'vale'] --> ex:- input[type='submit']
# driver.find_element(By.CSS_SELECTOR, "input[id='login-username']").send_keys("smilysurbhi@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input[id='login-password']").send_keys("surbhi@1998")
            # driver.find_element(By.XPATH, "//div[@class='ButtonInner-sc-14ud5tc-0']").click()
driver.find_element(By.CLASS_NAME, "ButtonInner-sc-14ud5tc-0").click()



