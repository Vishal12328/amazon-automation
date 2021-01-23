from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import cred

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome()
action = ActionChains(driver)



driver.get('http://www.amazon.in')

 
firstLevelMenu = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span[2]')
action.move_to_element(firstLevelMenu).perform()

 
secondLevelMenu = driver.find_element_by_xpath('//*[@id="nav-flyout-ya-signin"]/a/span')
secondLevelMenu.click()


signinelement = driver.find_element_by_xpath('//*[@id="ap_email"]')
signinelement.send_keys(cred.gmail)


cont = driver.find_element_by_xpath('//*[@id="continue"]')
cont.click()


passwordelement = driver.find_element_by_xpath('//*[@id="ap_password"]')
passwordelement.send_keys(cred.password)


login = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
login.click()
