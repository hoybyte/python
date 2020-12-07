import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user = 'guest'
pw = 'changeme'
driver = webdriver.Chrome()
driver.get("https://pyplanet.herokuapp.com/login")
driver.find_element_by_id('id_username').send_keys(user)
driver.find_element_by_id('id_password').send_keys(pw + Keys.RETURN)



if __name__ == "__main__":
    pass