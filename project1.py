from selenium import webdriver
import time

username = input('Enter your Username or email  :')
password = input('Enter your password :')

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.facebook.com/')

time.sleep(4)
search = driver.find_element_by_id('email')
search.send_keys(username)
time.sleep(4)
search = driver.find_element_by_id('pass')
search.send_keys(password)
time.sleep(4)
button = driver.find_element_by_id('u_0_b')
button.click()