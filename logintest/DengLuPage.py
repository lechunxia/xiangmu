from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
     url = "https://test-books.maishumaishu.com/login"
     username_input_loc = (By.NAME, "cid")
     userid_input_loc = (By.NAME, "uid")
     password_input_loc = (By.NAME, "password")
     login_button_loc = (By.CLASS_NAME, "btn")

     def __init__(self, driver):
          self.driver = driver

     def open(self):
          self.driver.get(self.url)

     def input_username(self, username):
          self.driver.find_element(*self.username_input_loc).send_keys(username)

     def input_userid(self,userid):
          self.driver.find_element(*self.userid_input_loc).send_keys(userid)

     def input_password(self, password):
          self.driver.find_element(*self.password_input_loc).send_keys(password)

     def click_login_button(self):
          self.driver.find_element(*self.login_button_loc).click()

     def login(self, username, userid, password):
          self.open()
          self.input_username(username)
          self.input_userid(userid)
          self.input_password(password)
          self.click_login_button()



